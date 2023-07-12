class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self,servicio):
        id = str(servicio.nombre)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "servicio_id": servicio.nombre,
                "precio": servicio.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"]+=1
            self.carrito[id]["acumulado"]+=servicio.precio
        self.actualizar()
    
    def actualizar(self):
        self.session["carrito"]=self.carrito
        self.session.modified = True

    def resta(self,servicio):
        id = str(servicio.nombre)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["precio"]-=servicio.precio
            if self.carrito[id]["cantidad"]==0:
                self.eliminar(servicio)
            self.actualizar()

    def eliminar(self,servicio):
        id = str(servicio.nombre)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.actualizar()
    
    def vaciar(self):
        self.session["carrito"]={}
        self.session.modified = True