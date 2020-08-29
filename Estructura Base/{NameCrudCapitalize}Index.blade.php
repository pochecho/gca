@extends('layouts.template')
@section('title')
{{ trans('copies.titles.{NameCrud}') }}
@endsection
@section('icono_menu_activo')
{{Config::get('constants.ICONO_MENU_ACTIVO')}}
@endsection

@section('nombre_menu_activo')
{{Config::get('constants.NOMBRE_MENU_ACTIVO')}}
@endsection

@section('barra-menu')
{{Config::get('constants.BARRA_MENU_ACTIVO')}}
@endsection
@section('head')

<style type="text/css">
    /* esta clase permite que los radio button tengan la apariencia de un checkbox*/
    input[type="radio"] {
        -webkit-appearance: checkbox;
        /* Chrome, Safari, Opera */
        -moz-appearance: checkbox;
        /* Firefox */
        -ms-appearance: checkbox;
        /* IExplorer */
    }
</style>

@endsection
@section('hist_navegacion')
<ol class="breadcrumb">
    <li><a href="#">{{trans('copies.breadcrumb.gestion')}}</a> </li>
    <li class="active"><strong>{{trans('copies.breadcrumb.{NameCrud}')}}</strong></li>
</ol>
@endsection

@section('icon-ayuda')
<i class="icon-ayuda icono-ayuda pointer" data-toggle="modal" data-target="#ayuda_{NameCrud}"></i>
@endsection
@section('content')

<div class="col-md-12">
    @component('layouts.component.mensaje_informativo')
    @slot('mensaje') {{ trans('copies.mensajes_informativos.{NameCrud}') }} @endslot
    @endcomponent
</div>

<div class="wrapper wrapper-content animated fadeInRight">
    <div class="row">
        <div class="col-lg-12">
            <div class="ibox float-e-margins">

                {!!Form::open(['id'=>'form_list', 'method'=>'POST', 'route'=>[posfijoRuta('admin_{NameCrud}_edit'),'identificador']])!!}
                {{ csrf_field() }}

                <div class="ibox-title">
                    <h5>{{trans('copies.{NameCrud}.{NameCrud}')}}</h5>

                    <div class="ibox-tools">

                        <!-- Botón de Guardar -->
                        <a href="{{trans('copies.{NameCrud}.new')}}">
                            <button type="button" class="btn btn-outline btn-success btn-sm btn_parametrizacion icon-agregar p-t-xxs p-b-xxs">
                                <label class="sin_negrita  fuente-letra no-padding">
                                    {{ trans('copies.parametrizacion.nuevo') }}
                                </label>
                            </button>
                        </a>



                        <!-- Botón de actualizar -->
                        {{ Form::button('', ['type'=>'submit','class' => 'btn btn-outline btn-success  btn-sm  icon-editar btn_parametrizacion','id'=>'btn_edit'] )  }}

                        <!-- Botón de eliminar -->
                        {!!Form::button('',['class'=>'btn btn-outline btn-success btn-sm icon-eliminar_1 btn_parametrizacion','data-style'=>'zoom-in', 'id'=>'btn_delete'])!!}

                        <!-- Botón de refrescar -->
                        {{ Form::button('', ['class' => 'btn btn-outline btn-success  btn-sm  icon-actualizar btn_parametrizacion','id'=>'btn_refresh'])}}

                    </div>
                </div>
                <div id="respuesta" class="ibox-content">
                    <div class="table-responsive">
                        <table class="table table-striped  order-column" id="{NameCrudTable}" style="width:100%">
                            <thead>
                                <tr>

                                    {DataTableModelCrud}
                                    <th>
                                        Acción
                                    </th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                </div>
                {!!Form::close()!!}
            </div>
        </div>
    </div>
</div>


<!-- LAYOUT PARA MOSTRAR LAS AYUDAS -->
@component('layouts.component.modal_ayuda')
@slot('id_modal') ayuda_{NameCrud} @endslot
@slot('icono') icon-{NameCrud} @endslot
@slot('texto_titulo') {{trans('copies.breadcrumb.{NameCrud}')}} @endslot
@slot('mensaje') {{trans('copies.ayudas.{NameCrud}')}} @endslot
@slot('background') background_ayuda_{NameCrud} @endslot
@slot('tipo') imagen @endslot

@endcomponent
@endsection


@section('codigo_scripts')

<script>
    // configuración global de rutas del registro
    var config = {
        routes: [
            //listar {NameCrud}  'route'=>['admin_{NameCrud}_editar','identificador']
            {
                admin_list: "{{route(posfijoRuta('admin_list_{NameCrud}'))}}"
            },
            //eliminar {NameCrud}
            {
                admin_delete: "{{posfijoRuta('delete_{NameCrud}')}}"
            },
            //dataTable language
            {
                language_datatable: "{{asset('././theme_inspinia/js/dataTable-midis.json')}}"
            },

        ]
    };
</script>

<script src="{{asset('/js/{NameCrud}/{NameCrudCapitalize}.js')}}"></script>


@endsection