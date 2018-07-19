from django.urls import path
from apps.usuarios.views import RegistroUsuario

urlpatterns = [
	 path('/registrar', RegistroUsuario.as_view(), name='Registrar'),
]

app_name = 'usuarios'