import "package:Tappsa/Components/Buttons/ButtonComponent.dart";
import "package:Tappsa/Components/Buttons/ButtonNavigationComponent.dart";
import "package:Tappsa/Components/Header/Header.dart";
import "package:Tappsa/Components/Header/HeaderAppMain.dart";
import "package:Tappsa/Components/Menu/MenuView.dart";
import "package:Tappsa/Controllers/categoria_elementoController.dart";
import "package:Tappsa/Helpers/Helper.dart";
import "package:Tappsa/Lang/Translations.dart";
import "package:Tappsa/Models/AppointmentModel.dart";
import "package:Tappsa/Models/categoria_elementoModel.dart";
import "package:Tappsa/Models/PatientModel.dart";
import "package:Tappsa/Providers/categoria_elementoProvider.dart";
import "package:Tappsa/Views/Chat/ChatView.dart";
import "package:Tappsa/Views/Home/HomeView.dart";
import "package:dependencies/dependencies.dart";
import "package:dependencies_flutter/dependencies_flutter.dart";
import "package:flutter/material.dart";
import "package:flutter/widgets.dart";
import "package:intl/intl.dart";

class categoria_elementoView extends StatefulWidget {
  static const routeName = "/categoria_elementoView";
  @override
  categoria_elementoState createState() => categoria_elementoState(this);
}

class categoria_elementoState extends State<categoria_elementoView>
    with InjectorWidgetMixin {
  categoria_elementoController _controller;
  categoria_elementoView parientElement;
  PatientModel usuario;

  categoria_elementoState(categoria_elementoView parientElement) {
    this.parientElement = parientElement;
    this._controller = new categoria_elementoController(parientElement, this);
  }

  update() {
    setState(() {});
  }

  @override
  Widget buildWithInjector(BuildContext context, Injector injector) {
    this._controller.provider = injector.get<categoria_elementoService>();
    final categoria_elementoModel args = ModalRoute.of(context).settings.arguments;
    return Scaffold(
      body: ListView(
        children: <Widget>[
         
         
        ],
      ),
    );
  }
}
