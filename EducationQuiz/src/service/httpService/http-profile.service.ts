import { Injectable } from '@angular/core';
import { ProfileService } from '../profile.service';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpProfileService implements ProfileService {
  private baseUrl = 'http://127.0.0.1:8000/api/';
  private format = '?format=JSON';
  constructor(public http: HttpClient) { }
  public registration(model: RegistrationModel) {
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');
    const body = {
      email: model.email,
      password1: model.password,
      password2: model.passwordConfirm,
      first_name: model.firstname,
      last_name: model.secondname,
      role: model.role
    };
    console.log(body);
    return this.http.post(this.baseUrl + 'profile/registration', body, {
      headers: new HttpHeaders().set('Content-type', 'application/json'),
    });
  } public login(loginModel: LoginModel) {

  }


}
