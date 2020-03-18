import { Quiz } from './quiz.model';
import { Answer, AnswerEdit } from './answer.model';

export class Question {
    public id: number;
    public quizId: number;
    public quiz: Quiz;
    // tslint:disable-next-line: variable-name
    public question_title: string;
    public answers: Answer[] = [];

}
export class QuestionEdit {
    public id: number;
    // tslint:disable-next-line: variable-name
    public question_title: string = '';
    public answers: AnswerEdit[] = [];
}