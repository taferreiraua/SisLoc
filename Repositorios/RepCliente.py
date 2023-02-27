from Classes.Cliente import Cliente


class RepositorioCliente:
    def __init__(self):
        self._clientes = list()

    def cadastrar(self, cliente: Cliente):
        # Checando se o cpf já foi cadastrado:
        jaCadastrado = False
        for cadCliente in self._clientes:
            if cadCliente.get_cpf() == cliente.get_cpf():
                jaCadastrado = True
        # Se não foi, o cliente é cadastrado. Caso contrario, informamos.
        if JaCadastrado is False:
            self._clientes.append(cliente)
        else:
            print('CPF já cadastrado.')

    def buscar(self, cpf):
        achou = False
        for cadCliente in self._clientes:
            if cadCliente.get_cpf() == cpf:
                achou = True
                return cadCliente
        if achou is False:
            print('Cliente não encontrado.')

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.get_cpf())
        if cliente:
            cliente.set_nome(cliente.get_nome())
            cliente.set_endereco(cliente.get_endereco())
            print('Cliente atualizado com sucesso!')

    def deletar(self, cpf: str):
        cliente = self.buscar(cpf)
        if cliente:
            self._clientes.remove(cliente)
            print('Cliente deletado com sucesso!')

    def listar(self):
        try:
            return self._clientes
        except TypeError:
            return None

