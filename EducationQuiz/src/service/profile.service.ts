import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { Observable, Subject } from 'rxjs';
import { User } from 'src/models/user.model';

@Injectable({
  providedIn: 'root'
})
export abstract class ProfileService {
  public csrtToken: string;

  public authUser: User = null;
  public userSubject: Subject<User> = new Subject<User>();

  constructor(public http: HttpClient) { }

  public abstract registration(registrationModel: RegistrationModel): Observable<any>;
  public abstract login(loginModel: LoginModel);
  public abstract updateProfile(): void;
}
