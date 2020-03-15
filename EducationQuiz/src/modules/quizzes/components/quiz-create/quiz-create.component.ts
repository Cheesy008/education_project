import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { QuizCreate } from './../../../../models/quiz.model';
import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-quiz-create',
  templateUrl: './quiz-create.component.html',
  styleUrls: ['./quiz-create.component.scss']
})
export class QuizCreateComponent implements OnInit {
  quiz: QuizCreate;
  public createForm: FormGroup;
  constructor(private profileServie: ProfileService, private formBuilder: FormBuilder) {
    this.quiz = new QuizCreate(this.profileServie.authUser);
    this.createForm = this.formBuilder.group({
      title: new FormControl('', [Validators.required]),
      description: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {
  }

}
