from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=10)
	email = models.EmailField()

	def __str__(self):
		return '{}'.format(self.nombre)

class Solicitud(models.Model):
	cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	numero_playera = models.IntegerField()
	razones = models.TextField()