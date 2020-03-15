import { User } from './user.model';
import { Question, QuestionEdit } from './question.model';

export class Quiz {
    public id: number;
    public owner: User;
    public title: string;
    public questions: Question[] = [];
    // tslint:disable-next-line: variable-name
    public questions_count: number;
    public description: string;
    constructor() {

    }
}
export class QuizCreate {
    public title: string;
    public description: string;
    constructor() {
    }
}
export class QuizEdit {
    public id = 0;
    public title = '';
    public description = '';
    public questions: QuestionEdit[] = [];
}
