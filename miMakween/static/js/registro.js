$(document).ready(function () {

    // Seleccionar el formulario
    const form = document.querySelector('form');
    // Escuchar el evento submit del formulario
    form.addEventListener('submit', (event) => {
        // Prevenir que se envíe el formulario automáticamente
        event.preventDefault();

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        // Obtener los valores de los campos del formulario
        const username = document.getElementById('formUser').value.trim();
        const nombre = document.getElementById('formNombre').value.trim();
        const apellido = document.getElementById('formApellido').value.trim();
        const email = document.getElementById('formEmail').value.trim();
        const contrasena = document.getElementById('formContrasena').value.trim();
        const confirmContra = document.getElementById('formConfirmContra').value.trim();

        // Validar que los campos no estén vacíos
        if (nombre === '' || apellido === '' || username === '' || email === '' || contrasena === '' || confirmContra === '') {
            Swal.fire({
                icon: 'warning',
                title: '¡Atención!',
                text: 'Debe completar todos los campos',
                confirmButtonText: 'OK'
            });
            return false;
        } else if (contrasena !== confirmContra) {
            Swal.fire({
                icon: 'error',
                title: '¡Error!',
                text: 'Las contraseñas no coinciden',
                confirmButtonText: 'OK'
            });
            return false;
        } else if (!emailRegex.test(email)) {
            Swal.fire({
                icon: 'error',
                title: '¡Error!',
                text: 'El email ingresado no es válido',
                confirmButtonText: 'OK'
            });
            return false;
        } else {
            // Si se llega hasta acá, el formulario se puede enviar
            Swal.fire({
                icon: 'success',
                title: '¡Registro exitoso!',
                text: 'Su cuenta ha sido creada satisfactoriamente',
                confirmButtonText: 'OK'
            }).then((result) => {
                // Redirigir a la página de inicio de sesión
                if (result.isConfirmed) {
                    form.submit()
                }
            });
        }

    });
});