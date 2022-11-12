from fpdf import FPDF  # fpdf class

class GeradorRelatorio:
    
    debug = True
    title = 'Relatório Administrativo de '


    def __init__(self, tipo, inicio, fim):
        self.tipo = tipo #tipo é um boolean (0 para Partidas e 1 para Chegadas)
        self.inicio = inicio #inicio e fim sao datetimes na forma AAAA/MM/DD-HH:MM:SS
        self.fim = fim
        if(self.tipo):
            self.title += 'Partidas'
        else:
            self.title += 'Chegadas'

    def gera_pdf(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4') #Cria arquivo PDF
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.set_xy(0,0)
        pdf.cell(40, 10, 'Olá Mundo', 0, 1)
        pdf.ln(40)
        pdf.cell(210 - pdf.get_string_width(self.title)/2, 10, self.title, 0, 1, 'C')
        pdf.set_title('Relatório Administrativo do Aeroporto de Vira-Canecos')
        pdf.set_author('Sistema de Monitoração de Voos')
        pdf.output('test.pdf','F')
        if (self.debug):
            self.debug_log



    def debug_log():
        print('---------------------------------------------------------------------------')
        print('                    Gerador de Relatorio Debug LOG                         ')
        print(str(self) + ' Gerou doc')
        print('')
        print('')
        print('---------------------------------------------------------------------------')