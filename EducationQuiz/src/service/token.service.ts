import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TokenService {
  public token: string;
  public getHeaders() {
    const headers = new HttpHeaders();
    headers.append('csrftoken', this.token);
    const options = {
      headers: headers
    };
    return options;
  }
}
