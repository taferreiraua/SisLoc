from datetime import date


class Operacao:
    def __init__(self, cpf: str, codigo: int):
        self._cpf = cpf
        self._codigo = codigo
        self._data = date.today().strftime("%d/%m/%Y")
        self._ativo = bool()

    def set_data(self, data: date):
        self._data = data.strftime("%d/%m/%Y")

    def get_data(self):
        return self._data

    def set_cpf(self, cpf: int):
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf

    def set_cod(self, cod: int):
        self._codigo = cod

    def get_cod(self):
        return self._codigo

    def set_ativo(self, ativo: bool):
        self._ativo = ativo

    def is_ativo(self):
        return self._ativo
