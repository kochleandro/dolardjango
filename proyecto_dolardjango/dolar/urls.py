from django.urls import path
from . import views

urlpatterns = [
    path('', views.subir_excel, name='subir_excel'),
    
]