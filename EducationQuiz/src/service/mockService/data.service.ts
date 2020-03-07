import { User } from './../../models/user.model';
import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
@Injectable({
  providedIn: 'root'
})
export class DataService implements InMemoryDbService {

  constructor() { }
  createDb() {

    const users: User[] = [
      new User(1, 'test1@test.com', 'user1', 'Nick', 'Kol', '123456qwerty'),
      new User(2, 'test2@test.com', 'user2', 'Nick', 'Kol', '123456qwerty'),
      new User(3, 'test3@test.com', 'user3', 'Nick', 'Kol', '123456qwerty'),
      new User(4, 'test4@test.com', 'user4', 'Nick', 'Kol', '123456qwerty'),
      new User(5, 'test5@test.com', 'user5', 'Nick', 'Kol', '123456qwerty'),
    ];

    return { users };

  }

}
