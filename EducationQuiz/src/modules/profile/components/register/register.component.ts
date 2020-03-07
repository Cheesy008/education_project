import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { MustMatch } from 'src/validators/must-match.validator';
import { RegistrationModel } from 'src/models/registration.model';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  public registerForm: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    this.registerForm = this.formBuilder.group({
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
      role: new FormControl('student')
    }, {
      validator: MustMatch('password', 'confirmPassword')
    });
  }

  ngOnInit(): void {
  }
  registration() {
    const model = new RegistrationModel(this.registerForm.value.firstname,
      this.registerForm.value.secondname,
      this.registerForm.value.password,
      this.registerForm.value.еmail,
      this.registerForm.value.role);
    console.log(model);
  }
}
