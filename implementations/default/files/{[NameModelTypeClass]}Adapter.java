package {[CompanyName]}.infrastructure.repository.{[NameModelLowerCamelCase]};

import {[CompanyName]}.core.utilities.ModelMapper;
import {[CompanyName]}.domain.entities.{[NameModelTypeClass]}Entity;
import {[CompanyName]}.gateway.{[NameModelTypeClass]}Gateway;
import {[CompanyName]}.repository.repository.{[NameModelTypeClass]}Repository;
import java.util.List;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@AllArgsConstructor
@Service
public class {[NameModelTypeClass]}Adapter implements {[NameModelTypeClass]}Gateway {

  private final ModelMapper modelMapper;
  private final {[NameModelTypeClass]}Repository channelRepository;

  @Override
  public {[NameModelTypeClass]}Entity get{[NameModelTypeClass]}ById(String id) {
    try {
      var response = this.channelRepository.findById(id);
      if (response.isPresent()) {
        return this.modelMapper.map(
          response.get(),
          {[NameModelTypeClass]}Entity.class
        );
      }
      return null;
    } catch (Exception e) {
      throw e;
    }
  }
}
