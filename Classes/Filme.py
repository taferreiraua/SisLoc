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
