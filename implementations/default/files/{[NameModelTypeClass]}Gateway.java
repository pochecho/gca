package {[CompanyName]}.domain.gateway;


import {[CompanyName]}.domain.entities.{[NameModelLowerCamelCase]}Entity.{[NameModelTypeClass]}Entity;

import java.util.List;

public interface {[NameModelTypeClass]}Gateway {

    {[NameModelTypeClass]}Entity update({[NameModelTypeClass]}Entity {[NameModelLowerCamelCase]}Entity);
    {[NameModelTypeClass]}Entity save({[NameModelTypeClass]}Entity {[NameModelLowerCamelCase]}Entity);
    void delete(String id);
    List<{[NameModelTypeClass]}Entity> get();
}
