from fpdf import FPDF  # fpdf class
import datetime
from book import models #importando os modelos de classses de BD

class GeradorRelatorio:
    
    debug = True
    title = 'Relatório Administrativo de '
    registros = []
    def __init__(self, tipo, inicio, fim):
        self.tipo = tipo #tipo é um boolean (0 para Partidas e 1 para Chegadas)
        self.inicio = inicio #inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS
        self.fim = fim
        if(self.tipo):
            self.title += 'Partidas'
        else:
            self.title += 'Chegadas'


        #Teste hardcoded     
        voar = models.Voo(codigo_de_voo=1,
            aeroporto_destino='Congonhas-SP',
            aeroporto_partida='Passos-MG',
            partida_prevista=datetime.date(2022,6,10),
            chegada_prevista=datetime.date(2022,6,11),
            status=1)
        self.registros.clear()
        self.registros.append(voar)
        self.registros.append(voar)
        #Ok, esse é o resultado esperado:
        #"       Relatório Administrativo de Chegadas
        #Congonhas-SP                               None
        #Congonhas-SP                               None"
        #Não importa quantas vezes vc atualize o relatório
        
        
    def gera_pdf(self):
        nome = str('Relatorio'+'.pdf')
        
        pdf = FPDF(orientation='P', unit='mm', format='A4') #Cria arquivo PDF
        pdf.add_page() # Configs inicias e página
        pdf.set_font('Arial', '', 8)

        pdf.set_xy(0,3) # Cabeçalho
        pdf.cell(210, 4, 'Você pode atualizar esta página para atualizar o relatório', 0, 1, 'C')
        pdf.set_xy(0,0)
        pdf.set_font('Arial', 'B', 16)
        pdf.set_xy(0,0)
        pdf.ln(20)
        pdf.cell(210, 10, self.title, 0, 1, 'C')

        pdf.set_font('Arial', '', 12) #Texto de Corpo
        for voo in self.registros:
            pdf.set_x(12.7)         
            pdf.cell(210-30-12.7, 8, voo.aeroporto_destino, 0, 1, 'L')
            pdf.ln(-8)
            pdf.set_x(180)
            pdf.cell(30, 8, str(voo.chegada_real), 0, 1, 'L')
            if (pdf.get_y()) >= 297-25: #Anti-Transbordo
                pdf.add_page()
        pdf.set_xy(0, 270)
        pdf.cell(210, 4, 'Relatório realizado em '+datetime.datetime.now().strftime('%Y/%m/%d-%H:%M:%S'), 0, 1, 'C')
        #Assinatura, título, autor e etc. 
        pdf.set_title('Relatório Administrativo do Aeroporto de Vira-Canecos')
        pdf.set_author('Sistema de Monitoração de Voos')
        pdf.output(name=nome, dest='F').encode('latin-1')
        pdf.close()
        
        if (self.debug):
            self.debug_log
            
        return str(nome)

    def debug_log():
        print('---------------------------------------------------------------------------')
        print('                    Gerador de Relatorio Debug LOG                         ')
        print(str(self) + ' Gerou doc')
        print('')
        print('')
        print('---------------------------------------------------------------------------')
