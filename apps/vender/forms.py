from django import forms

from apps.vender.models import Cliente, Solicitud

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields =[
		'nombre',
		'telefono',
		'email',
		]

		labels = {
		'nombre': 'Nombre',
		'telefono': 'Telefono',
		'email': 'Correo',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'telefono': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),
		}

class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud

		fields =[
		'numero_playera',
		'razones',
		]

		labels = {
		'numero_playera': 'Numero de Playeras',
		'razones': 'Razon de compra',
		}

		widgets = {
		'numero_playera': forms.TextInput(attrs={'class':'form-control'}),
		'razones': forms.TextInput(attrs={'class':'form-control'}),
		}