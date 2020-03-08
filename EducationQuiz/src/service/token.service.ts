import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TokenService {
  public static token: string;
  public getRequestOptions() {
    let headers = new Headers();
    headers.append('csrftoken', 'token');

    let options = new RequestOptions({ headers: headers });
  }
}
