package fare.domain.usecases.getServicesUseCase;

import fare.core.utilities.UseCase;
import fare.core.utilities.Event;
import fare.domain.entities.ServiceEntity;

public  class GetServicesUseCaseImpl extends GetServicesUseCase {

    private final ServiceGateway serviceGateway;

    public GetServicesUseCaseImpl(ServiceGateway serviceGateway ){
        this.serviceGateway = serviceGateway;
    }

    public Event<List<Service>> call (GetServicesParam param){

        return Event.build(true, this.serviceGateway.get(), "SERVICE:GET");

    }

}

