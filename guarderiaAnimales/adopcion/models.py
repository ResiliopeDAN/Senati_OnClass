from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='mascotas/',null=True,blank=True)

    def __str__(self):
        return self.nombre


class Interesados(models.Model):
    idmascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="interesados")
    email = models.EmailField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
