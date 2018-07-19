from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuarios.form import RegistroForm
# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('almacen:almacen_lista')
