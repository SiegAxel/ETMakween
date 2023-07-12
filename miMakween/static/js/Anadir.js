$(document).ready(function () {
    $(".anadirTrabajo").click(function () {
        $("#AnadirModal").modal("show");
    });


    const form = document.querySelector('form');
    const nombre = document.getElementById("nombre");
    const textarea = document.getElementById("descripcion");
    const categoria = document.getElementById("categoria");
    const mecanico = document.getElementById("mecanico");
    const fileInput = document.getElementById("fotoForm");

    form.addEventListener('submit', (event) => {
        event.preventDefault();


        if (nombre.value.trim() === "") {
            Swal.fire("Debe ingresar un título para el trabajo.");
            return false;
        } else if (nombre.value.trim().length < 3) {
            Swal.fire("El título no puede contener menos de 3 caracteres.");
            return false;
        }
        else if (textarea.value.trim() === "") {
            Swal.fire("Debe ingresar una descripción para el trabajo.");
            return false;
        }
        else if (textarea.value.trim().length > 500) {
            Swal.fire("La descripción no puede contener más de 500 caracteres.");
            return false;
        }
        else if (categoria.value === "0") {
            Swal.fire("Debe seleccionar una categoría para el trabajo.");
            return false;

        } else {

            Swal.fire({
                icon: 'Success',
                title: 'Exito',
                text: 'Trabajo añadido con exito',
                footer: 'Recuerde esperar a la confirmacion del administrador'
            }).then((ok) => {
                if (ok.isConfirmed) {
                    form.submit();
                }
            });

        }




    });
    $("#AnadirModal").modal("hide");
});