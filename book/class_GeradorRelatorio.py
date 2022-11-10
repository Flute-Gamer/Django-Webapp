from fpdf import FPDF  # fpdf class

class GeradorRelatorio:

    def __init__(self, tipo, inicio, fim, pdf):
        self.tipo = tipo
        self.inicio = inicio
        self.fim = fim
        pdf = PDF(orientation='L', unit='mm', format='A4') #Cria arquivo PDF

    def gera_pdf():
        self.pdf.add_page()
        self.pdf.output('test.pdf','F')
        print("Gerou doc")