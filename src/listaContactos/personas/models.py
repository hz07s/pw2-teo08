from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombres   = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=100)
    edad      = models.IntegerField(blank=True)
    donador   = models.BooleanField()

    def get_absolute_url(self):
        return reverse('personas:browsing', kwargs={'myID' : self.id})