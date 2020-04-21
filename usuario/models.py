from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    usuario_nombre = models.CharField(max_length=30)
    usuario_apellido_paterno = models.CharField(max_length=30)
    usuario_apellido_materno = models.CharField(max_length=30)
    usuario_ocupacion = models.CharField(max_length=30)
    usuario_correo = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user)

