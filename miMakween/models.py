from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your models here.



class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='userprofile', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='foto', null=True, blank=True, default='foto/adult-school.png')
    is_mecanico = models.BooleanField(default=False)

    USERNAME_FIELD = 'user'
   
    def get_nombre(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    @property
    def get_id(self):
        return self.user.pk
    def get_username(self):
        return self.user.username
    def get_status(self):
        if self.is_mecanico:
            return "Mecánico"
        else:
            return "Cliente"
    def __str__(self):
        return self.user.username+" / "+self.get_status()
    class Meta:
        verbose_name_plural = 'Usuarios'
    

class Servicio(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='foto',null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url = self.foto.url
        except:
            url = ''
        return url
    

class Orden(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_orden= models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False, null=True, blank=True)
    transaccion_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_total_carro(self):
        itemorden = self.itemorden_set.all()
        total = sum([item.get_total for item in itemorden])
        return total
    @property
    def get_items_carro(self):
        itemorden = self.itemorden_set.all()
        total = sum([item.cantidad for item in itemorden])
        return total

class ItemOrden(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_add= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.cantidad * self.servicio.precio
        return total



class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='foto',null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=0, null=True)  # Agregado el campo de precio
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Categorias'
        
    ## perdon bb , te veo el lunes 
class Trabajos(models.Model):
    idTrabajo= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=45)
    descripcion= models.TextField()
    foto=models.ImageField(upload_to='foto',null=True,default='foto/CarExample.png')
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='--')
    mecanico= models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    categoria= models.ForeignKey(Categoria,related_name='categorias',on_delete=models.CASCADE)

    def get_status(self):
        if self.publicar:
            return "Publicado"
        else:
            return "No publicado"

    def __str__(self):
        return self.titulo+" - Categoria: "+self.categoria.nombre+" - Estado: "+self.get_status()
    
    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

class Galeria(models.Model):
    idFoto=models.AutoField(primary_key=True)
    foto= models.ImageField(upload_to='Galeria',null=True)
    trabajo= models.ForeignKey(Trabajos,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.idFoto)+" "+(self.trabajo.titulo)
    

class formulario_contacto(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    telefono = models.CharField(max_length=45)
    mensaje = models.TextField(max_length=250)
    def __str__(self):
        return self.nombre+" "+self.apellido+" - Email: "+self.email
    