@extends('layouts.template')
@section('title')
{{ trans('copies.titles.{NameCrud}_edit') }}
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

@endsection
@section('hist_navegacion')
<ol class="breadcrumb">
    <li><a href="#">{{trans('copies.breadcrumb.gestion')}}</a> </li>
    <li><a href="{{route(posfijoruta('{NameCrud}'))}}">{{trans('copies.breadcrumb.{NameCrud}')}}</a></li>
    <li class="active"><strong>{{trans('copies.breadcrumb.editar')}}</strong></li>
</ol>
@endsection
@section('content')

<div class="wrapper wrapper-content animated fadeInRight">
    <div class="row">
        <div class="col-lg-12">
            <div class="ibox float-e-margins">
                <div class="tabs-container">
                    <div class="panel-body">
                        <div class="wrapper wrapper-content animated fadeInRight">
                            <div class="row">
                                <div class="col-md-12">
                                    <div>
                                        <div class="row">
                                            {!!Form::model(
                                            ${NameCrud},[
                                            'id'=>'update_{NameCrud}',
                                            'method'=>'PUT',
                                            'route'=>[posfijoRuta('update_{NameCrud}'),${NameCrud}->id_pk],
                                            'action'=>[posfijoRuta('update_{NameCrud}'),${NameCrud}->id_pk],
                                            'enctype'=>'multipart/form-data'])!!}
                                            {{ csrf_field() }}

                                            {NameCrudEdit}


                                            @component('layouts.return_message')
                                            @slot('id_mensaje') message_{NameCrud} @endslot
                                            @endcomponent



                                            <div class="form-group">
                                                <div class="col-md-2 pull-right">
                                                    <button id="edit_{NameCrud}" type="button" class="btn btn-outline btn-success btn-rounded" data-style="zoom-in" data-toggle="tooltip" data-placement="left" title="" data-original-title="Guardar" onclick="guardar_registro('#edit_{NameCrud}', 'update_{NameCrud}', posfijoRuta('{NameCrud}'), 'actualizar la {NameCrud}', 'message_{NameCrud}')">{{ trans('copies.registro.guardar') }} </button>
                                                </div>

                                            </div>

                                            {!!Form::close()!!}

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>



@endsection