import { User } from './../models/user.model';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  authUser: User = new User('admin', 'Admin');
  constructor() { }

  public isUserAuth() { return User == null; }
  public getAuthUser(): User { return this.authUser; }
}
