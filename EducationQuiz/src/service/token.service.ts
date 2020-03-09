import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TokenService {
  public token: string;
  public getHeaders() {
    const httpHeaders = new HttpHeaders({
      'X-CSRFToken': this.token
    });
    console.log('headers: ' + httpHeaders.keys());
    const options = {
      headers: httpHeaders
    };
    return options;
  }
}
