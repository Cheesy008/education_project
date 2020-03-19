import { Injectable } from '@angular/core';
import { QuizService } from '../quiz.service';
import { ProfileService } from '../profile.service';
import { HttpClient } from '@angular/common/http';
import { QuizCreate, QuizEdit } from 'src/models/quiz.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpQuizService implements QuizService {

  constructor(public profileService: ProfileService, public htttpClient: HttpClient) { }
  public getQuizzes(page: number): Observable<any> {
    return this.htttpClient.get<any>('api/quizzes/?page=' + page);
  }
  public createQuiz(quiz: QuizCreate) {
    const body = {
      title: quiz.title,
      description: quiz.description,
      questions: []
    };
    return this.htttpClient.post<any>('api/quizzes/', body);
  }
  getQuiz(id: number) {
    return this.htttpClient.get<any>('api/quizzes/' + id);
  }
  updateQuiz(quiz: QuizEdit) {
    const quistions = [];
    quiz.questions.forEach((d) => {
      const answers = [];
      d.answers.forEach((a) => {
        const r: any = {
          answer_text: a.answer_text,
          is_correct: a.is_correct
        };
        // tslint:disable-next-line: triple-equals
        if (a.id != -1) {
          r.id = a.id;
        }
        answers.push(r);
      });
      const r: any = {
        question_title: d.question_title,
        answers
      };
      // tslint:disable-next-line: triple-equals
      if (d.id != -1) {
        r.id = d.id;
      }
      quistions.push(r);
    });
    const body = {
      title: quiz.title,
      description: quiz.description,
      questions: quistions
    };
    console.log(body);
    return this.htttpClient.put<any>('api/quizzes/' + quiz.id + '/', body);

  }

}
