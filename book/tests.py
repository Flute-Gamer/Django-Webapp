from django.test import TestCase
import datetime
# Create your tests here.
from book.models import Voo,Operador,Funcionario,Piloto,Status,Companhia
class VooTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Funcionario.objects.create(nome='Igor',email='igor@usp.br',salario=300,endereco='Rua de Passos')
        Piloto.objects.create(nome='Augusto',email='augusto@usp.br',salario=250,endereco='Rua de Fora de Passos')
        Status.objects.create(status_atual=1,proximo_status=2,horario=datetime.date.today())
        funcionario_1 = Funcionario.objects.get(nome='Igor')
        piloto_1 = Piloto.objects.get(nome='Augusto')
        Voo.objects.create(
            codigo_de_voo=1,
            aeroporto_destino='Congonhas-SP',
            aeroporto_partida='Passos-MG',
            partida_prevista=datetime.date(2022,6,10),
            chegada_prevista=datetime.date(2022,6,11),
            status=1
            )
        voo_1 = Voo.objects.get(codigo_de_voo=1)
        Companhia.objects.create(nome='TAM',funcionarios=funcionario_1,pilotos=piloto_1,voo=voo_1)
    def test_criacao_id(self):
        voo_1 = Voo.objects.get(aeroporto_destino='Congonhas-SP')
        self.assertEqual(voo_1.codigo_de_voo, 1)
