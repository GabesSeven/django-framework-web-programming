from django.db import models

# Create your models here.
class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Montadora(models.Model):
    """OneToOneField
     - cada carro só pode ter um montadora
     - cada montadora pode ter muitos carros
    """
    nome = models.CharField('Nome', max_length=50, help_text='Máximo 50 caracteres')

    class Meta():
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

class Carro(models.Model):
    """ForeignKey (One to Many)
     - cada carro só pode ter um chassi
     - cada chassi só pode ter um carro
    """
    chassi  = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    mont  = models.ForeignKey('Montadora', on_delete=models.CASCADE)
    modelo  = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco  = models.DecimalField('Preco', max_length=8, max_digits=2, decimal_places=2)

    class Meta():
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'
