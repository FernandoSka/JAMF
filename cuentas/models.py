from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuarios(models.Model):
    """docstring for telefono."""

    id_persona = models.OneToOneField(User, related_name='id_persona')
    tel = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="img/img_usr", null=True, blank=True)
    usr2 = models.ManyToManyField('self')

    def get_image(self):

        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True


class Dispositivos(models.Model):
    """docstring for telefono."""
    fecha = models.CharField(max_length=30)


class Alarma(models.Model):
    """docstring for Alarma"""
    owner = models.ForeignKey(Dispositivos, null=True, blank=True)
    hora = models.CharField(max_length=30)
    image = models.ImageField(upload_to="img/img_usr", null=True, blank=True)
    def get_image(self):

        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
        