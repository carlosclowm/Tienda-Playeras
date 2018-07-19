from django.urls import path
from apps.navegacion.views import index


urlpatterns = [
    path('', index, name="Inicio"),

    ]
app_name = 'navegacion'