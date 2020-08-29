
<?php

namespace App\Models\Formulario;

use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class FormularioModel extends Model
{
	protected $table = "formulario";
	protected $primaryKey = "id_pk";
	protected $casts = ["id_pk" => "string"];

}



class formularioModel extends BaseModel{
  {ModelDB}

  formularioModel();


  Map<String, dynamic> toMap() {
    var map = new Map<String, dynamic>();
    {ToMap}

    return map;
  }

  void map(dynamic obj) {
    {Map}
  }
}