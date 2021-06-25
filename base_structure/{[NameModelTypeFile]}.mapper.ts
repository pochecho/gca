import { IBaseMapper } from 'core';
import { I{[NameModelTypeClass]}Model } from '../../../domain/models/{[NameModelTypeFile]}/{[NameModelTypeFile]}.model';
import { Injectable } from '@angular/core';

@Injectable()
export class {[NameModelTypeClass]}Mapper implements IBaseMapper<I{[NameModelTypeClass]}Model> {
  fromMap(obj: any): I{[NameModelTypeClass]}Model {
    return {
      {[PropertyMappers]}
    };
  }
}
