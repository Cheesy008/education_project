import { TestBed } from '@angular/core/testing';

import { HttpQuizService } from './http-quiz.service';

describe('HttpQuizService', () => {
  let service: HttpQuizService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HttpQuizService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
