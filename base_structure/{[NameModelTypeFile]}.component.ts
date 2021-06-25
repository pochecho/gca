import { Component, OnInit, Input } from '@angular/core';
import { {[NameWidgetTypeClass]}Configuration } from '../../{[NameWidgetTypeFile]}-configuration';
@Component({
  selector: 'bcw-{[NameModelTypeFile]}[configuration]',
  templateUrl: './{[NameModelTypeFile]}.component.html',
  styleUrls: ['./{[NameModelTypeFile]}.component.scss'],
})
export class {[NameModelTypeClass]}Component implements OnInit {
  response$;
  
  @Input() configuration: {[NameWidgetTypeClass]}Configuration;

  constructor() {

  }

  ngOnInit(): void {
  }
}
