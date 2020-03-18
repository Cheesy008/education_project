import { Injectable } from '@angular/core';
import { ProfileService } from './profile.service';
import { HttpClient } from '@angular/common/http';
import { QuizCreate, QuizEdit } from 'src/models/quiz.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export abstract class QuizService {

  constructor(public profileService: ProfileService, public htttpClient: HttpClient) { }

  public abstract createQuiz(quiz: QuizCreate);
  public abstract getQuizzes(page: number): Observable<any>;
  abstract getQuiz(id: number);
  abstract updateQuiz(quiz: QuizEdit);
}

