import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit, Input, ElementRef } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  @Input() csrtToken: string;
  constructor(private profileService: ProfileService, private _elementRef: ElementRef) {
    const native = this._elementRef.nativeElement;
    const test = native.getAttribute("csrftoken");
    this.csrtToken = test;
  }
  ngOnInit(): void {
    console.log('d' + this.csrtToken);
    this.profileService.csrtToken = this.csrtToken;
    this.profileService.updateProfile();
  }
}
