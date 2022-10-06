from django.test import TestCase

# Create your tests here.
from emprestimo_livros.models import Livro, Usuario, Emprestimo
class VooTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        companhia_area.objects.create()
        Voo.objects.create(companhia_area='TAM',aeroporto_destino='Congonhas-SP',codigo_de_voo='')
    def test_criacao_id(self):
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        self.assertEqual(livro_1.id, 1)
