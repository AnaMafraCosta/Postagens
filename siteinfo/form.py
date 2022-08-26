from .models import Categoria
from .models import Postagem
from django.forms import ModelForm


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria"]


class PostagemForm(ModelForm):
    class Meta:
        model = Postagem
        fields = ["titulo", "subtitulo", "texto", "categoria", "usuario"]
