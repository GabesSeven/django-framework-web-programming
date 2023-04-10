from django.test import TestCase

# Create your tests here.
def add_num(num):
    return num + 1

class SimplesTestCase(TestCase):

    # executa toda vez
    def setUp(self):
        print('Iniciando o Teste')
        self.numero = 41

    # testa a unidade de código
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)
