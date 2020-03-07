import { Component, OnInit } from '@angular/core';
import { ProfileService } from 'src/service/profile.service';
import { User } from 'src/models/user.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  user: User;
  constructor(private profileService: ProfileService) { }

  ngOnInit(): void {
    //this.user = this.profileService.getAuthUser();
  }

}
