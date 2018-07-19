from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.vender.models import Cliente, Solicitud
from apps.vender.forms import ClienteForm, SolicitudForm
# Create your views here.

def index(request):
	return render(request, 'almacen/index.html')

class SolicitudList(ListView):
	model = Solicitud
	template_name = 'vender/solicitud_list.html'

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'vender/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = ClienteForm
	success_url = reverse_lazy('vender:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)

		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.cliente = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Cliente
	template_name = 'vender/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = ClienteForm
	success_url = reverse_lazy('vender:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		solicitud = self.model.objects.get(id=pk)
		cliente = self.second_model.objects.get(id=solicitud.cliente_id)
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=cliente)
		context['id']=pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.cliente_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
		model = Solicitud
		template_name = 'vender/solicitud_delete.html'
		success_url = reverse_lazy('vender:solicitud_listar')
