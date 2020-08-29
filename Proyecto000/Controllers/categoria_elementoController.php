import "package:flutter/material.dart";
import "package:Tappsa/Models/categoria_elementoModel.dart";
import "package:Tappsa/Providers/categoria_elementoProvider.dart";
import "package:Tappsa/Controllers/BaseController.dart";

class categoria_elementoController extends BaseController{
  var _context;
  var _view;


  categoria_elementoController(Widget view,State state) : super(view) {
    this.state = state;
    this.model = new categoria_elementoModel();
  }

}
