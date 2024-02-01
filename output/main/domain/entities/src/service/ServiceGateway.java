package fare.domain.gateway;


import fare.domain.entities.serviceEntity.ServiceEntity;

import java.util.List;

public interface ServiceGateway {

    ServiceEntity update(ServiceEntity serviceEntity);
    ServiceEntity save(ServiceEntity serviceEntity);
    void delete(String id);
    List<ServiceEntity> get();
}
