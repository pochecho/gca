package {[CompanyName]}.domain.usecases.get{[NameModelPluralTypeClass]}UseCase;

import {[CompanyName]}.core.utilities.UseCase;
import {[CompanyName]}.core.utilities.Event;
import {[CompanyName]}.domain.entities.{[NameModelTypeClass]}Entity;

public  class Get{[NameModelPluralTypeClass]}UseCaseImpl extends Get{[NameModelPluralTypeClass]}UseCase {

    private final {[NameModelTypeClass]}Gateway {[NameModelLowerCamelCase]}Gateway;

    public Get{[NameModelPluralTypeClass]}UseCaseImpl({[NameModelTypeClass]}Gateway {[NameModelLowerCamelCase]}Gateway ){
        this.{[NameModelLowerCamelCase]}Gateway = {[NameModelLowerCamelCase]}Gateway;
    }

    public Event<List<{[NameModelTypeClass]}>> call (Get{[NameModelPluralTypeClass]}Param param){

        return Event.build(true, this.{[NameModelLowerCamelCase]}Gateway.get(), "{[NameModelUpperSnakecase]}:GET");

    }

}

