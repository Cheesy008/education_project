import { MatCheckboxModule } from '@angular/material/checkbox';
import { QuizEdit } from './../../models/quiz.model';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { QuizzesListComponent } from './components/quizzes-list/quizzes-list.component';
import { QuizInfoComponent } from './components/quiz-info/quiz-info.component';
import { QuizDetailsComponent } from './components/quiz-details/quiz-details.component';
import { QuizCreateComponent } from './components/quiz-create/quiz-create.component';
import { FormsModule, ReactiveFormsModule, } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';
import { AppModule } from 'src/app/app.module';
import { QuizEditComponent } from './components/quiz-edit/quiz-edit.component';
import { QuestionEditComponent } from './components/question-edit/question-edit.component';
import { AnswerEditComponent } from './components/answer-edit/answer-edit.component';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatCardModule } from '@angular/material/card';
import { QuizPassComponent } from './components/quiz-pass/quiz-pass.component';

@NgModule({
  declarations: [
    QuizzesListComponent,
    QuizInfoComponent,
    QuizDetailsComponent,
    QuizCreateComponent,
    QuizEditComponent,
    QuestionEditComponent,
    AnswerEditComponent,
    QuizPassComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,
    MatButtonModule,
    MatCheckboxModule,
    MatPaginatorModule,
    MatCardModule,
    AppModule
  ],
  exports: [
    QuizCreateComponent,
    QuizEditComponent,
    FormsModule,
    ReactiveFormsModule]
})
export class QuizzesModule { }
