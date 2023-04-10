from django.contrib import admin
from .models import Chassi, Carro, Montadora

# Register your models here.
@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    lis_display = ('modelo', 'chassi', 'preco')
