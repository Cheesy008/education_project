import { QuizEditComponent } from './../modules/quizzes/components/quiz-edit/quiz-edit.component';
import { AuthActivatorService } from './../guards/auth-activator.service';

import { RegisterComponent } from './../modules/profile/components/register/register.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProfileComponent } from 'src/modules/profile/components/profile/profile.component';
import { LoginComponent } from 'src/modules/profile/components/login/login.component';
import { QuizzesListComponent } from 'src/modules/quizzes/components/quizzes-list/quizzes-list.component';
import { QuizCreateComponent } from 'src/modules/quizzes/components/quiz-create/quiz-create.component';
import { QuizDetailsComponent } from 'src/modules/quizzes/components/quiz-details/quiz-details.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/login', component: LoginComponent },
  { path: 'profile/register', component: RegisterComponent },
  { path: 'profile/logout', component: ProfileComponent },
  { path: 'quizzes', component: QuizzesListComponent },
  { path: 'quizzes/create', component: QuizCreateComponent, canActivate: [AuthActivatorService] },
  { path: 'quizzes/:id/edit', component: QuizEditComponent },
  { path: 'quizzes/:id', component: QuizDetailsComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
