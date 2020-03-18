import { map } from 'rxjs/operators';
export class User {
  public id: number;
  public email: string;
  public username: string;
  public firstname: string;
  public secondname: string;
  public role: string;
  constructor() { }
  static parse(d: any): User {
    return {
      id: d.id,
      email: d.email,
      username: d.username,
      firstname: d.first_name,
      secondname: d.last_name,
      role: d.role
    };
  }
}
