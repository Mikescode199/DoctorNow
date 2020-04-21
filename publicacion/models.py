from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    etiqueta_tema = models.CharField(max_length=50)
    etiqueta_contenido = models.TextField()
    etiqueta_fuente_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.user)