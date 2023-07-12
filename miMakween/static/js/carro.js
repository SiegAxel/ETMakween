var updateBtns = document.getElementsByClassName('update-carro')


for( i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var servicioId = this.dataset.servicio
        var action = this.dataset.action
        console.log('servicioId:', servicioId,'action:',action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            addCookieItem(servicioId, action)
        }else{
            updateUserOrder(servicioId,action)
        }
    })
}

function addCookieItem(servicioId, action){
    console.log('No hay usuario logueado, agregando item a cookie.')

    if (action == 'add') {
        if(cart[servicioId] == undefined){
            cart[servicioId] = {'cantidad':1}
        }else{
            cart[servicioId]['cantidad'] += 1
        }
    }

    if (action =='remove'){
        cart[servicioId]['cantidad'] -= 1

        if(cart[servicioId]['cantidad'] <=0 ){
            console.log('Servicio quitado.')
            delete cart[servicioId];
        }
    }

    console.log('Cart:', cart)
    document.cookie = 'cart' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}


function updateUserOrder(servicioId, action){
    console.log('Usuario esta logeado, enviando datos.')

    var url = '/actualizar_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'servicioId':servicioId,'action':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) =>{
        console.log('data:',data)
        location.reload()
    })
}