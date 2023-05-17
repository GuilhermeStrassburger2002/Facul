import csv
import random
import os

class Figurinha():
    def __init__(self, nro,nomefig,conteudo,nroPagina):
        self.nro = nro
        self.nome = nomefig
        self.conteudo = conteudo
        self.status = None
        self.nroPagina = nroPagina
        self.listaFigurinhas = []
    
    def imprimirfig(self):
        print(self.nro,' ',self.nome,' ', self.conteudo, ' ', self.nroPagina)  

    def get_lista(self):
        return self.listaFigurinhas

    def carregarFigurinhas(self):
        arqFigurinhas = open('Figurinha.csv')
        leitor = csv.reader(arqFigurinhas,delimiter=';')
        listaFig = list(leitor)
        arqFigurinhas.close()

        for i in range(1, len(listaFig)):
            figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
            self.listaFigurinhas.append(figurinha)               

        # for i in range(len(self.listaFigurinhas)):
        #     self.listaFigurinhas[i].imprimirfig()     
        
fig = Figurinha(0, 0, 0, 0)

class Usuario():
    def __init__(self):
        self.nome = ''
        self.senha = ''
        self.album = [[None for _ in range(5)] for _ in range(3)]
        self.figurinhas = []
        self.figpossui = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.trocas = []
        self.true = True
        self.fig = Figurinha(0,0,0,0)

    def getfigpossui(self):
        return self.figpossui
    
    def novo_usuario(self):
        self.nome = input("Digite o nome de usuário: ")
        self.senha = input("Digite a senha: ")
        return {'nome_usuario': self.nome, 'senha': self.senha, 'album': {}, 'colecao': {}, 'trocas': {}}

    def ver_album(self):
        for i in range(0, 15):
            if self.figpossui[i] > 0:
                self.fig.get_lista()[i].imprimirfig()
        pagina_atual = 0
        while self.true == True:
            print(f"Página {pagina_atual + 1}")
            for linha in self.album[pagina_atual]:
                for self.figpossui in linha:
                    if self.figpossui == 0:
                        print("  ", end="")
                    elif self.figpossui.status == 1:
                        print(" X", end="")
                    elif self.figpossui.status == 2:
                        print(" T", end="")
                    else:
                        print(" O", end="")
                print()
            print("O - Figurinha não colada")
            print("X - Figurinha colada no álbum")
            print("T - Figurinha disponível para troca")
            opcao = input("Digite 'n' para ir para a próxima página, 'p' para a página anterior ou 'v' outra tecla para voltar ao menu: ")
            if opcao == "n":
                pagina_atual = (pagina_atual + 1) % 18
            elif opcao == "p":
                pagina_atual = (pagina_atual - 1) % 18
            elif opcao == 'v':
                print('Voltou ao MENU!')
            else:
                print('Sua resposta não foi: [n], [p] e nem [v]')
                print('VERIFIQUE!')
        
    def carregar_dados(self):
        with open("nome_arquivo.csv", mode= 'a', newline= '') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow([self.nome,self.senha , self.album, self.figurinhas, self.trocas])

            # leitor_csv = csv.reader(arquivo, delimiter=',')
            # dados = list(leitor_csv)
        # return dados
    
    def pacotrinho(self):
        fig1 = random.randint(0,14)
        fig2 = random.randint(0,14)
        fig3 = random.randint(0,14)
        self.figpossui [fig1] = self.figpossui [fig1] +1
        self.figpossui [fig2] = self.figpossui [fig2]+1
        self.figpossui [fig3] = self.figpossui [fig3]+1
        print(self.figpossui)

    # def gerenciar_colecao(self):
    #     visualizar_colecao(colecao)
    #     print("1 - Adicionar figurinha ao álbum")
    #     print("2 - Disponibilizar figurinha para troca")
    #     print("3 - Ver minhas trocas")
    #     print("4 - Voltar ao menu anterior")
    #     opcao = int(input("Escolha uma opção: "))
    #     if opcao == 1:
    #         figurinha = int(input("Digite o número da figurinha que deseja adicionar ao álbum: "))
    #         if figurinha in colecao:
    #             album[figurinha] = {'status': 0, 'nome': colecao[figurinha]['nome'], 'informacao': colecao[figurinha]['informacao'], 'pagina': (figurinha // 5) + 1}
    #             del colecao[figurinha]
    #             print(f"Figurinha {figurinha} adicionada ao álbum.")
    #         else:
    #             print("Você não possui essa figurinha.")
    #     elif opcao == 2:
    #         figurinha
#-------------------------------------------------------------------------------------------------

# Função para salvar os dados no arquivo csv
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=',')
        for linha in dados:
            escritor_csv.writerow(linha)

# Função para acessar o álbum
def acessar_album(usuarios):
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario['nome_usuario'] == nome_usuario and usuario['senha'] == senha:
            return usuario
    print("Usuário ou senha incorretos.")
    return None

# Função para listar as figurinhas de uma página do álbum
def listar_figurinhas(pagina, album, colecao):
    print(f"--- Página {pagina} ---")
    for i in range((pagina-1)*5, pagina*5):
        if i in album:
            if album[i]['status'] == 1:
                print(f"{i}: {album[i]['nome']} ({album[i]['informacao']})")
            else:
                print(f"{i}: COLADA")
        elif i in colecao:
            print(f"{i}: COLAR")
        else:
            print(f"{i}: X")

# Função para visualizar a coleção de figurinhas
def visualizar_colecao(colecao):
    print("----- Minha Coleção -----")
    for i in range(0, 15):
        if i in colecao:
            print(f"{i}: {colecao[i]}")
        else:
            print(f"{i}: 0")
    print("------------------------")

# Função para gerenciar a coleção de figurinhas
def gerenciar_colecao(album, colecao, trocas):
    visualizar_colecao(colecao)
    print("1 - Adicionar figurinha ao álbum")
    print("2 - Disponibilizar figurinha para troca")
    print("3 - Ver minhas trocas")
    print("4 - Voltar ao menu anterior")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        figurinha = int(input("Digite o número da figurinha que deseja adicionar ao álbum: "))
        if figurinha in colecao:
            album[figurinha] = {'status': 0, 'nome': colecao[figurinha]['nome'], 'informacao': colecao[figurinha]['informacao'], 'pagina': (figurinha // 5) + 1}
            del colecao[figurinha]
            print(f"Figurinha {figurinha} adicionada ao álbum.")
        else:
            print("Você não possui essa figurinha.")
    elif opcao == 2:
        figurinha

#-----------------------------------------------------------------------------------------
# Aqui é onde tudo aconte!

sair = False
opc = False
usu = Usuario()
fig = Figurinha(0, 0, 0, 0)

def carregar_dados():
    if os.path.isfile('nome_arquivo.csv'):
        with open('nome_arquivo.csv', 'r') as arquivo:
        # Ler o conteúdo do arquivo
                    leitor_csv = csv.reader(arquivo)
                    for linha in leitor_csv:
                        print(linha)
    else:
        print('Arquivo não encontrado.')                


carregar_dados()
fig.carregarFigurinhas()
fig.imprimirfig()

while sair == False:
    print("------ MENU -------")
    print("1 - Novo Album.")
    print("2 - Acessar Album.")
    print("3 - Sair")
    opcaoMenu = int(input('Escola uma das opção:'))

    if opcaoMenu == 1:

        usu.novo_usuario()
        usu.carregar_dados()

    elif opcaoMenu == 2:
            while opc == False:
                print("------ MENU -------")
                print("1 - Ver Album.")
                print("2 - Colar Figurinha.")
                print("3 - Abrir Pacotinho.")
                print("4 - Voltar")
                opcaoMenu2 = int(input('Escola uma das opção:'))
                if opcaoMenu2 == 1:
                    usu.ver_album()
                
                # elif opcaoMenu2 == 2:

                elif opcaoMenu2 == 3:
                    usu.pacotrinho()

                elif opcaoMenu2 == 4:
                    opc = True
    

    elif opcaoMenu == 3:
        # Função para salvar os dados no arquivo csv
        def salvar_dados(nome_arquivo, dados):
            with open(nome_arquivo, 'a', newline='') as arquivo:
                escritor_csv = csv.writer(arquivo, delimiter=',')
            for linha in dados:
                escritor_csv.writerow(linha)
