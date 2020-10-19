from django.shortcuts import render

from .models import *


def listar_publicaciones(request):
    news = Publicacion.objects.all()
    return render(request, './post/index.html', {'news':news} )


def ver_publicacion(request, pub):
    publicacion = Publicacion.objects.get(id = pub)
    return render(request, './ver.html', {'pub':publicacion})


def ver_publicaciones_categoria(request, categoria):
    categoria = Categoria.objects.get(id = id(categoria))
    return render(request,'./post/index.html.html', {'categoria':categoria})

