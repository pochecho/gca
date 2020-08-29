import "package:Tappsa/Models/categoria_elementoModel.dart";
import "package:Tappsa/Providers/Provider.dart";
import "package:dependencies/dependencies.dart";
import "Injection/Service.dart";

abstract class categoria_elementoService implements Service<categoria_elementoModel> {}

class categoria_elementoProvider extends Provider<categoria_elementoModel>
    implements categoria_elementoService {
  @override
  categoria_elementoModel toModel(Map map) => categoria_elementoModel.map(map);

  categoria_elementoProvider(Injector injector) : super(injector, "categoria_elementos") {}

  
}
