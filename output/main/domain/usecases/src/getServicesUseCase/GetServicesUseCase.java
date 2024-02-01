package fare.domain.usecases.getServicesUseCase;

import fare.core.utilities.UseCase;
import fare.core.utilities.Event;
import fare.domain.entities.ServiceEntity;

public abstract class GetServicesUseCase extends UseCase<GetServicesParam,List<ServiceEntity>> {

    public abstract Event<List<ServiceEntity>> call (GetServicesParam param);

}

