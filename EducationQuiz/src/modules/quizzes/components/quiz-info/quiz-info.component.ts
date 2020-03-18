import { Component, OnInit, Input } from '@angular/core';
import { Quiz } from 'src/models/quiz.model';

@Component({
  selector: 'app-quiz-info',
  templateUrl: './quiz-info.component.html',
  styleUrls: ['./quiz-info.component.scss']
})
export class QuizInfoComponent implements OnInit {
  @Input() quiz: Quiz;
  constructor() { }

  ngOnInit(): void {
  }

}
