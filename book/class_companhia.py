class Companhia:
    ##Construir Classe
    def __init__(self, nome):
        self.nome               = nome
        self.funcionarios       = []
        self.pilotos            = []
        self.voo                = 0
        self.id_companhia_aerea = 0

    ##GETTERS
    def get_nome(self):
        return self.nome

    def get_funcionarios(self):
        return self.funcionarios

    def get_pilotos(self):
        return self.pilotos

    def get_voo(self):
        return self.voo

    def get_id_companhia_aerea(self):
        return self.id_companhia_aerea

    ##SETTERS
    def set_nome(self, nome):
        self.nome = nome

    def set_funcionarios(self, funcionarios):
        self.cpf = cpf

    def set_pilotos(self, pilotos):
        self.pilotos = pilotos

    def set_voo(self, voo):
        self.voo = voo

    def set_id_companhia_aerea(self, id_companhia_aerea):
        self.id_companhia_aerea = id_companhia_aerea