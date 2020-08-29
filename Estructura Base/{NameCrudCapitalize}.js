var table;
$(document).ready(function() {
    setTimeout(function() {
        toastr.options = {
            closeButton: true,
            progressBar: true,
            showMethod: 'slideDown',
            showDuration: true,
            timeOut: 3000
        };
    }, 1300);


    table = $('#{NameCrudTable}').DataTable({
        "language": {
            "url": config.routes[2].language_datatable
        },
        "processing": true,
        "serverSide": true,
        "ajax": config.routes[0].admin_list,
        "columns": [

            { DataTableColumns } { data: 'action', name: 'action', orderable: false, searchable: false },

        ],
        dom: 'Bfrtip',
        buttons: {
            buttons: [{
                    extend: 'colvisGroup',
                    text: 'Información General',
                    className: 'btn btn-outline btn-success btn-rounded btn-sm btn_parametrizacion',
                    { DataTableGeneralColumns }

                },

                {
                    extend: 'colvisGroup',
                    text: 'Auditoría',
                    className: 'btn btn-outline btn-success btn-rounded btn-sm btn_parametrizacion',
                    { DataTableAuditColumns }

                }

            ]
        }




    });


    $.ajaxSetup({
        headers: { "X-CSRF-TOKEN": $("meta[name=\"csrf-token\"]").attr("content"), }

    });


    $('#btn_edit').click(function() {

        var id = $('input:radio:checked').val();
        var form = $('#form_list');

        if (id) {
            var url = defineURL(jQuery(form).attr('action'), id);
            form.attr('action', url);
        } else {
            swal({
                title: general.advertencia_title,
                text: general.selec_registro,
                type: "warning",
                showCancelButton: false,
                confirmButtonColor: "#1e8ac2",
                confirmButtonText: general.swal_acept,
                closeOnConfirm: false,
                showLoaderOnConfirm: true,
                allowOutsideClick: false
            });
            return false;
        }
    });




    $("#btn_delete").click(function() {
        var id = $('input:radio:checked').val();

        if (id) {
            var ruta = config.routes[1].admin_delete;
            eliminar_registro(ruta, id, null, null, '{NameCrudTable}', '{NameCrud}');

        } else {
            swal({
                title: general.advertencia_title,
                text: general.selec_registro,
                type: "warning",
                showCancelButton: false,
                confirmButtonColor: "#1e8ac2",
                confirmButtonText: general.swal_acept,
                closeOnConfirm: false,
                showLoaderOnConfirm: true,
                allowOutsideClick: false
            });
            return false;
        }
    });


    $("#btn_save").click(function() {
        var jsonResponse;
        var l = Ladda.create(document.querySelector('#btn_save'));
        $.ajaxSetup({
            headers: { "X-CSRF-TOKEN": $("meta[name=\"csrf-token\"]").attr("content"), }
        });

        $.ajax({
            type: "POST",
            url: "{NameCrud}",
            data: $('#form_create').serialize(),

            beforeSend: function(data) {
                l.start();
            },
            success: function(data) {
                toastr.success('Registro almacenado', data.valor);

            },
            error: function(data) {

                jsonResponse = JSON.parse(data.responseText);
                $.map(jsonResponse.error, function(val, key) {
                    toastr.error(key, val);
                });

            },
            complete: function() {
                table.ajax.reload();
                l.stop();
            }
        });
    });

    $("#btn_refresh").click(function() {

        table.ajax.reload();

    });

});


function defineURL(url, id) {

    url = url.replace("identificador", id);
    return url;
}