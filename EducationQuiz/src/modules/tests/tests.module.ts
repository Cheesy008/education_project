import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TestsListComponent } from './components/tests-list/tests-list.component';
import { TestInfoComponent } from './components/test-info/test-info.component';
import { TestDetailsComponent } from './components/test-details/test-details.component';
import { TestCreateComponent } from './components/test-create/test-create.component';



@NgModule({
  declarations: [TestsListComponent, TestInfoComponent, TestDetailsComponent, TestCreateComponent],
  imports: [
    CommonModule
  ]
})
export class TestsModule { }
