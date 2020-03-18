import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { QuizCreate } from './../../../../models/quiz.model';
import { ProfileService } from 'src/service/profile.service';
import { Component, OnInit } from '@angular/core';
import { QuizService } from 'src/service/quiz.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-quiz-create',
  templateUrl: './quiz-create.component.html',
  styleUrls: ['./quiz-create.component.scss']
})
export class QuizCreateComponent implements OnInit {
  quiz: QuizCreate;
  public createForm: FormGroup;
  constructor(private router: Router,
    private profileServie: ProfileService,
    private formBuilder: FormBuilder,
    private quizService: QuizService) {
    this.quiz = new QuizCreate();
    this.createForm = this.formBuilder.group({
      title: new FormControl('', [Validators.required]),
      description: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {
  }
  create() {
    this.quiz.description = this.createForm.value.description;
    this.quiz.title = this.createForm.value.title;
    this.quizService.createQuiz(this.quiz).subscribe((data) => {
      this.router.navigate(['/quizzes/', data.id]);
    });
  }
}
