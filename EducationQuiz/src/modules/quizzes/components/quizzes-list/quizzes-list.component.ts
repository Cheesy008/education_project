import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { QuizService } from "src/service/quiz.service";
import { Quiz } from "src/models/quiz.model";
import { PageEvent } from "@angular/material/paginator";

@Component({
  selector: "app-quizzes-list",
  templateUrl: "./quizzes-list.component.html",
  styleUrls: ["./quizzes-list.component.scss"]
})
export class QuizzesListComponent implements OnInit {
  page: number;
  quizzes: Quiz[] = [];
  pageSize = 1;
  length = 1;
  constructor(
    private route: ActivatedRoute,
    private quizService: QuizService
  ) {}
  pageEvent: PageEvent;
  ngOnInit(): void {
    this.route.params.subscribe((params: any) => {
      if (params.page) {
        this.page = params.page;
      } else {
        this.page = 1;
      }
      this.getPage(null);
    });
  }
  getPage(event?: PageEvent) {
    if (event) {
      this.page = event.pageIndex + 1;
    }
    this.quizService.getQuizzes(this.page).subscribe(data => {
      this.quizzes = [];
      this.length = data.count;
      this.pageSize = data.results.length;
      data.results.forEach(element => {
        this.quizzes.push(Quiz.parse(element));
      });
    });
  }
}
