import { LoginErrorsModel, LoginModel } from './../../../../models/login.model';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { ProfileService } from 'src/service/profile.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public loginForm: FormGroup;
  isError = false;
  showLoading = false;
  errors: LoginErrorsModel;
  constructor(private formBuilder: FormBuilder, private profileService: ProfileService, private router: Router) {
    this.loginForm = this.formBuilder.group({
      еmail: new FormControl('test@test.com', [
        Validators.required,
        Validators.email
      ]),
      password: new FormControl('123456qwerty', [
        Validators.required
      ])
    });
  }
  ngOnInit(): void { }
  login() {
    const model = new LoginModel(this.loginForm.value.email, this.loginForm.value.password);

    this.isError = false;
    this.showLoading = true;

    this.profileService.login(model).subscribe((data) => {
      this.showLoading = false;
      this.isError = false;
      this.profileService.updateProfile();
      this.router.navigate(['/profile']);
    }, (error) => {
      this.profileService.updateProfile();
      this.showLoading = false;
      this.errors = error.error;
      this.isError = true;
    });

  }
}
