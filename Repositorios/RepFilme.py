from Classes.Filme import Filme


class RepositorioFilme:
    def __init__(self):
        self._filmes = list()

    def cadastrar(self, filme: Filme):
        jaCad = False
        for cadFilme in self._filmes:
            if cadFilme.getCodigo() == filme.getCodigo():
                jaCad = True
        if jaCad is True:
            print('Código já cadastrado.')
        else:
            self._filmes.append(filme)
            print('Filme cadastrado com sucesso!')

    def buscar(self, codigo: int):
        achou = False
        for cadFilme in self._filmes:
            if cadFilme.get_cod() == codigo:
                achou = True
                return cadFilme
        if achou is False:
            print('Filme não encontrado.')

    def atualizar(self, filme: Filme):
        filme = self.buscar(filme.getCodigo())
        if filme:
            filme.set_cod(filme.get_cod())
            filme.set_titulo(filme.get_titulo())
            filme.set_lancamento(filme.get_lancamento())
            filme.set_diretor(filme.get_diretor())
            filme.set_n_copias(filme.get_n_copias())
            filme.set_sinopse(filme.get_sinopse())
            filme.set_preco(filme.get_preco())
            filme.set_produtores(filme.get_produtores())
            filme.set_atores(filme.get_atores())
            filme.set_genero(filme.get_genero())
            print('Filme atualizado com sucesso!')

    def deletar(self, codigo: int):
        filme = self.buscar(codigo)
        if filme:
            self._filmes.remove(filme)
            print('Filme deletado com sucesso!')

    def listar(self):
        try:
            return self._filmes
        except TypeError:
            return None