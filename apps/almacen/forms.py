from django import forms
from apps.almacen.models import Playeras

class AlmacenForm(forms.ModelForm):

	class Meta:
		model = Playeras

		fields = [
		'banda',
		'genero',
		'fecha',
		'cliente',
		'tipo',
		]

		labels = {
		'banda': 'Nombre de la Banda',
		'genero': 'Genero de la Banda',
		'fecha': 'Fecha de Entrada/Almacen',
		'cliente': 'Cliente que la Adquirio',
		'tipo': 'Tipo de empaquetado',
		}

		widgets = {
		'banda': forms.TextInput(attrs={'class':'form-control'}),
		'genero': forms.TextInput(attrs={'class':'form-control'}),
		'fecha': forms.TextInput(attrs={'class':'form-control'}),
		'cliente': forms.Select(attrs={'class':'form-control'}),
		'tipo': forms.CheckboxSelectMultiple(),
		}