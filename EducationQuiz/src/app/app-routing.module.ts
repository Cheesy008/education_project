
import { RegisterComponent } from './../modules/profile/components/register/register.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProfileComponent } from 'src/modules/profile/components/profile/profile.component';
import { LoginComponent } from 'src/modules/profile/components/login/login.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/login', component: LoginComponent },
  { path: 'profile/register', component: RegisterComponent },
  { path: 'profile/logout', component: ProfileComponent },
  { path: 'tests', component: HomeComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
