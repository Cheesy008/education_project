import { User } from './user.model';
import { Question, QuestionEdit } from './question.model';

export class Quiz {
  public id: number;
  public owner: User;
  public ownerId: number;
  public title: string;
  public questions: Question[] = [];
  // tslint:disable-next-line: variable-name
  public questionsCount: number;
  public description: string;
  public isCompleted: boolean;
  public createDate: Date;
  constructor() {
  }
  public static parse(d: any): Quiz {
    return {
      id: d.id,
      title: d.title,
      owner: User.parse(d.owner),
      ownerId: d.owner_id,
      questionsCount: d.questions_count,
      description: d.description,
      isCompleted: d.test_completed,
      createDate: d.created,
      questions: d.questions
    };
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
