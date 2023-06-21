import csv

class Usuario:
    def __init__(self, Id, nome_usuario, senha, tipo_assinatura):
        self.id = Id
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.perfis = []

    def adicionar_perfil(self, nome, idade):
        if len(self.perfis) < self.tipo_assinatura.max_perfis:
            perfil = Perfil(nome, idade)
            self.perfis.append(perfil)
            print(f"Perfil '{nome}' adicionado com sucesso.")
        else:
            print("Número máximo de perfis atingido.")

    def remover_perfil(self, nome):
        for perfil in self.perfis:
            if perfil.nome == nome:
                self.perfis.remove(perfil)
                print(f"Perfil '{nome}' removido com sucesso.")
                return
        print(f"Perfil '{nome}' não encontrado.")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso.")

    def alterar_plano(self, novo_tipo):
        if novo_tipo == "Simples" or novo_tipo == "Premium":
            self.tipo_assinatura = novo_tipo
            print("Plano alterado com sucesso.")
        else:
            print("Tipo de assinatura inválido.")

    def reproduzir_midia(self, midia):
        if self.tipo_assinatura == "Simples":
            print("Exibindo propaganda...")
        print(f"Reproduzindo {midia}.")

    def buscar_midia(self, query):
        # Implementar a lógica de busca de mídia aqui
        pass

#------------------------------------------------------
class Perfil:
    def __init__(self, usuario, nome, idade):
        self.nome = nome
        self.idade = idade
        self.usuario  = usuario
        self.favoritos = []
        self.ultimos_assistidos = []

    def adicionar_favorito(self, midia):
        self.favoritos.append(midia)

    def remover_favorito(self, midia):
        if midia in self.favoritos:
            self.favoritos.remove(midia)

    def adicionar_ultimo_assistido(self, midia):
        if len(self.ultimos_assistidos) >= 10:
            self.ultimos_assistidos.pop(0)
        self.ultimos_assistidos.append(midia)

    def listar_midias_apropriadas(self, tipo, catalogo):
        midias_apropriadas = []
        for midia in catalogo.obter_lista(tipo):
            if midia.classificacao == "18+" or midia.classificacao == "Livre" or midia.classificacao == "10 anos":
                midias_apropriadas.append(midia)
            elif self.idade >= int(midia.classificacao.split()[0]):
                midias_apropriadas.append(midia)
        return midias_apropriadas

    def assistir_midia(self, midia):
        print(f"Você está assistindo: ", midia)
        self.adicionar_ultimo_assistido(midia)
        print(self.ultimos_assistidos)

    def favoritar_midia(self, midia):
        if midia not in self.favoritos:
            self.favoritos.append(midia)
            print('midia favotritada')
        elif midia in self.favoritos:
            self.favoritos.remove(midia)
            print('deu erro')

    def buscar_por_titulo(self, titulo, catalogo):
        for tipo in catalogo.tipos_midia:
            midias_tipo = catalogo.obter_lista(tipo)
            for midia in midias_tipo:
                if midia.titulo.lower() == titulo.lower():
                    return midia
        return None



class Midia:
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao):
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.classificacao = classificacao


class Serie(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, numero_temporadas, episodios_por_temporada):
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.numero_temporadas = numero_temporadas
        self.episodios_por_temporada = episodios_por_temporada


class Filme(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, duracao):
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.duracao = duracao


class Documentario(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, diretor):
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.diretor = diretor


class Animacao(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, estudio):
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.estudio = estudio


class ProgramaTV(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, canal):
        self.canal = canal
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
 #------------------------------------------------------
class TipoAssinatura:
    def __init__(self, max_perfis, propagandas, custo_mensal):
        self.max_perfis = max_perfis
        self.propagandas = propagandas
        self.custo_mensal = custo_mensal
#------------------------------------------------------        
def ler_dados_csv(arquivo_csv):
    dados = []

    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for linha in reader:
            dados.append(linha)

    return dados   

def criar_usuarios(dadosUsuarios):
    usuarios = []

    for linha in dadosUsuarios:
        # Extrair dados relevantes da linha
        Id = linha[0]
        nome = linha[1]
        senha = linha[2]
        tipoC = linha[3]
        

        # Criar objeto de Usuário com os dados da linha
        usuario = Usuario(Id, nome, senha, tipoC)

        # Adicionar usuário à lista de usuários
        usuarios.append(usuario)

    return usuarios
#------------------------------------------------------
def ler_virgula_csv(arquivo_csv):
    dados = []

    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for linha in reader:
            dados.append(linha)

    return dados
#------------------------------------------------------
def listar_perfis(lista_perfil):
    perfis = []

    for linha in lista_perfil:
        # Extrair dados relevantes da linha
        usuario = linha[0]
        nome = linha[1]
        idade = linha[2]
        

        # Criar objeto de Usuário com os dados da linha
        perfil = Perfil(usuario, nome, idade)

        # Adicionar usuário à lista de usuários
        perfis.append(perfil)

    return perfis
#------------------------------------------------------
def listar_serie(lista_serie):
    series = []

    for linha in lista_serie:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]
        nmr_temp = linha[6]
        nmr_eps = linha[7]
        

        # Criar objeto de Usuário com os dados da linha
        serie = Serie(id, tipo, titulo, genero, ano_lancamento, classificacao, nmr_temp, nmr_eps)

        # Adicionar usuário à lista de usuários
        series.append(serie)

    return series
#------------------------------------------------------
def listar_filmes(lista_filme):
    filmes = []

    for linha in lista_filme:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]
        duracao = linha[6]
        

        # Criar objeto de Usuário com os dados da linha
        filme = Filme(id, tipo, titulo, genero, ano_lancamento, classificacao, duracao)

        # Adicionar usuário à lista de usuários
        filmes.append(filme)

    return filmes
#------------------------------------------------------
def listar_docs(lista_docs):
    documentarios = []

    for linha in lista_docs:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]
        diretor = linha[6]
        

        # Criar objeto de Usuário com os dados da linha
        documentario = Documentario(id, tipo, titulo, genero, ano_lancamento, classificacao, diretor)

        # Adicionar usuário à lista de usuários
        documentarios.append(documentario)

    return documentarios
#------------------------------------------------------
def listar_anima(lista_anima):
    animacoes = []

    for linha in lista_anima:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]
        estudio = linha[6]
        

        # Criar objeto de Usuário com os dados da linha
        animacao = Animacao(id, tipo, titulo, genero, ano_lancamento, classificacao, estudio)

        # Adicionar usuário à lista de usuários
        animacoes.append(animacao)

    return animacoes
#------------------------------------------------------
def listar_prog(lista_prog):
    programas = []

    for linha in lista_prog:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]
        canal = linha[6]
        

        # Criar objeto de Usuário com os dados da linha
        programa = ProgramaTV(id, tipo, titulo, genero, ano_lancamento, classificacao, canal)

        # Adicionar usuário à lista de usuários
        programas.append(programa)

    return programas
#------------------------------------------------------
def listar_catalogo(lista_catalogo):
    itens = []

    for linha in lista_catalogo:
        # Extrair dados relevantes da linha
        id = linha[0]
        tipo = linha[1]
        titulo = linha[2]
        genero = linha[3]
        ano_lancamento = linha[4]
        classificacao = linha[5]

        # Criar objeto de Usuário com os dados da linha
        item = Midia(id, tipo, titulo, genero, ano_lancamento, classificacao)

        # Adicionar usuário à lista de usuários
        itens.append(item)

    return itens
#------------------------------------------------------

dadosUsuarios= ler_dados_csv('ExemploUsuarios.csv')
usuarios=criar_usuarios(dadosUsuarios)
lista_prog = ler_virgula_csv('progrmas.csv')
programas = listar_prog(lista_prog)
lista_anima = ler_virgula_csv('animações.csv')
animacoes = listar_anima(lista_anima)
lista_docs = ler_virgula_csv('documentarios.csv')
documentarios = listar_docs(lista_docs)
lista_filme = ler_virgula_csv('Filmes.csv')
filmes = listar_filmes(lista_filme)
lista_serie = ler_virgula_csv('series.csv')
series = listar_serie(lista_serie)
lista_catalogo= ler_virgula_csv('catalogo.csv')
itens=listar_catalogo(lista_catalogo)
lista_perfis= ler_dados_csv('ExemploPerfis.csv')
perfis=listar_perfis(lista_perfis)

loop= True

while loop ==True:
    print('\n---- Metflix ----')
    print('1 - Acessar')
    print('2 - Criar conta')
    print('3 - Sair')
    opcao=int(input('Adicione uma opção:'))
    
    if opcao == 1:
        logn = input('Adicione seu usuario:')
        senha = input('Adicione sus senha:')
        usuarioAtivo=None
        for usuario in usuarios:
            if usuario.nome_usuario == logn and usuario.senha == senha:
                    print(f'\nOlá {logn}!\n')
                    usuarioAtivo=usuario
                    usu = Usuario(usuario.Id, usuario.nome_usuario, usuario.senha, usuario.tipo_assinatura)
                    while opcao != 6:
                        escper = input('escolha um perfil: \n')
                        perfilAtivo=None
                        for perfil in perfis:
                            # print(perfil.usuario, ' ' , logn, perfil.nome, ' ', escper)
                            if perfil.usuario == logn and perfil.nome == escper:
                                perfilAtivo = escper
                                pfl = Perfil(perfil.usuario, perfil.nome, perfil.idade)
                                print('usuario selecionado foi', escper , '\n')
                                print('1 -Alterar assinatura')
                                print('2 -Acessar Perfil')
                                print('3 -Editar Perfil')
                                print('4 -Adicionar Perfil')
                                print('5 -Remover Perfil')
                                print('6 -Voltando ao Menu anterior')
                                opcao=int(input('\nAdicione uma opção:'))
                                
                                if opcao == 1: #Alterar assinatura
                                    pass
                                if opcao == 2:
                                    while opcao != 9:
                                        print('1 -Buscar por nome')
                                        print('2 -Ultimos assistindo')
                                        print('3 -Favarios')
                                        print('4 -Filmes')
                                        print('5 -Séries')
                                        print('6 -Documentário')
                                        print('7 -Animações')
                                        print('8 -Programas de TV')
                                        print('9 -Voltando ao Menu anterior')
                                        opcao=int(input('\nAdicione uma opção: \n'))
                                        if opcao == 1: #Buscar por nome
                                            # for item in itens:
                                            #     print (item.titulo)
                                            escolha = input('Escolha uma midia: ')
                                            midiaescolhido=None
                                            for item in itens:
                                                # print(item.titulo, ' ', escolha)
                                                if item.titulo == escolha:
                                                    midiaescolhido = escolha
                                                    print('bom')                                
                                                    break
                                        if opcao == 2: #Ultimos assistindo
                                            pfl.assistir_midia(escolha)
                                        if opcao == 3:
                                            pfl.adicionar_favorito(escolha)
                                        if opcao == 4:
                                            for filme in filmes:
                                                print(filme.id, filme.tipo, filme.titulo, filme.genero, filme.ano_lancamento, filme.classificacao, filme.duracao, '\n')
                                        if opcao == 5:
                                            for serie in series:
                                                print(serie.id, serie.tipo, serie.titulo, serie.genero, serie.ano_lancamento, serie.classificacao, serie.nmr_temp, serie.nmr_eps, '\n')
                                        if opcao == 6:
                                            for documentario in documentarios:
                                                print(documentario.id, documentario.tipo, documentario.titulo, documentario.genero, documentario.ano_lancamento, documentario.classificacao, documentario.diretor, '\n')
                                        if opcao == 7:
                                            for animacao in animacoes:
                                                print(animacao.id, animacao.tipo, animacao.titulo, animacao.genero, animacao.ano_lancamento, animacao.classificacao, animacao.estudio, '\n')
                                        if opcao == 8:
                                            for programa in programas:
                                                print(programa.id, programa.tipo, programa.titulo, programa.genero, programa.ano_lancamento, programa.classificacao, programa.canal, '\n')
                                        if opcao == 9:
                                            print('\nVoltando ao Menu anterior...') # não esta Voltando ao Menu anterior!!
                                            
                                if opcao == 3:
                                    pass
                                if opcao == 4:
                                    usu.adicionar_perfil
                                if opcao == 5:
                                    usu.remover_perfil(escper)
                                if opcao == 6:
                                    print('\nVoltando ao Menu anterior...')

                                    #break
                                #break
                            #else:
                            #    print('perfil inexistente \n')
                            #    break
                        if perfilAtivo == None:
                            print('perfil inexistente \n')
        if usuarioAtivo == None:
            print('\nsenha ou usuario incorreto!\n')
 
    elif opcao == 2:
        print('Criando conta!')
        with open('ExemploUsuarios', 'a', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)

        id = len()
        input(print)
    
    elif opcao == 3:
        print('\nSaindo...')
        loop=False
    else:
        print('\nVocê não colocou nenhuma das opção!')
        print('Escolha a opção novamente!\n')