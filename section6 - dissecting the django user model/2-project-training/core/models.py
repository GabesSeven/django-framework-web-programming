from django.db import models

# Modo 1 - usuário padrão
# from django.contrib.auth.models import User

# Modo 2 - usuário customizado
# from django.conf import settings

# Modo 3 - modulo do Django oficial
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    # Modo 1 - usuário padrão
    # autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    
    # Modo 2 - usuário customizado
    # autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    
    # Modo 3 - modulo do Django oficial
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)

    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
