$(document).ready(function () {


    function generatePassword() {
        const passwordInput = document.querySelector('#password');
        const randomPassword = Math.random().toString(36).slice(-8);
        passwordInput.value = randomPassword;
    }

    const modal = document.querySelector('.modal-dialog');
    const openModalButtons = document.querySelectorAll('[data-modal-target]');
    const closeModalButton = document.querySelector('.modal-close');
    const overlay = document.querySelector('.modal-overlay');

    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modalTarget = button.getAttribute('data-modal-target');
            openModal(modalTarget);
        });
    });

    overlay.addEventListener('click', () => {
        const modals = document.querySelectorAll('.modal.active');
        modals.forEach(modal => {
            closeModal(modal);
        });
    });

    closeModalButton.addEventListener('click', () => {
        const modals = document.querySelectorAll('.modal.active');
        modals.forEach(modal => {
            closeModal(modal);
        });
    });

    function openModal(modalTarget) {
        const modal = document.querySelector(modalTarget);
        modal.classList.add('active');
        overlay.classList.add('active');
    }

    function closeModal(modal) {
        modal.classList.remove('active');
        overlay.classList.remove('active');
    }

    function validarForm() {
        var nombre = document.getElementById("nombre").value;
        var apellidos = document.getElementById("apellidos").value;
        var email = document.getElementById("email").value;
        var categoria = document.getElementById("categoria").value;
        var password = document.getElementById("password").value;

        if (nombre.length < 3 || nombre.length > 30) {
            Swal.fire("El nombre debe tener entre 3 y 30 caracteres.");
            return false;
        }

        else if (apellidos.length < 3 || apellidos.length > 30) {
            Swal.fire("Los apellidos deben tener entre 3 y 30 caracteres.");
            return false;
        }

        else if (email.length < 5 || email.length > 20) {
            Swal.fire("El email debe tener entre 5 y 20 caracteres.");
            return false;
        }

        else if (categoria == 1) {
            Swal.fire("Por favor seleccione una categoría.");
            return false;
        } else {
            Swal.fire({
                icon: 'Success',
                title: 'Exito',
                text: 'Mecánico añadido con exito',
                footer: 'Recuerde entregarle su contraseña al trabajador'
            })
        }


        // If all fields pass validation, submit form
        document.getElementById("AnadirModal").submit();
    }



    const generateButton = document.querySelector('#generate-button');
    generateButton.addEventListener('click', generatePassword);

    const form = document.querySelector('#register-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(form);
        const name = formData.get('name');
        const lastName = formData.get('lastName');
        const email = formData.get('email');
        const category = formData.get('category');
        const password = formData.get('password');
        const profileImage = formData.get('profileImage');

        closeModal(modal);
    });


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


    // Agregar evento click a cada icono con clase 'las la-user-slash'
    $('.las.la-user-slash').each(function () {
        $(this).on('click', function () {
            Swal.fire({
                title: '¿Estás seguro de eliminar este usuario?',
                text: "Esta acción no se puede deshacer",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Si el usuario confirma la eliminación, realizar la acción
                    // Aquí se puede agregar el código para eliminar al usuario
                    Swal.fire(
                        'Eliminado',
                        'El usuario ha sido eliminado.',
                        'success'
                    )
                }
            })
        });
    });

});