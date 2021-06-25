import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ViewModelsModule } from '../view-models/view-models.module';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    ViewModelsModule,
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  exports: [],
})
export class PagesModule { }
