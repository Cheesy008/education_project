import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';

@Injectable({
  providedIn: 'root'
})
export abstract class ProfileService {
  constructor(public http: HttpClient) { }
  public abstract registration(registrationModel: RegistrationModel);
  public abstract login(loginModel: LoginModel);
}
