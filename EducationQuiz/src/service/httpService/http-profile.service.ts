import { Injectable } from '@angular/core';
import { ProfileService } from '../profile.service';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from 'src/models/user.model';
import { Subject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class HttpProfileService implements ProfileService {

  public authUser: User;
  public userSubject: Subject<User>;

  constructor(public http: HttpClient) { }
  public registration(model: RegistrationModel) {
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');
    const body = {
      username: model.username,
      email: model.email,
      password1: model.password,
      password2: model.password,
      first_name: model.firstname,
      last_name: model.secondname,
      role: model.role
    };
    console.log(body);
    return this.http.post('api/profile/registration/', body);
  }
  public login(loginModel: LoginModel) {

  }
  public updateProfile(): void {
    this.http.get('api/profile/').subscribe((data) => {
      this.authUser = data as User;
      this.userSubject.next(data as User);
    }, (error) => { });
  }

}
