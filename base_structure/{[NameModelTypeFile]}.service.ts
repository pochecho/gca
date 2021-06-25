import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { delay } from 'rxjs/operators';
import { {[NameModelTypeClass]}Gateway } from '../../../domain/models/{[NameModelTypeFile]}/gateway/{[NameModelTypeFile]}.gateway';
import { {[NameModelTypeClass]}Mapper } from '../../mappers/{[NameModelTypeFile]}/{[NameModelTypeFile]}.mapper';
import { I{[NameModelTypeClass]}Model } from '../../../domain/models/{[NameModelTypeFile]}/{[NameModelTypeFile]}.model';
@Injectable()
export class {[NameModelTypeClass]}Service extends {[NameModelTypeClass]}Gateway {
  constructor(private http: HttpClient, private {[NameModelTypeFile]}Mapper: {[NameModelTypeClass]}Mapper) {
    super();
  }
  getById(id: string): Observable<I{[NameModelTypeClass]}Model> {
   return null;
  }
  getAll(): Observable<I{[NameModelTypeClass]}Model[]> {
    return null;
  }
  save(alb: I{[NameModelTypeClass]}Model): Observable<I{[NameModelTypeClass]}Model> {
    throw new Error('Method not implemented.');
  }
}
