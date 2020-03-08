import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { MustMatch } from 'src/validators/must-match.validator';
import { RegistrationModel, RegistrationErrorsModel } from 'src/models/registration.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  public registerForm: FormGroup;
  isError = false;
  showLoading = false;
  errors: RegistrationErrorsModel;
  constructor(private formBuilder: FormBuilder, private profileService: ProfileService, private router: Router) {
    this.registerForm = this.formBuilder.group({
      username: new FormControl('Dima', Validators.required),
      firstname: new FormControl('Дмитрий', Validators.required),
      secondname: new FormControl('Павлов', Validators.required),
      еmail: new FormControl('test@test.com', [
        Validators.required,
        Validators.email
      ]),
      password: new FormControl('123456qwerty', [
        Validators.required
      ]),
      confirmPassword: new FormControl('123456qwerty', [
        Validators.required,
      ]),
      role: new FormControl('ST')
    }, {
      validator: MustMatch('password', 'confirmPassword')
    });
  }

  ngOnInit(): void { }
  registration() {
    const model = new RegistrationModel(this.registerForm.value.username,
      this.registerForm.value.firstname,
      this.registerForm.value.secondname,
      this.registerForm.value.password,
      this.registerForm.value.password,
      this.registerForm.value.еmail,
      this.registerForm.value.role);
    this.isError = false;
    this.showLoading = true;
    this.profileService.registration(model).subscribe((data) => {
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
