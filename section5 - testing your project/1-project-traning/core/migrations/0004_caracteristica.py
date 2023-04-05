# Generated by Django 4.1.7 on 2023-03-27 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_funcionario_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('caracteristica', models.CharField(max_length=100, verbose_name='Serviço')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Dispositivos'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Característica',
                'verbose_name_plural': 'Características',
            },
        ),
    ]
