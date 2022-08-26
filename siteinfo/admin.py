from django.contrib import admin
from siteinfo.models import Categoria, Permissao, Tipo_usuario, Formacao, Usuario, Postagem, Permissao_usuario, Formacao_usuario
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Permissao)
admin.site.register(Tipo_usuario)
admin.site.register(Formacao)
admin.site.register(Usuario)
admin.site.register(Postagem)
admin.site.register(Permissao_usuario)
admin.site.register(Formacao_usuario)
