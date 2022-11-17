from fpdf import FPDF  # fpdf class
import datetime
from book.models import Voo #importando os modelos de classses de BD

class GeradorRelatorio:
    
    debug = True
    title = 'Relatório Administrativo de '
    registros = []
    texto = 'tipo_relatorio=partida'
    def __init__(self, tipo, inicio, fim):
        self.tipo = tipo
        self.inicio = inicio #inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS
        self.fim = fim
        
        if(self.tipo == self.texto):
            voar = Voo.objects.filter(partida_prevista__range=[inicio, fim])
            self.title += 'Partidas'
        else:
            voar = Voo.objects.filter(chegada_prevista__range=[inicio, fim])
            self.title += 'Chegadas'

        self.registros.clear()
        for i in voar.iterator():
            self.registros.append(i)
        # self.registros.append(voar)
        #Ok, esse é o resultado esperado:
        #"       Relatório Administrativo de Chegadas
        #Congonhas-SP                               None
        #Congonhas-SP                               None"
        #Não importa quantas vezes vc atualize o relatório
        
    def gera_pdf(self):
        campoID = 20
        altura = 8
        campoData = 35
        campoAeroporto = 210-campoID-2*campoData-20

        nome = str('Relatorio'+'.pdf')
        
        pdf = FPDF(orientation='P', unit='mm', format='A4') #Cria arquivo PDF
        pdf.add_page() # Configs inicias e página
        pdf.set_font('Arial', '', 8)

        pdf.set_xy(0,3) # Cabeçalho
        pdf.cell(210, 4, 'Você pode atualizar a página para atualizar este relatório', 0, 1, 'C')
        pdf.set_xy(0,0)
        pdf.set_font('Arial', 'B', 16)
        pdf.set_xy(0,0)
        pdf.ln(20)
        pdf.set_x(0)
        pdf.cell(210, 15, self.title, 0, 1, 'C')

        pdf.set_font('Arial', '', 12) #Texto de Corpo
        pdf.cell(campoID, 2*altura, '', 1, 1, 'C')
        pdf.ln(-2*altura)
        pdf.cell(campoID, altura, 'Código', 0, 1, 'C')
        pdf.cell(campoID, altura, 'de Voo', 0, 1, 'C')
        pdf.ln(-2*altura)
        pdf.set_x(campoID+10)
        pdf.cell(campoAeroporto, 2*altura, 'Aeroporto de Partida', 1, 1, 'C')
        pdf.ln(-2*altura)
        pdf.set_x(campoID+campoAeroporto+10)
        
        if(self.tipo == self.texto):
            pdf.cell(2*campoData, altura, 'Partida', 1, 1, 'C')
        else:
            pdf.cell(2*campoData, altura, 'Chegada', 1, 1, 'C')
            
        pdf.set_x(campoAeroporto+campoID+10)
        pdf.cell(campoData, altura, 'Prevista', 1, 1, 'C')
        pdf.ln(-altura)
        pdf.set_x(campoID +campoAeroporto +campoData +10)
        pdf.cell(campoData, altura, 'Real', 1, 1, 'C')
        for voo in self.registros:
            
            pdf.cell(campoID, altura, str(voo.codigo_de_voo), 1, 1, 'C')   
            pdf.ln(-altura)
            pdf.set_x(10+campoID)

            if (self.tipo == self.texto):
                pdf.cell(campoAeroporto, altura, voo.aeroporto_partida, 1, 1, 'C')
                pdf.ln(-altura)
                pdf.set_x(campoAeroporto+campoID+10)
                pdf.cell(campoData, altura, str((voo.partida_prevista).strftime('%Y/%m/%d-%H:%M')), 1, 1, 'C')
            else:
                pdf.cell(campoAeroporto, altura, voo.aeroporto_destino, 1, 1, 'C')
                pdf.ln(-altura)
                pdf.set_x(campoAeroporto+campoID+10)
                pdf.cell(campoData, altura, str((voo.chegada_prevista).strftime('%Y/%m/%d-%H:%M')), 1, 1, 'C')

        #Assinatura, título, autor e etc. 
        pdf.ln(10)
        pdf.set_x(0)
        pdf.cell(210, 4, 'Relatório realizado em '+datetime.datetime.now().strftime('%Y/%m/%d-%H:%M:%S'), 0, 1, 'C') #TODO:Atualizar para GMT-3
        pdf.set_title('Relatório Administrativo do Aeroporto de Vira-Canecos')
        pdf.set_author('Sistema de Monitoração de Voos')
        pdf.output(name=nome, dest='F').encode('latin-1')
        pdf.close()
        
        if (self.debug):
            self.debug_log(len(self.registros))   
        return str(nome)

    def debug_log(self, x):
        print('---------------------------------------------------------------------------')
        print('                    Gerador de Relatorio Debug LOG                         ')
        print(str(self) + ' Gerou doc')
        print('Tipo: '+self.tipo)
        print('Voos encontrados: ' +str(x))
        print('')
        print('---------------------------------------------------------------------------')
