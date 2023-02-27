from Classes.Operacao import Operacao
from Classes.Reserva import Reserva
from Classes.Locacao import Locacao


class RepositorioOperacao:
    def __init__(self):
        self._operacoes = list()

    def cadastrar(self, operacao: Operacao):
        operacao.set_ativo(True)
        self._operacoes.append(operacao)
        print('Operação cadastrada com sucesso!')

    def buscarReservas(self, cpf: str):
        reservas = list()
        for CadOperacao in self._operacoes:
            if isinstance(CadOperacao, Reserva):
                if CadOperacao.get_cpf() == cpf and CadOperacao.is_ativo() is True:
                    reservas.append(CadOperacao)
        if reservas:
            return reservas

    def buscarLocacoes(self, cpf: str):
        locacoes = list()
        for CadOperacao in self._operacoes:
            if isinstance(CadOperacao, Locacao):
                if CadOperacao.get_cpf() == cpf and CadOperacao.is_ativo() is True:
                    locacoes.append(CadOperacao)
        if locacoes:
            return locacoes

    def deletarLocacao(self, cpf: str, codigo: int):
        LocEncontrada = False
        for operacao in self._operacoes:
            if isinstance(operacao, Locacao):
                if operacao.get_cpf() == cpf and operacao.get_cod() == codigo:
                    LocEncontrada = True
                    if operacao.is_ativo() is True:
                        operacao.set_ativo(False)
                        print('Locação inativada!')
                    else:
                        print('Locação já está inativa!')
        if LocEncontrada is False:
            print('Locação não encontrada.')

    def deletarReserva(self, cpf: str, codigo: int):
        ResEncontrada = False
        for operacao in self._operacoes:
            if isinstance(operacao, Reserva):
                if operacao.get_cpf() == cpf and operacao.get_cod() == codigo:
                    ResEncontrada = True
                    if operacao.is_ativo() is True:
                        operacao.set_ativo(False)
                        print('Reserva encerrada!')
        if ResEncontrada is False:
            print('Reserva não encontrada.')

    def listarLocacoes(self, cpf: str):
        operacoes_cliente = list()
        for operacao in self._operacoes:
            if isinstance(operacao, Locacao) and operacao.get_cpf() == cpf:
                operacoes_cliente.append(operacao)
        if operacoes_cliente:
            return operacoes_cliente

    def NumLocCliente(self, cpf: str):
        count = 0
        for operacao in self._operacoes:
            if isinstance(operacao, Locacao) and operacao.get_cpf() == cpf:
                count += 1
        return count

    def NumLocFilme(self, codigo: int):
        count = 0
        for operacao in self._operacoes:
            if isinstance(operacao, Locacao) and operacao.get_cod() == codigo:
                count += 1
        return count

    def NumLocAtivoCliente(self, cpf: str):
        loc = self.buscarLocacoes(cpf)
        return len(loc)

    def NumLocAtivoFilme(self, codigo: int):
        count = 0
        for operacao in self._operacoes:
            if isinstance(operacao, Locacao):
                if operacao.get_cod() == codigo and operacao.is_ativo() is True:
                    count += 1
        return count

    def NumResAtivoFilme(self, codigo: int):
        count = 0
        for operacao in self._operacoes:
            if isinstance(operacao, Reserva):
                if operacao.get_cod() == codigo and operacao.is_ativo() is True:
                    count += 1
        return count