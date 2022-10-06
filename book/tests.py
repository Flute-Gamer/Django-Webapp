from django.test import TestCase
import datetime
# Create your tests here.
from book.models import Voo,Operador,Funcionario,Piloto,Status,Companhia
class VooTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Funcionario.objects.create(nome='Igor',email='igor@usp.br',salario=3,endereco='Rua de Passos')
        Piloto.objects.create(nome='Igor',email='igor@usp.br',salario=3,endereco='Rua de Passos')
        Status.objects.create(proximo_status=1,horario=datetime.date.today())
        funcionario_1 = Funcionario.objects.get(nome='Igor')
        piloto_1 = Piloto.objects.get(nome='Igor')
        Voo.objects.create(
            aeroporto_destino='Congonhas-SP',
            aeroporto_partida='Passos-MG',
            partida_prevista=datetime.date(2022,6,10),
            chegada_prevista=datetime.date(2022,6,11),
            status=1
            )
        voo_1 = Voo.objects.get(aeroporto_destino='Congonhas-SP')
        Companhia.objects.create(nome='TAM',funcionarios_id=funcionario_1,pilotos_id=piloto_1,voo_id=voo_1)
    def test_criacao_id(self):
        voo_1 = Voo.objects.get(aeroporto_destino='Congonhas-SP')
        self.assertEqual(voo_1.id, 1)
