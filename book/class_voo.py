class Voo():
    ##Construir Classe
    def __init__(self, status, aeroporto_destino, aeroporto_partida, partida_prevista, chegada_prevista):
        self.codigo_de_voo     = 0
        self.status            = status
        self.aeroporto_destino = aeroporto_destino
        self.aeroporto_partida = aeroporto_partida
        self.partida_prevista  = partida_prevista
        self.partida_real      = 0
        self.chegada_prevista  = chegada_prevista
        self.chegada_real      = 0

    ##GETTERS

    def get_codigo_de_voo(self):
        return self.codigo_de_voo

    def get_status(self):
        return self.status
        
    def get_aeroporto_destino(self):
        return self.aeroporto_destino

    def get_aeroporto_partida(self):
        return self.aeroporto_partida

    def get_partida_prevista(self):
        return self.partida_prevista

    def get_partida_real(self):
        return self.partida_real

    def get_chegada_prevista(self):
        return self.chegada_prevista

    def get_chegada_real(self):
        return self.chegada_real    

    ##SETTERS

    def set_codigo_de_voo(self, codigo_de_voo):
        self.codigo_de_voo = codigo_de_voo 

    def set_status(self, status):
        self.status = status  

    def set_aeroporto_destino(self, aeroporto_destino):
        self.aeroporto_destino = aeroporto_destino

    def set_aeroporto_partida(self, aeropoto_partida):
        self.aeroporto_partida = aeropoto_partida 

    def set_partida_prevista(self, partida_prevista):
        self.partida_prevista = partida_prevista  

    def set_partida_real(self, partida_real):
        self.partida_real = partida_real 

    def set_chegada_prevista(self, chegada_prevista):
        self.chegada_prevista = chegada_prevista

    def set_chegada_real(self, chegada_real):
        self.chegada_real = chegada_real 