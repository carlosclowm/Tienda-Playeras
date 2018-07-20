from django.urls import path
from apps.almacen.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('/nuevo', login_required(AlmacenCreate.as_view()), name='almacen_crear'),
    path('/lista', login_required(AlmacenList.as_view()), name='almacen_lista'),
    path('/editar/<int:pk>/', login_required(AlmacenUpdate.as_view()), name='almacen_editar'),
    path('/eliminar/<int:pk>/', login_required(AlmacenDelete.as_view()), name='almacen_eliminar'),
    ]
app_name = 'almacen'