# Generated by Django 4.0.6 on 2022-08-20 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formacao',
            options={'verbose_name_plural': 'Formações'},
        ),
        migrations.AlterModelOptions(
            name='formacao_usuario',
            options={'verbose_name_plural': 'Formações de usuários'},
        ),
        migrations.AlterModelOptions(
            name='permissao',
            options={'verbose_name_plural': 'Permissões'},
        ),
        migrations.AlterModelOptions(
            name='permissao_usuario',
            options={'verbose_name_plural': 'Permissões de usuários'},
        ),
        migrations.AlterModelOptions(
            name='postagem',
            options={'verbose_name_plural': 'Postagens'},
        ),
        migrations.AlterModelOptions(
            name='tipo_usuario',
            options={'verbose_name_plural': 'Tipos de Usuários'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuários'},
        ),
    ]
