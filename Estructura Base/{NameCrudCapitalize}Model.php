<?php

namespace App\Models\{Folder};

use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class {NameCrudCapitalize}Model extends Model
{
	
    public $timestamps=false;
	protected $table = '{NameDB}';
	protected $primaryKey = '{AttributeID}';
	protected $casts = ['{AttributeID}' => 'string'];

}