import random

class dado():
    def __init__(self, dadox):
        self.dado = dadox
    
    def rolar(self):
        if self.dado == 6:
            return random.randint(1,6)

        elif self.dado == 8:
            return random.randint(1,8)
        
        elif self.dado == 12:
            return random.randint(1,12)
        
        else:
            print('numero de dado invalido')

D6 = dado(6)
D8 = dado(8)
D12 = dado(12)
D13 = dado(13)

for i in range(3):
    print('d6 = ', D6.rolar()),
    print('d8 = ',D8.rolar()),
    print('d12 = ',D12.rolar())