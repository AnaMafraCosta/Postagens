from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Categoria
from .form import CategoriaForm
from .models import Postagem
from .form import PostagemForm
# Create your views here.


def lista_categ(request):
    categorias = Categoria.objects.all()
    pacote = {"categoria_chave": categorias}
    return render(request, "lista_categ.html", pacote)


def create_categ(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listacateg")

    pacote = {"form_categoria": form}
    return render(request, "create_categ.html", pacote)


def atualizar_categ(request, id_categoria):
    categoria = Categoria.objects.get(pk=id_categoria)

    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect("listacateg")

    pacote = {"form_categoria": form}
    return render(request, "create_categ.html", pacote)


def lista_post(request):
    postagens = Postagem.objects.all()
    pacote = {"postagem_chave": postagens}
    return render(request, "lista_post.html", pacote)


def create_post(request):
    form = PostagemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listapost")

    pacote = {"form_postagem": form}
    return render(request, "create_post.html", pacote)


def atualizar_post(request, id_postagem):
    postagem = Postagem.objects.get(pk=id_postagem)

    form = PostagemForm(request.POST or None, instance=postagem)
    if form.is_valid():
        form.save()
        return redirect("listapost")

    pacote = {"form_postagem": form}
    return render(request, "create_post.html", pacote)
