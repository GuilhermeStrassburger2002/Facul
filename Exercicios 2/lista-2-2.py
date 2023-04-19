class calculadora():
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def somar(self):
        soma = 0
        soma = self.numero1 + self.numero2
        return soma
    
    def subtrair(self):
        subtracao = 0
        subtracao = self.numero1 - self.numero2
        return subtracao
    
    def Multiplicar(self):
        multiplicacao = 0
        multiplicacao = self.numero1 * self.numero2
        return multiplicacao

    def Dividir(self):
        divisao = 0
        if self.numero2 != 0:
            divisao = self.numero1 / self.numero2
            return divisao

        else:
            return ('erro -1')

Numeros = calculadora(11,43)

print(Numeros.somar())
print(Numeros.subtrair())
print(Numeros.Multiplicar())
print(Numeros.Dividir())