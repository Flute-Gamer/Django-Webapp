from fpdf import FPDF  # fpdf class

class GeradorRelatorio:

    def __init__(self, tipo, inicio, fim):
        self.tipo = tipo
        self.inicio = inicio
        self.fim = fim

    def gera_pdf(self):
        pdf = FPDF(orientation='L', unit='mm', format='A4') #Cria arquivo PDF
        pdf.add_page()
        pdf.output('test.pdf','F')
        print("Gerou doc")