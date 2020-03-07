
import { Injectable } from '@angular/core';
import { ProfileService } from 'src/service/profile.service';
import { RegistrationModel } from 'src/models/registration.model';
import { LoginModel } from 'src/models/login.model';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class MockProfileService implements ProfileService {
    constructor(public http: HttpClient) { }
    public registration(registrationModel: RegistrationModel) {
        
    }
    public login(loginModel: LoginModel) {
        
    }


}