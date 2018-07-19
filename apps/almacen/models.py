from django.db import models
from apps.vender.models import Cliente
# Create your models here.

class Empaquetado(models.Model):
	tipo = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.tipo)

class Playeras(models.Model):
	banda = models.CharField(max_length=100)
	genero = models.CharField(max_length=50)
	fecha = models.DateField()
	cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	tipo = models.ManyToManyField(Empaquetado)

	def __str__(self):
		return '{}'.format(self.banda)