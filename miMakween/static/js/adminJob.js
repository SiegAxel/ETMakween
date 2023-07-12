$(document).ready(function () {

    function activateLink(link) {
        // remove "active" class from all links
        const links = document.querySelectorAll('.sidebar-menu a');
        links.forEach(link => {
            link.classList.remove('active');
        });

        // add "active" class to current link
        link.classList.add('active');
    }

    // get all the links in the sidebar
    const links = document.querySelectorAll('.sidebar-menu a');

    // add event listener to each link
    links.forEach(link => {
        link.addEventListener('mouseenter', () => {
            activateLink(link);
        });
    });



    var table = $('#tbtrabajos').DataTable({
        columnDefs: [
            {
                targets: -1, // last column (actions)
                render: function (data, type, row, meta) {
                    return '<button class="btn-editar">Modificar</button>' +
                        '<button class="btn-eliminar">Eliminar</button>';
                }
            }],

        "language": {
            "decimal": "",
            "emptyTable": "No hay datos disponibles en la tabla",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ entradas",
            "infoEmpty": "Mostrando 0 a 0 de 0 entradas",
            "infoFiltered": "(filtrado de _MAX_ entradas totales)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "No se encontraron registros coincidentes",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": Activar para ordenar la columna en orden ascendente",
                "sortDescending": ": Activar para ordenar la columna en orden descendente"
            }
        },



        paging: true, // enable pagination
        lengthChange: false, // hide the "show X entries" dropdown
        pageLength: 10, // set the number of rows per page to 5
        searching: true, // hide the search box
        ordering: true, // enable sorting
        info: true // hide the "Showing X to Y of Z entries" text
    });
    $('#trabajos-card h1').text(table.page.info().recordsTotal);


    // "Eliminar"
    $('#trabajos tbody').on('click', '.btn-eliminar', function () {
        var row = $(this).closest('tr');
        var data = table.row(row).data();
        // accion de eliminar abajo
        row.remove().draw();
    });

    // "Modificar"
    $('#trabajos tbody').on('click', '.btn-editar', function () {
        var row = $(this).closest('tr');
        var data = table.row(row).data();
        // accion de modificar abajo de esto.
    });


    var modificarButtons = document.querySelectorAll(".btn-editar");
    modificarButtons.forEach(function (modificarButton) {
        modificarButton.addEventListener("click", function () {
            // Show the modal with id "AnadirModal"
            $("#AnadirModal").modal("show");
        });
    });

    var eliminarButtons = document.querySelectorAll(".btn-eliminar");
    eliminarButtons.forEach(function (eliminarButton) {
        eliminarButton.addEventListener("click", function () {
            Swal.fire({
                title: "¿Está seguro?",
                text: "¡No podrá recuperar este registro!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, estoy seguro!',
                dangerMode: true,
            })
                .then((result) => {
                    if (result.isConfirmed) {

                        Swal.fire("¡El registro ha sido eliminado!", {
                            icon: "success",
                        });
                    }
                });
        });
    });



});