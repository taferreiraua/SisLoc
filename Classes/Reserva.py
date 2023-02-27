from Classes.Operacao import Operacao

class Reserva(Operacao):
    def __init__(self, cpf: str, codigo: int):
        Operacao.__init__(self, cpf, codigo)
        self._prioridade = int()

    def set_prioridade(self, prioridade: int):
        self._prioridade = prioridade

    def get_prioridade(self):
        return self._prioridade
