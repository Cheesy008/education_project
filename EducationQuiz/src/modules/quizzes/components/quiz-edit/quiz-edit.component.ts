import { AnswerEdit } from './../../../../models/answer.model';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators, FormArray } from '@angular/forms';
import { QuizEdit } from 'src/models/quiz.model';
import { QuestionEdit } from 'src/models/question.model';
import { Router, ActivatedRoute } from '@angular/router';
import { QuizService } from 'src/service/quiz.service';

@Component({
  selector: 'app-quiz-edit',
  templateUrl: './quiz-edit.component.html',
  styleUrls: ['./quiz-edit.component.scss']
})
export class QuizEditComponent implements OnInit {
  editForm: FormGroup;
  questionForm: FormGroup;
  quiz: QuizEdit = new QuizEdit();
  index = 0;
  hasNext = true;
  addNext = false;
  hasPrev = false;
  constructor(formBuilder: FormBuilder, private route: ActivatedRoute, private quizService: QuizService) {
    this.questionForm = new FormGroup({
      question_title: new FormControl('', [Validators.required]),
      answers: new FormArray([])
    });
    this.editForm = new FormGroup({
      title: new FormControl('', [Validators.required]),
      description: new FormControl('', [Validators.required]),
      question: this.questionForm
    });
    // this.quiz.questions.push(new QuestionEdit());
    // this.setQuestion();
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params.id;
      this.quizService.getQuiz(id).subscribe((data) => {
        this.quiz = data;
        console.log(this.quiz);
        let index = 0;
        this.quiz.questions.forEach((e) => {
          e.index = index;
          index++;
        });
        this.setQuiz();
        if (this.quiz.questions.length === 0) {
          this.quiz.questions.push(new QuestionEdit());
        }
        this.setQuestion();
      });
    });
  }
  submit() {

  }
  nextQuestion() {
    if (!this.editForm.valid) {
      return;
    }
    this.getQuestion();
    this.index++;
    this.setQuestion();
  }
  previousQuestion() {
    if (!this.editForm.valid) {
      return;
    }
    this.getQuestion();
    this.index--;
    this.setQuestion();
  }
  addQuestion() {
    if (!this.editForm.valid) {
      return;
    }
    this.getQuestion();
    this.quiz.questions.push(new QuestionEdit());
    this.index++;

    this.setQuestion();
  }
  setQuiz() {
    this.editForm.controls.title.setValue(this.quiz.title);
    this.editForm.controls.description.setValue(this.quiz.description);
  }
  getQuestion() {
    console.log('index:' + this.index);
    const q = this.quiz.questions[this.index];
    q.question_title = this.questionForm.controls.question_title.value;

    (this.questionForm.controls.answers as FormArray).controls.forEach(element => {
      const a = new AnswerEdit();
      a.index = (element as FormGroup).controls.index.value;
      a.id = (element as FormGroup).controls.id.value;
      a.answer_text = (element as FormGroup).controls.answer_text.value;
      a.is_correct = (element as FormGroup).controls.id.value;
      if (q.answers.find(x => (x.id != -1 && x.id === a.id) || x.index === a.index)) {
        console.log('set');
        const i = q.answers.indexOf(q.answers.find(x => x.id === a.id && x.index === a.index));
        q.answers[i] = a;
      } else {
        console.log('push');
        q.answers.push(a);
      }
    });
    this.quiz.questions[this.index] = q;
    console.log(this.quiz);
    (this.questionForm.controls.answers as FormArray).clear();
  }
  setQuestion() {

    if (this.index <= 0) {
      this.hasPrev = false;
    } else {
      this.hasPrev = true;
    }
    if (this.index + 1 >= this.quiz.questions.length) {
      this.hasNext = false;
      this.addNext = true;
    } else {
      this.hasNext = true;
      this.addNext = false;
    }
    const question = this.quiz.questions[this.index];
    this.questionForm.controls.question_title.setValue(question.question_title);
    const answersForm = (this.questionForm.controls.answers as FormArray);
    answersForm.clear();
    console.log(question.answers);
    question.answers.forEach(element => {
      answersForm.push(new FormGroup({
        index: new FormControl(element.index),
        id: new FormControl(element.id),
        answer_text: new FormControl(element.answer_text, [Validators.required]),
        is_correct: new FormControl(element.is_correct ? 'checked' : '', [Validators.required])
      }));
    });
  }
  addAnswer() {

    const index = (this.questionForm.controls.answers as FormArray).length != 0 ?
      Math.max.apply(Math, (this.questionForm.controls.answers as FormArray).controls.map((o) => (o as FormGroup).controls.index.value)) + 1
      : 1;
    console.log(index);
    (this.questionForm.controls.answers as FormArray).push(new FormGroup({
      index: new FormControl(index),
      id: new FormControl('-1'),
      answer_text: new FormControl('', [Validators.required]),
      is_correct: new FormControl('', [Validators.required])
    }));
  }
}
