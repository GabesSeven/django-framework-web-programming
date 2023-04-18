from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Chassi(models.Model):
	numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

	class Meta:
		verbose_name = 'Chassi'
		verbose_name_plural = 'Chassis'

	def __str__(self):
		return self.numero

class Montadora(models.Model):
	nome = models.CharField('Nome', max_length=50)

	class Meta:
		verbose_name = 'Montadora'
		verbose_name_plural = 'Montadoras'

	def __str__(self):
		return self.nome


# retorna uma tupla: (Object, Boolean)
# Boolean: True se Object NÃO existe; False se Object já existe
def set_default_montadora():
	return Montadora.objects.get_or_create(nome='Padrão')[0] 

class Carro(models.Model):
	"""
	OneToOneField:
	 - Carro possui um Chassi
	 - Chassi possui um Carro
	"""
	"""
	ForeignKey:
	 - Carro possui uma Montadora
	 - Montadora possui vários Carros
	"""
	"""
	ManyToManyField:
	 - Motoristas possui vários Carros
	 - Carros possui vários Motoristas 
	"""
	chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
	montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
	# se Montadora atual for excluída, seta para os referenciados a Montadora com pk=1
	# montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)
	# se Montadora atual for excluída, seta para os referenciados a Montadora "Padrão"
	# montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
	motoristas = models.ManyToManyField(get_user_model())
	modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
	preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name = 'Carro'
		verbose_name_plural = 'Carros'

	def __str__(self):
		return f'{self.montadora} {self.modelo}'