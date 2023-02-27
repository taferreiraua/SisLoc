from Classes.Operacao import Operacao


class Locacao(Operacao):
    def __init__(self, cpf: str, codigo: int):
        Operacao.__init__(self, cpf, codigo)
        self._periodo = int()

    def set_periodo(self, periodo):
        self._periodo = periodo

    def get_periodo(self):
        return self._periodo
