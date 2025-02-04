import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, constr
from tortoise.contrib.fastapi import register_tortoise
from tortoise.models import Model
from tortoise import fields
from passlib.hash import bcrypt

# FastAPI app
app = FastAPI()


# Database Model
class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.hashed_password)


# Pydantic Models
class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: str

    class Config:
        from_attributes = True


# Utility Functions
def hash_password(password: str) -> str:
    return bcrypt.hash(password)


@app.get("/hello")
async def hello():
    return ""


# Routes
@app.post("/users", response_model=UserResponse)
async def create_user(user_create: UserCreate):
    existing_user = await User.filter(email=user_create.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user_create.password)
    user = await User.create(email=user_create.email, hashed_password=hashed_password)
    return user


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/{user_id}/verify-password")
async def verify_password_route(user_id: int, password: str):
    user = await User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.verify_password(password):
        return {"message": "Password is correct"}
    return {"message": "Password is incorrect"}


DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "yourdatabase")

DB_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": [__name__]},
    generate_schemas=True,
    add_exception_handlers=True,
)
