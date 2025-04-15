"""
Configuración de URLs para el proyecto web_django.

La lista `urlpatterns` enruta URLs a vistas. Para más información, por favor consulta:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agrega una importación:  from my_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación:  from other_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra configuración de URLs
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views  # Importamos la vista index

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('hello/', include('hello.urls')),
    path('dolar/', include('dolar.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
