<?php
Route::resource('{NameCrud}','{Folder}\{NameCrudCapitalize}Controller');

// Ruta para listar las {NameCrud}: GCA - Midis
Route::get('{NameCrud}',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@index','as'=>'{NameCrud}'.$posfijo]);

// Ruta para recuperar los datos de las {NameCrud}: GCA - Midis
Route::get('api/{NameCrud}',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@get{NameCrudCapitalize}','as'=>'admin_list_{NameCrud}'.$posfijo]);

// Ruta para generar la edición de las {NameCrud}: GCA - Midis
Route::post('{NameCrud}/{id}/edit',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@edit','as'=>'admin_{NameCrud}_edit'.$posfijo]);

// Ruta para actualizar las {NameCrud}: GCA - Midis
Route::put('edit_{NameCrud}/{id}',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@update','as'=>'update_{NameCrud}'.$posfijo]);

// Ruta para eliminar las {NameCrud}: GCA - Midis
Route::post('{NameCrud}/eliminar',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@eliminar{NameCrudCapitalize}', 'as'=>'delete{NameCrudCapitalize}'.$posfijo]);

// Ruta para generar la creación de las {NameCrud}: GCA - Midis
Route::get('{NameCrud}_create',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@create','as'=>'create_{NameCrud}'.$posfijo]);

// Ruta para crear las {NameCrud}: GCA - Midis
Route::post('store_{NameCrud}',['uses'=>'{Folder}\{NameCrudCapitalize}Controller@store','as'=>'store_{NameCrud}'.$posfijo]);