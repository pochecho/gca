@extends('layouts.template')
@section('title')
{{ trans('copies.titles.{NameCrud}_nuevo') }}
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
        <li ><a href="#">{{trans('copies.breadcrumb.gestion')}}</a> </li>
        <li><a href="{{route(posfijoruta('{NameCrud}'))}}">{{trans('copies.breadcrumb.{NameCrud}')}}</a></li>
        <li class="active"><strong>{{trans('copies.breadcrumb.nueva')}}</strong></li>   
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
                                        <div  class="row" >
                        
                                        <form class="form-horizontal" id="store_{NameCrud}" method="POST" action="{{ route(posfijoRuta('store_{NameCrud}')) }}" enctype="multipart/form-data"> 
                                        {{ csrf_field() }}
                                        
                                        {NameCrudCreate}

                                        @component('layouts.return_message')    
                                            @slot('id_mensaje') message_{NameCrud} @endslot
                                        @endcomponent

                                        <div class="form-group">
                                            <div class="col-md-2 pull-right">

                                                <button id="create_{NameCrud}" type="button" class="btn btn-outline btn-success btn-rounded" data-style="zoom-in" data-toggle="tooltip" data-placement="left" title="" data-original-title="Guardar" onclick="guardar_registro('#create_{NameCrud}', 'store_{NameCrud}', posfijoRuta('{NameCrud}'), 'insertar la {NameCrud}', 'message_{NameCrud}')">{{ trans('copies.registro.guardar') }} 
                                                </button>

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








