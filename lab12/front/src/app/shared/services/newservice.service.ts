import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MainService } from './main.service';

@Injectable({
  providedIn: 'root'
})
export class NewserviceService extends MainService {

  constructor(http: HttpClient) { 
    super(http);
  }

  
}
