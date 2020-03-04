import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfileComponent } from './components/profile/profile.component';
import { LoginComponent } from './components/profile/login/login.component';
import { RegisterComponent } from './components/register/register.component';

@NgModule({
  declarations: [ProfileComponent, LoginComponent, RegisterComponent],
  imports: [
    CommonModule
  ],
  exports: [ProfileComponent]
})
export class ProfileModule { 

}
