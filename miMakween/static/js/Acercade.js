$(document).ready(function () {


    
    $(window).scroll(function () {
      if ($(document).scrollTop() > 80 ) {
        $('.texto').addClass('scroll');
      } else {
        $('.texto').removeClass('scroll');
      }
    });
  
  
  });

  //cuando el documento este listo, haz lo siguiente
  //si el documento esta a mas de 80 px scrolleado entonces
  //agrega el scroll
  //sino, quita el scroll