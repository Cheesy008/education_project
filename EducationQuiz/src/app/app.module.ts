import { MatCheckboxModule } from '@angular/material/checkbox';
import { QuizzesModule } from './../modules/quizzes/quizzes.module';
import { TokenService } from './../service/token.service';
import { LoadingComponent } from './components/loading/loading.component';
import { HttpProfileService } from './../service/httpService/http-profile.service';
import { ProfileService } from 'src/service/profile.service';
import { ProfileModule } from './../modules/profile/profile.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavComponent } from './components/nav/nav.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { HomeComponent } from './components/home/home.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { HttpClientModule } from '@angular/common/http';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    HomeComponent,
    LoadingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule,
    MatToolbarModule,
    MatIconModule,
    MatFormFieldModule,
    MatCheckboxModule,
    HttpClientModule,
    MatProgressSpinnerModule,
  ],
  exports: [LoadingComponent],
  providers: [{ provide: ProfileService, useClass: HttpProfileService },
  { provide: TokenService },
  { provide: Quizservice }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
