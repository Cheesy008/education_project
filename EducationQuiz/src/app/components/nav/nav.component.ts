import { Component, OnInit } from '@angular/core';
import { ProfileService } from 'src/service/profile.service';
import { User } from 'src/models/user.model';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {
  user: User = null;
  constructor(private profileService: ProfileService) { }
  ngOnInit(): void {
    this.profileService.userSubject.subscribe((data) => {
      console.log('nav');
      this.user = data;
    });
    this.profileService.updateProfile();
  }

}
