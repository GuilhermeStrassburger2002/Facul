class mago():
    def __init__(self, nome, idade, escola, tipo, magia, dano, vidaM):
        self.nome = nome
        self.idade = idade
        self.escola = escola
        self.tipo = tipo
        self.magia = magia
        self.dano = dano
        self.danoE = 100
        self.vidaE  = 300
        self.vidaM = vidaM
        print('mago', self.nome, 'foi criado!')

    def atacar(self):
        print('ataco usando', self.magia, 'do tipo', self.tipo)

    def falar(self):
        print('ola sou', self.nome)

    def danoEnemy(self):
        self.vidap = self.vidaE - self.dano
        if self.vidap <= 0:
            print('inimigo morto')
        else:
            self.vidaE = self.vidap
            print(self.vidaE)
            print('inimigo ataca')
            self.vidaM = self.vidaM - self.danoE

    def morte(self):
        if self.vidaM <= 0:
            print('você morreu')
        else:
            print(self.vidaM)

# nome = input('informe o nome ')
# idade = input('informe a idade ')
# escola = input('informe a escola ')
# tipo = input('informe o tipo de magia ')
# magia = input('informe a magia ')
# dano = int(input('informe o dano '))
# vidaM = int(input('informa a vida do mago '))

magician = mago('gundalf', 300, 'cinza', 'radiante', 'clarão', 400, 600)
magician = mago('harry', 17, 'hogwarts', 'bruxaria', 'reducto', 200, 100)

magician.falar()
magician.atacar()
magician.danoEnemy()
magician.morte()