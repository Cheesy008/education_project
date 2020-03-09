import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit, Input, ElementRef } from '@angular/core';
import { TokenService } from 'src/service/token.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  constructor(private tokenService: TokenService, private _elementRef: ElementRef) {
    const native = this._elementRef.nativeElement;
    const test = native.getAttribute("csrftoken");
    this.tokenService.token = test;
    console.log('token: ' + test);
  }
  ngOnInit(): void {

  }
}
