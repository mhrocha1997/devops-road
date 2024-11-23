import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    console.log(process.env.APP);
    console.log(process.env.API_KEY);
    return 'Hello World!';
  }
  getExample(): string {
    return "I'm on K8S!!!";
  }
}
