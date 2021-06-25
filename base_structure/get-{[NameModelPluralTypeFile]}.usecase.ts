import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { I{[NameModelTypeClass]}Model } from '../../models/{[NameModelTypeFile]}/{[NameModelTypeFile]}.model';
import { IBaseUsecase } from 'core';
import { {[NameModelTypeClass]}Gateway } from '../../models/{[NameModelTypeFile]}/gateway/{[NameModelTypeFile]}.gateway';
@Injectable()
export class Get{[NameModelPluralTypeClass]}UseCase implements IBaseUsecase<I{[NameModelTypeClass]}Model[]> {
  constructor(private {[NameModelTypeProperty]}GateWay: {[NameModelTypeClass]}Gateway) {}
  invoke(): Observable<I{[NameModelTypeClass]}Model[]> {
    return this.{[NameModelTypeProperty]}GateWay.getAll();
  }
}