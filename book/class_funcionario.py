class Funcionario:
    ##Construir Classe
    def __init__(self, nome, cpf, email, salario, endereco):
        self.nome     = nome
        self.cpf      = cpf
        self.email    = email
        self.salario  = salario
        self.endereco = endereco

    ##GETTERS
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_email(self):
        return self.email 

    def get_salario(self):
        return self.salario

    def get_endereco(self):
        return self.endereco

    ##SETTERS
    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_email(self, email):
        self.email = email

    def set_salario(self, salario):
        self.salario = salario

    def set_email(self, endereco):
        self.endereco = endereco