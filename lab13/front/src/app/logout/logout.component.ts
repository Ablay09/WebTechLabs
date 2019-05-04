import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.sass']
})
export class LogoutComponent implements OnInit {
  public logged = false;

  constructor(
    private provider: ProviderService,
    private location: Location
  ) { }

  ngOnInit() {
  }

  logout(){
    this.provider.logout().then(res => {
      localStorage.clear();
      console.log(localStorage)
    });
  }
}
