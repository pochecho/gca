package fare.infrastructure.repository.service;

import fare.core.utilities.ModelMapper;
import fare.domain.entities.ServiceEntity;
import fare.gateway.ServiceGateway;
import fare.repository.repository.ServiceRepository;
import java.util.List;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@AllArgsConstructor
@Service
public class ServiceAdapter implements ServiceGateway {

  private final ModelMapper modelMapper;
  private final ServiceRepository channelRepository;

  @Override
  public ServiceEntity getServiceById(String id) {
    try {
      var response = this.channelRepository.findById(id);
      if (response.isPresent()) {
        return this.modelMapper.map(
          response.get(),
          ServiceEntity.class
        );
      }
      return null;
    } catch (Exception e) {
      throw e;
    }
  }
}
