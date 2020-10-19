from django.urls import path

from django.views.generic import TemplateView

from .views import *

app_name = 'blog'


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('', listar_publicaciones, name='listar_publicaciones'),
    path('<uuid:pub>/', ver_publicacion, name='ver_publicacion'),
    path('categoria/<int:categoria/', ver_publicaciones_categoria, name='ver_publicaciones_categoria')
]