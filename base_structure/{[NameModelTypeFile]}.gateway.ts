import { Observable } from 'rxjs';
import { I{[NameModelTypeClass]}Model } from '../{[NameModelTypeFile]}.model';

export abstract class {[NameModelTypeClass]}Gateway {
  abstract getById({[MainPropertyDefinition]}): Observable<I{[NameModelTypeClass]}Model>;
  abstract getAll(): Observable<I{[NameModelTypeClass]}Model[]>;
  abstract save(alb: I{[NameModelTypeClass]}Model): Observable<I{[NameModelTypeClass]}Model>;
}
