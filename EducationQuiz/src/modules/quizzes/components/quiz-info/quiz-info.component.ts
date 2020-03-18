import { Component, OnInit, Input } from '@angular/core';
import { Quiz } from 'src/models/quiz.model';
import { ProfileService } from 'src/service/profile.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-quiz-info',
  templateUrl: './quiz-info.component.html',
  styleUrls: ['./quiz-info.component.scss']
})
export class QuizInfoComponent implements OnInit {
  @Input() quiz: Quiz;
  canEdit = false;
  constructor(private profileService: ProfileService, private router: Router) { }

  ngOnInit(): void {
    this.canEdit = this.profileService.authUser.id === this.quiz.ownerId;
  }
  view() {
    this.router.navigate(['quizzes', this.quiz.id]);
  }
  pass() {
    this.router.navigate(['quizzes', this.quiz.id, 'pass']);
  }
  edit() {
    this.router.navigate(['quizzes', this.quiz.id, 'edit']);
  }
}
