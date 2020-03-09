import { Injectable } from '@angular/core';
import { ProfileService } from '../profile.service';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from 'src/models/user.model';
import { Subject, Observable } from 'rxjs';
import { TokenService } from '../token.service';

@Injectable({
  providedIn: 'root'
})

export class HttpProfileService implements ProfileService {


  public csrtToken: string;

  public authUser: User;
  public userSubject: Subject<User> = new Subject<User>();

  constructor(public http: HttpClient, public token: TokenService) { }

  public registration(model: RegistrationModel) {
    const body = {
      username: model.username,
      email: model.email,
      password1: model.password,
      password2: model.password,
      first_name: model.firstname,
      last_name: model.secondname,
      role: model.role
    };
    return this.http.post('api/profile/registration/', body, this.token.getHeaders());
  }
  public login(model: LoginModel) {
    const body = {
      email: model.email,
      password: model.password
    };
    console.log(body);
    return this.http.post('api/profile/login/', body, this.token.getHeaders());
  }
  public logout() {
    return this.http.post('api/profile/logout/', null, this.token.getHeaders());
  }
  public updateProfile(): void {
    this.http.get<User>('api/profile/', this.token.getHeaders()).subscribe((data) => {
      this.authUser = data;
      this.userSubject.next(data);
    }, (error) => {
      this.authUser = null;
      this.userSubject.next(null);
    });
  }

}
