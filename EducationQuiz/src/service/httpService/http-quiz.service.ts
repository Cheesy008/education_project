import { Injectable } from '@angular/core';
import { QuizService } from '../quiz.service';
import { ProfileService } from '../profile.service';
import { HttpClient } from '@angular/common/http';
import { QuizCreate, QuizEdit } from 'src/models/quiz.model';

@Injectable({
  providedIn: 'root'
})
export class HttpQuizService implements QuizService {

  constructor(public profileService: ProfileService, public htttpClient: HttpClient) { }

  public createQuiz(quiz: QuizCreate) {
    const body = {
      title: quiz.title,
      description: quiz.description,
      questions: []
    };
    return this.htttpClient.post<any>('api/quizzes/', body);
  }
  getQuiz(id: number) {
  }
  updateQuiz(quiz: QuizEdit) {
  }

}
