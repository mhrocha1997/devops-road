import { Controller, Get } from '@nestjs/common';
import { HealthService } from './health.service';

@Controller()
export class HealthController {
  constructor(private readonly appService: HealthService) {}

  @Get('/healthz')
  healthz(): string {
    return this.appService.cheackHealth();
  }

  @Get('/readyz')
  readyz(): string {
    return this.appService.checkReady();
  }
}
