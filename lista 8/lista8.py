import random

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def exibirDescricao(self):
        print(f"Este é um animal chamado {self.nome}")


class Carnivoro(Animal):
    def caca(self):
        print(f"O animal carnívoro {self.nome} está caçando")
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal carnívoro")


class Herbivoro(Animal):
    def pastar(self):
        print(f"O animal herbívoro {self.nome} está pastando")
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal herbívoro")


class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        if random.randint(0, 1) == 0:
            self.caca()
        else:
            self.pastar()
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal onívoro")


# Exemplo de uso
leao = Carnivoro("Leão")
leao.exibirDescricao()
leao.caca()

girafa = Herbivoro("Girafa")
girafa.exibirDescricao()
girafa.pastar()

urso = Onivoro("Ser Humano")
urso.exibirDescricao()
urso.comer()
            