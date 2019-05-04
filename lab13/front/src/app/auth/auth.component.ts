import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { Location } from '@angular/common';
import { AuthService } from '../shared/services/auth.service';
@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.sass']
})
export class AuthComponent implements OnInit {

  public username: any = '';
  public password: any = '';

  constructor(
    private provider: ProviderService,
    private location: Location,
    private auth: AuthService
    ) { }

  
  navigateBack(){
    this.location.back()
  }

  ngOnInit() {
  }
  
  login() {
    if(this.username !== '' && this.password !== '') {
      this.auth.login(this.username, this.password);
    }
  }
}
