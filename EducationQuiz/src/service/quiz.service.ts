import { Injectable } from '@angular/core';
import { ProfileService } from './profile.service';
import { HttpClient } from '@angular/common/http';
import { QuizCreate, QuizEdit } from 'src/models/quiz.model';

@Injectable({
  providedIn: 'root'
})
export abstract class QuizService {

  constructor(public profileService: ProfileService, public htttpClient: HttpClient) { }

  public abstract createQuiz(quiz: QuizCreate);
  abstract getQuiz(id: number);
  abstract updateQuiz(quiz: QuizEdit);
}

