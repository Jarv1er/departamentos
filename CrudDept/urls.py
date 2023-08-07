from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insertar/', views.insertar, name='insertar'),
    path('editar/', views.editar, name='editar'),
    path('eliminar/', views.eliminar, name='eliminar'),
]