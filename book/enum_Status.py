from enum import Enum
#para importar use from "from enum_Status import enum_Status"
# escrevendo "enum_Status(2)" deve retornar "Programado"
# escrever o nome retorna o numero
#Tratar como objeto
class enum_Status (Enum):
    Embarcando = 1
    Programado = 2 
    Taxiando = 3
    Pronto = 4 
    Autorizado = 5 
    Em_Voo = 6 
    Aterrissado = 7
    Cancelado = 8
    Arquivado = 9