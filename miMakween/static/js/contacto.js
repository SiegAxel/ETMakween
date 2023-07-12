$(document).ready(function () {


    var email = $("#formEmail").val();
    var nombre = $("#formNombre").val();
    var apellido = $("#formApellido").val();
    var telefono = $("#formTelefono").val();

    const form = document.querySelector('form');
    const email = document.getElementById('formEmail');
    const nombre = document.getElementById('formNombre');
    const apellido = document.getElementById('formApellido');
    const telefono = document.getElementById('formTelefono');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            Swal.fire({
                icon: 'error',
                title: '¡Error!',
                text: 'El email ingresado no es válido',
                confirmButtonText: 'OK'
            });
            return;
        }

        if (email == "" || nombre == "" || apellido == "" || telefono == "") {
            Swal.fire({
                icon: 'error',
                title: 'Campos vacíos',
                text: 'Por favor complete todos los campos'
            });
            return;
        } else if (nombre.length < 3 || apellido.length < 3) {
            Swal.fire({
                icon: 'error',
                title: 'Error en el formulario',
                text: 'El nombre y el apellido deben tener al menos 3 caracteres',
            });
            return;
        } else if (telefono.match(/^\d+$/) == null) {
            Swal.fire({
                icon: 'error',
                title: 'Error en el formulario',
                text: 'El teléfono debe contener solo números',
            });
            return;
        }
        else {
            Swal.fire({
                icon: 'success',
                title: 'Formulario enviado con éxito!',
            });
            formEmail = '';
            formNombre = '';
            formApellido = '';
            formTelefono = '';
            $("#formEmail").val(formEmail);
            $("#formNombre").val(formNombre);
            $("#formApellido").val(formApellido);
            $("#formTelefono").val(formTelefono);

        }
    });
});
