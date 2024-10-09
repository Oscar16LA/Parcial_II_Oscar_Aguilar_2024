from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz que llama a la vista index
]
