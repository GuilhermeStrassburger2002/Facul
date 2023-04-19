from functools import reduce

class Pais():
    def __init__(self):
        self.__iso = ''
        self.__nome = ''
        self.__populacao = 0
        self.__dimensao = float
        self.__visinho = []

    def set_iso(self,iso):
        self.__iso = iso

    def set_nome(self,nome):
        self.__nome = nome

    def set_populacao(self,populacao):
        self.__populacao = populacao

    def set_dimensao(self,dimensao):
        self.__dimensao = dimensao

    def set_visinhos(self, visinho):
        self.__visinho = visinho

    def get_iso(self):
        return self.__iso
    
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    
    def get_dimensao(self):
        return self.__dimensao
    
    def get_visinhos(self):
        return self.__visinho
    
    def comparariso(self, pais02):
        if self.__iso == pais02.get_iso():

            return True
        else:

            return False
        
    def verificar_visinho(self, pais02):
        if pais02.get_nome() in self.__visinho:

            return True
        else:

            return False
        
    def calc_densidade(self):
        self.densidade = self.__populacao / self.__dimensao
        return self.densidade

    def vizinhos_comuns(self, pais02):
        vizinhosc = set(self.__visinho).intersection(pais02.get_visinhos())
        return vizinhosc



pais01 = Pais()
pais02 = Pais()
pais03 = Pais()
pais04 = Pais()
pais05 = Pais()

pais01.set_iso('BRA')
pais01.set_nome('Brasil')
pais01.set_populacao(200000000)
pais01.set_dimensao(800000000.00)
pais01.set_visinhos(['colombia', 'peru', 'uruguai', 'paraguai', 'bolivia', 'argentina', 'venezuela'])

pais02.set_iso('CL')
pais02.set_nome('chile')
pais02.set_populacao(19000000)
pais02.set_dimensao(756950.00)
pais02.set_visinhos(['argentina', 'bolivia', 'peru'])

pais03.set_iso('URU')
pais03.set_nome('uruguai')
pais03.set_populacao(3000000)
pais03.set_dimensao(176215.00)
pais03.set_visinhos(['argentina', 'brasil'])

pais04.set_iso('EQU')
pais04.set_nome('Equador')
pais04.set_populacao(17000000)
pais04.set_dimensao(283561.00)
pais04.set_visinhos(['colombia', 'peru'])

pais05.set_iso('ARG')
pais05.set_nome('argentina')
pais05.set_populacao(45000000)
pais05.set_dimensao(2780000.00)
pais05.set_visinhos(['chile', 'paraguai', 'bolivia', 'uruguai', 'brasil'])

print(pais01.calc_densidade())
print(pais01.comparariso(pais02))
print(pais01.vizinhos_comuns(pais02))
print(pais01.verificar_visinho(pais02))

class Continente():
    def __init__(self):
        self.nomecontinente = ''
        self.paises = []
        self.dimesaot = 0
        self.populacaot = 0

    def addpais(self, pais01):
        self.paises.append(pais01)
        return self.paises

    def dimesãocontinente(self):
        self.dimesaot = reduce(lambda x, y: x + y.get_dimensao(), self.paises, 0)
        return self.dimesaot
    
    def populaçãocontinente(self):
        self.populacaot = reduce(lambda x, y: x + y.get_populacao(), self.paises, 0)
        return self.populacaot
    
    def densidadecontinente(self):
        densidadet = self.populacaot / self.dimesaot
        return densidadet
    



Continente01 = Continente()

print(Continente01.addpais(pais01))
# print(Continente01.dimesãocontinente())
# print(Continente01.populaçãocontinente())
# print(Continente01.densidadecontinente())
