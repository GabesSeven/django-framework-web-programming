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
	list_display = ('montadora', 'modelo', 'chassi', 'get_motoristas')

	def get_motoristas(self, obj):
		return ', '.join([m.username for m in obj.motoristas.all()])

	get_motoristas.short_description = 'Motoristas'