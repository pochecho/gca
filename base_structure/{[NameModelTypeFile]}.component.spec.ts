import { ComponentFixture, TestBed } from '@angular/core/testing';

import { {[NameModelTypeClass]}CardComponent } from './{[NameModelTypeFile]}.component';

describe('{[NameModelTypeClass]}CardComponent', () => {
  let component: {[NameModelTypeClass]}CardComponent;
  let fixture: ComponentFixture<{[NameModelTypeClass]}CardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ {[NameModelTypeClass]}CardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent({[NameModelTypeClass]}CardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
