from datetime import date


class Filme:
    def __init__(self, codigo: str, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = list()
        self.data = date
        self.diretores = list()
        self.atores = list()
        self.sinopse = str()
        self.produtores = list()
        self.preco = float()
        self.copias = int()

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def addGenero(self, genero):
        self.genero.append(genero)

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setDiretor(self, diretores):
        self.diretores = diretores

    def getDiretores(self):
        return self.diretores

    def addDiretor(self, diretor):
        self.diretores.append(diretor)

    def setAtores(self, atores):
        self.atores = atores

    def getAtores(self):
        return self.atores

    def addAtor(self, ator):
        self.atores.append(ator)

    def setSinopse(self, sinopse):
        self.sinopse = sinopse

    def getSinopse(self):
        return self.sinopse

    def setProdutores(self, produtores):
        self.produtores = produtores

    def getProdutores(self):
        return self.produtores

    def addProdutor(self, produtor):
        self.diretores.append(produtor)

    def setPreco(self, preco):
        self.preco = preco

    def getPreco(self):
        return self.preco

    def setCopias(self, copias):
        self.copias = copias

    def getCopias(self):
        return self.copias

    def Imprimir(self):
        print(f'Código: {self.codigo}\n'
              f'Título: {self.titulo}\n'
              f'Gêneros: {self.genero}\n'
              f'Data de lançamento: {self.data}'
              f'Atores: {self.atores}\n'
              f'Diretores: {self.diretores}\n'
              f'Sinopse: {self.sinopse}')
