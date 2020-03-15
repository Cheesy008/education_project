import { Question } from './question.model';

export class Answer {
    public id: number;
    public questionId: number;
    public question: Question;
    // tslint:disable-next-line: variable-name
    public answer_text: string;
    // tslint:disable-next-line: variable-name
    public is_correct: boolean;
}
export class AnswerEdit {
    public id = -1;
    public index: number;
    // tslint:disable-next-line: variable-name
    public answer_text: string = '';
    // tslint:disable-next-line: variable-name
    public is_correct: boolean;
}