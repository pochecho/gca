<?php

namespace App\Http\Controllers\{Folder};

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\{Folder}\{NameCrudCapitalize}Model;
use Illuminate\Support\Facades\Schema;
use Yajra\Datatables\Facades\Datatables;
use Carbon\Carbon;
use Response;
use DB;
use Auth;
use Crypt;


use App\User;

use Illuminate\Support\Facades\Config;

use Illuminate\Support\Facades\Validator;

class {NameCrudCapitalize}Controller extends Controller
{

    /**
     *--------------------------------------------
     * Hace el llamado a la vista del listado de {NameCrud}
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
    */
    public function index(Request $request)
    {
        cargar_datos_menu_activo(Config::get('constants.PK_SUB_MODULO_{NameCrudUpper}')); // permite cargar barra superior
        //encabezados param nombre relación en DB
        if (isset($request->ins_fk)) {
            $ins_fk = $request->ins_fk;
        } else {
            $ins_fk = Auth::user()->ins_fk;
        }
        return view('{Folder}.{NameCrudCapitalize}Index')->with(["id_institucion" => $ins_fk]);
    }

    /**
     *--------------------------------------------
     * Hace el llamado a la vista de creación de {NameCrud}
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
    */
    public function create(Request $request)
    {
        if (isset($request->ins_fk)) {
            $ins_fk = $request->ins_fk;
        } else {
            $ins_fk = Auth::user()->ins_fk;
        }
       
        
        cargar_datos_menu_activo(Config::get('constants.PK_SUB_MODULO_{NameCrudUpper}')); // permite cargar barra superior
        return view('{Folder}.{NameCrudCapitalize}Create');
    }

    


    /**
     *--------------------------------------------
     * Permite cargar todos los recursos necesarios para cargar el formulario de editar
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
     */
    public function edit($id)
    {
        cargar_datos_menu_activo(Config::get('constants.PK_SUB_MODULO_{NameCrudUpper}'));
        $id_{NameCrud}  = Crypt::decrypt($id);
        if (isset($request->ins_fk)) {
            $ins_fk = $request->ins_fk;
        } else {
            $ins_fk = Auth::user()->ins_fk;
        }
        ${NameCrud} = {NameCrudCapitalize}Model::where('id_pk', $id_{NameCrud})->findOrFail($id_{NameCrud});
        if (${NameCrud}) {
            return view('{Folder}.{NameCrudCapitalize}Edit', compact('{NameCrud}'));
        } else {
            throw new \Exception();
        }
    }

    /**
     *--------------------------------------------
     * Almacena una {NameCrud} en tabla principal y en tablas relacionadas.
     *--------------------------------------------
     * @author GCA-Midis
     * @param  \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response->json
     *          success:true - en éxito, success: false - en fallo
     *--------------------------------------------
     */
    public function store(Request $request)
    {
        $rules = [
            {RulesValidator}
        ];
        $validator = Validator::make(
            $request->all(),
            $rules
        );
        if ($validator->fails()) {
            return response()->json(array('errors' => $validator->messages()), 200);
        } else {
            DB::beginTransaction();
            try {
                if (isset($request->login_pk)) {
                    $login_pk = $request->login_pk; // recupera la llave primaria por parametro
                } else {
                    $login_pk = Auth::user()->login_pk; // recupera la llave primaria de la tabla profesional
                }

                ${NameCrud} = new {NameCrudCapitalize}Model();

                {CrudBodyDB}
                
                
                ${NameCrud}->user_create = $login_pk;
                ${NameCrud}->created_at =  formatearFechas("");

                if (${NameCrud}->save()) {
                    DB::commit();
                    return response()->json(array('success' => true), 200);
                } else {
                    DB::rollback();
                    return response()->json(array('success' => false), 200);
                }
            } catch (\Exception $e) {

                DB::rollback();
                return Response::json(array('success' => false), 200);
            }
        }
    }

    /**
     *--------------------------------------------
     * Actualizar los datos de una {NameCrud}
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
     */
    public function update($id_pk, Request $request)
    {


        $rules = [
            {RulesValidator}
        ];
     
        
        $validator = Validator::make(
            $request->all(), 
            $rules
        );
        if ($validator->fails()) {
            return response()->json(array('errors' => $validator->messages()), 200);
        } else {
            DB::beginTransaction();
            try {
              
                if (isset($request->login_pk)) {
                    $login_pk = $request->login_pk; // recupera la llave primaria por parametro
                } else {
                    $login_pk = Auth::user()->login_pk; // recupera la llave primaria de la tabla profesional
                }
                ${NameCrud} = {NameCrudCapitalize}Model::find($id_pk);

              
                {CrudBodyDB}
              
                
                ${NameCrud}->user_update = $login_pk;
                ${NameCrud}->updated_at = formatearFechas("");

                if (${NameCrud}->save()) {
                    DB::commit();
                    return response()->json(array('success' => true), 200);
                } else {
                    DB::rollback();
                    return response()->json(array('success' => false), 200);
                }
            } catch (\Exception $e) {

                DB::rollback();
                return Response::json(array('success' => false), 200);
            }
        }
    }


    /**
     *--------------------------------------------
     * Gestiona la información de las {NameCrud} para cargar en Datatables
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
    */
    public function get{NameCrudCapitalize}()
    {
        ${NameCrud} = {NameCrudCapitalize}Model::select(
           {Attributes}
        );
        return Datatables::of(${NameCrud})
            ->editColumn('id_pk', function (${NameCrud}) { })
            {EditColumnDataTable}
            ->addColumn('action', function (${NameCrud}) {
                $id_{NameCrud} = Crypt::encrypt(${NameCrud}->id_pk);
                return '<div class=""><input  type="radio" id="action" name="{NameCrud}checkboxname" value="' . $id_{NameCrud} . '""><label></label></div>';
            })
            ->rawColumns(['action'])
            ->make(true);
    }


   
    /**
     *--------------------------------------------
     * Elimina el cargo pasado por $request.
     *--------------------------------------------
     * @author GCA-Midis
     *--------------------------------------------
     */
    public function eliminar{NameCrudCapitalize}(Request $request)
    {

        DB::beginTransaction();
        try {

            $flag = true;
            if (is_numeric($request->id)) {
                ${NameCrud}_delete = $request->id;
            } else {
                ${NameCrud}_delete  = Crypt::decrypt($request->id);
            }

            $user_session = Auth::user()->login_pk;
            $fecha_actual = formatearFechas("");

            ${NameCrud} = {NameCrudCapitalize}Model::find(${NameCrud}_delete);
            ${NameCrud}->user_update = $user_session;
            ${NameCrud}->updated_at  = $fecha_actual;

            ${NameCrud}->user_delete = $user_session;
            ${NameCrud}->deleted_at  = $fecha_actual;

            if (${NameCrud}->save()) {
                $flag = true;
            } else {
                $flag = false;
            }

            if ($flag) {
                DB::commit();
                return Response()->json(array("success" => true), 200);
            } else {
                DB::rollback();
                return Response()->json(array("success" => false), 200);
            }
        } catch (\Exception $e) {

            DB::rollback();
            return Response::json(array("success" => false), 200);
        }
    }
}
