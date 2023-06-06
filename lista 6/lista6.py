class UnidadeMilitar:
    def mover(self):
        print("A unidade está se movendo.")
    
    def atacar(self):
        print("A unidade está atacando.")

class Soldado(UnidadeMilitar):
    def mover(self):
        print("O soldado está marchando para a batalha.")
    
    def atacar(self):
        print("O soldado está atacando com sua espada.")

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("O arqueiro está se deslocando para encontrar uma posição estratégica.")
    
    def atacar(self):
        print("O arqueiro está disparando suas flechas.")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("O cavaleiro está galopando para o combate.")
    
    def atacar(self):
        print("O cavaleiro está investindo com sua lança.")

unidades = []
unidades.append(Soldado())
unidades.append(Arqueiro())
unidades.append(Cavaleiro())

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print()

