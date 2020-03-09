import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { Observable, Subject } from 'rxjs';
import { User } from 'src/models/user.model';

@Injectable({
  providedIn: 'root'
})
export abstract class ProfileService {
  public authUser: User = null;
  public userSubject: Subject<User> = new Subject<User>();

  constructor(public http: HttpClient) { }

  public abstract registration(registrationModel: RegistrationModel): Observable<any>;
  public abstract login(loginModel: LoginModel): Observable<HttpResponse<any>>;
  public abstract logout();
  public abstract updateProfile(): void;
}
