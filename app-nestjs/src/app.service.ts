import { Injectable } from '@nestjs/common';
import { createWriteStream } from 'fs';

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

  writeFile(): null {
    const file = createWriteStream('teste.txt');

    for (let x = 0; x <= 10000; x++) {
      file.write('Writing...\n');
    }
    file.end();
    return;
  }
}
