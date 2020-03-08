import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  @Input() csrtToken: string;
  constructor(private profileService: ProfileService) {
  }
  ngOnInit(): void {
    this.profileService.csrtToken = this.csrtToken;
    this.profileService.updateProfile();
  }
}
