import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { {[NameModelTypeClass]}Component } from './ui/view-models/{[NameModelTypeFile]}/{[NameModelTypeFile]}.component';
import { {[NameModelTypeClass]}Service } from './infrastructure/driven-adapter/{[NameModelTypeFile]}/{[NameModelTypeFile]}.service';
import { HttpClientModule } from '@angular/common/http';
import { {[NameModelTypeClass]}Gateway } from './domain/models/{[NameModelTypeFile]}/gateway/{[NameModelTypeFile]}.gateway';
import { {[NameModelTypeClass]}Mapper } from './infrastructure/mappers/{[NameModelTypeFile]}/{[NameModelTypeFile]}.mapper';


@NgModule({
  declarations: [{[NameModelTypeClass]}Component],
  entryComponents: [],
  imports: [CommonModule, HttpClientModule],
  exports: [{[NameModelTypeClass]}Component],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  providers: [
    {[NameModelTypeClass]}Mapper,
    {
      provide: {[NameModelTypeClass]}Gateway,
      useClass: {[NameModelTypeClass]}Service,
    },
  ],
})
export class LayoutWidgetModule {}
