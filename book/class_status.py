from self import self


class Status:
    ##Construir Classe
    def __init__(proximo_status, status_atual):
        self.status_atual    = 0
        self.proximo_status  = proximo_status
        self.horario         = 0

    ##GETTERS
    def get_status_atual(self):
        return self.status_atual

    def get_proximo_status(self):
        return self.proximo_status

    def get_horario(self):
        return self.horario

    ##SETTERS
    def set_status_atual(self, status_atual):
        self.status_atual = status_atual

    def set_proximo_status(self, proximo_status):
        self.proximo_status = proximo_status

    def set_email(self, horario):
        self.horario = horario
