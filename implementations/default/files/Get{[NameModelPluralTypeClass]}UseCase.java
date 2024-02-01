package {[CompanyName]}.domain.usecases.get{[NameModelPluralTypeClass]}UseCase;

import {[CompanyName]}.core.utilities.UseCase;
import {[CompanyName]}.core.utilities.Event;
import {[CompanyName]}.domain.entities.{[NameModelTypeClass]}Entity;

public abstract class Get{[NameModelPluralTypeClass]}UseCase extends UseCase<Get{[NameModelPluralTypeClass]}Param,List<{[NameModelTypeClass]}Entity>> {

    public abstract Event<List<{[NameModelTypeClass]}Entity>> call (Get{[NameModelPluralTypeClass]}Param param);

}

