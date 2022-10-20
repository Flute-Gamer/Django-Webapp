class Operador:
    ##Construir Classe
    def __init__(self, nome, cpf, email):
        self.nome  = nome
        self.cpf   = cpf
        self.email = email


    ##GETTERS
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_email(self):
        return self.email 

    ##SETTERS
    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_email(self, email):
        self.email = email