
$(document).ready(function () {
  $(window).scroll(function () {
    if ($(document).scrollTop() > 50 && $('.navbar-toggler').is(':hidden')) {
      $('.navbar').addClass('scrolled');
    } else {
      $('.navbar').removeClass('scrolled');
    }
  });

  $('.navbar-toggler').click(function () {
    $('.navbar-collapse').toggleClass('show');
    $('.navbar').toggleClass('collapsed');
  });



});


const searchForm = document.getElementById('search-form');
const advancedSearchBtn = document.getElementById('advanced-search-btn');
const advancedSearchDropdown = document.getElementById('advanced-search-dropdown');
const categorySelect = document.getElementById('category-select');
const mecanicoSelect = document.getElementById('mecanico-select');
const buscarBtn = document.getElementById('buscar-btn');
const loginNavlink = document.querySelector('#login-navlink');
const loginDropdown = document.querySelector('#login-dropdown');

// Initialize Popper instance
const popperInstance = Popper.createPopper(advancedSearchBtn, advancedSearchDropdown, {
  placement: 'bottom',
  modifiers: [
    {
      name: 'offset',
      options: {
        offset: [0, 10],
      },
    },
  ],
});

let menuVisible = false;


// Event listener for "Advanced Search" button
advancedSearchBtn.addEventListener('click', function () {
  if (!menuVisible) {
    advancedSearchDropdown.style.display = 'block';
    popperInstance.update();
    console.log('Clicked on "Advanced Search" button');
    menuVisible = true;
  } else {
    advancedSearchDropdown.style.display = 'none';
    menuVisible = false;
  }
});



buscarBtn.addEventListener('click', function() {
  const selectedCategory = categorySelect.value;
  const selectedMecanico = mecanicoSelect.value;

  console.log(`Categoria: ${selectedCategory}`);
  console.log(`Mecanico: ${selectedMecanico}`);
});




// Crear un popper para el login
const loginPopperInstance = Popper.createPopper(loginNavlink, loginDropdown, {
  placement: 'bottom-start',
  modifiers: [
    {
      name: 'offset',
      options: {
        offset: [0, 8],
      },
    },
    {
      name: 'flip',
      options: {
        fallbackPlacements: ['top-start', 'bottom-start', 'top', 'bottom'],
      },
    },
    {
      name: 'preventOverflow',
      options: {
        boundary: 'viewport',
      },
    },
  ],
});

// Esconder el login por default
loginDropdown.classList.remove('show');

// Mostrar o no el login dando click al navlink
loginNavlink.addEventListener('click', function () {
  loginDropdown.classList.toggle('show');
  loginPopperInstance.update();
});





