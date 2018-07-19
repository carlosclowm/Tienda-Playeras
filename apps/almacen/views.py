from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.almacen.forms import AlmacenForm
from apps.almacen.models import Playeras
# Create your views here.

def listado(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['usarname', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index(request):
	return HttpResponse("almacen")

def almacen_view(request):
	if request.method == 'POST':
		form = AlmacenForm(request.POST)		
		if form.is_valid():
			form.save()
		return redirect('almacen:lista')
	else:
		form = AlmacenForm()

	return render(request, 'almacen/almacen_form.html', {'form':form})

def almacen_list(request):
	playera = Playeras.objects.all().order_by('id')
	contexto = {'almacen': playera}
	return render(request, 'almacen/almacen_list.html', contexto)

def almacen_edit(request, id_playera):
	playera = Playeras.objects.get(id=id_playera)
	if request.method == 'GET':
		form = AlmacenForm(instance=playera)
	else:
		form = AlmacenForm(request.POST, instance=playera)
		if form.is_valid():
			form.save()
			return redirect('almacen:almacen_lista')
	return render(request, 'almacen/almacen_form.html', {'form':form})

def almacen_delete(request, id_playera):
	playera = Playeras.objects.get(id=id_playera)
	if request.method == 'POST':
		playera.delete()
		return redirect('almacen:almacen_lista')
	return render(request, 'almacen/almacen_delete.html', {'playera':playera})

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

