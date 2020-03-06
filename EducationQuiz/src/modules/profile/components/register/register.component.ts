import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  public registerForm: FormGroup;
  email = new FormControl('', [Validators.required, Validators.email]);

  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'Введите значение';
    }

    return this.email.hasError('email') ? 'Неправильная почта' : '';
  }
  constructor() {
    this.registerForm = new FormGroup({
      userName: new FormControl('Tom', Validators.required),
      userEmail: new FormControl('', [
        Validators.required,
        Validators.email
      ]),
      userPhone: new FormControl('', Validators.pattern('[0-9]{10}'))
    });
  }

  ngOnInit(): void {
  }

}
