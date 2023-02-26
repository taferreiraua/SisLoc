class Cliente:
    def __init__(self, cpf: str):
        self._cpf = cpf
        self._nome = str()
        self._endereco = str()

    def set_cpf(self, cpf: str):
        self._cpf = cpf

    def get_cpf(self):
        return self._cpf

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_endereco(self, endereco: str):
        self._endereco = endereco

    def get_endereco(self):
        return self._endereco

    def imprimir(self):
        print(f'Nome: {self._nome}\n'
              f'Endereço: {self._endereco}')
