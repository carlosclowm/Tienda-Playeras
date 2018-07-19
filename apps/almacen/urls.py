from django.urls import path
from apps.almacen.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', index, name='index'),
    path('/nuevo', login_required(AlmacenCreate.as_view()), name='almacen_crear'),
    path('/lista', login_required(AlmacenList.as_view()), name='almacen_lista'),
    path('/editar/<int:pk>/', login_required(AlmacenUpdate.as_view()), name='almacen_editar'),
    path('/eliminar/<int:pk>/', login_required(AlmacenDelete.as_view()), name='almacen_eliminar'),
    path('/listado', listado, name='listado'),
    ]
app_name = 'almacen'