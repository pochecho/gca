
<?php

namespace App\Models\CategoriaElemento;

use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class CategoriaElementoModel extends Model
{
	protected $table = "categoria_elemento";
	protected $primaryKey = "id_pk";
	protected $casts = ["id_pk" => "string"];

}