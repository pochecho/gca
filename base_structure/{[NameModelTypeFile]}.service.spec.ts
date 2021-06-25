import { TestBed } from '@angular/core/testing';

import { {[NameModelTypeClass]}Service } from './{[NameModelTypeFile]}.service';

describe('{[NameModelTypeClass]}Service', () => {
  let service: {[NameModelTypeClass]}Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    // service = TestBed.inject({[NameModelTypeClass]}ApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
