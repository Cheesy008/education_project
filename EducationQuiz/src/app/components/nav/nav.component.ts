import { Component, OnInit } from '@angular/core';
import { ProfileService } from 'src/service/profile.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  isLogin = false;
  constructor(private profileService: ProfileService) { }
  checkAuth() {
    //this.isLogin = this.profileService.isUserAuth();
  }
  ngOnInit(): void {
    //this.checkAuth();
  }

}
