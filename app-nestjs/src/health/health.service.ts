import { Injectable } from '@nestjs/common';

@Injectable()
export class HealthService {
  cheackHealth(): string {
    const message = 'Healthy!';
    console.log(message);
    return message;
  }
  checkReady(): string {
    const message = 'Ready!';
    console.log(message);
    return message;
  }
}
// Utilize terminus - test external libs readiness
