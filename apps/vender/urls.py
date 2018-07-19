from django.urls import path
from apps.vender.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', index),
    path('/listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    path('/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    path('/editar/<int:pk>', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    path('/eliminar/<int:pk>', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]

app_name = 'vender'