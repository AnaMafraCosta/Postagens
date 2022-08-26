from django.db import models

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria


class Permissao(models.Model):
    permissao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Permissões"

    def __str__(self):
        return self.permissao


class Tipo_usuario(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Usuários"

    def __str__(self):
        return self.tipo


class Formacao(models.Model):
    formacao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.formacao


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    tipo_usuario = models.ForeignKey(
        Tipo_usuario, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome


class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateField(auto_now=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default=None, null=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo


class Permissao_usuario(models.Model):
    unique_together = (('Permissao', 'Usuario'))

    class Meta:
        verbose_name_plural = "Permissões de usuários"


class Formacao_usuario(models.Model):
    unique_together = (('Formacao', 'Usuario'))

    class Meta:
        verbose_name_plural = "Formações de usuários"
