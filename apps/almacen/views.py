from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.almacen.forms import AlmacenForm
from apps.almacen.models import Playeras
# Create your views here.



class AlmacenList(ListView):
	model = Playeras
	template_name = 'almacen/almacen_list.html'
	paginate_by = 5

class AlmacenCreate(CreateView):
	model = Playeras
	form_class = AlmacenForm
	template_name = 'almacen/almacen_form.html'
	success_url = reverse_lazy('almacen:almacen_lista')

class AlmacenUpdate(UpdateView):
	model = Playeras
	form_class = AlmacenForm
	template_name = 'almacen/almacen_form.html'
	success_url = reverse_lazy('almacen:almacen_lista')

class AlmacenDelete(DeleteView):
	model = Playeras
	template_name = 'almacen/almacen_delete.html'
	success_url = reverse_lazy('almacen:almacen_lista')

