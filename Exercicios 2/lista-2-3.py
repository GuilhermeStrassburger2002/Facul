class Data():
    def __init__(self,ano,mes,dia):
        self._ano = ano
        self._mes = mes
        self._dia = dia

    def imprimidata(self):
        print(self._dia, '/', self._mes, '/', self._ano)

    def imprimirdataporextensão(self, cidade):

        if self._mes == 1:
            mese = 'janeiro'
        
        elif self._mes == 2:
            mese = 'fevereiro'

        elif self._mes == 3:
            mese = 'março'

        elif self._mes == 4:
            mese = 'abril'

        elif self._mes == 5:
            mese = 'maio'

        elif self._mes == 6:
            mese = 'junho'

        elif self._mes == 7:
            mese = 'julho'

        elif self._mes == 8:
            mese = 'agosto'
        
        elif self._mes == 9:
            mese = 'setembro'
        
        elif self._mes == 10:
            mese = 'outubro'

        elif self._mes == 11:
            mese = 'novembro'

        elif self._mes == 12:
            mese = 'dezembro'
        
        print('dia ', self._dia,'de ',  mese,  'do ano de ',  self._ano,  ', cidade de',  cidade)

    
cidade = input('nome da cidade ')

data = Data(2023,12,5)

class CadastroCliente:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.dataNascimento = ''
        self.email = ''
        self.cpf = ''
        self.__senha = ''
        self.__bloqueado = False

    def setNome(self, nome):
        self.nome = nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def setDataNascimento(self, dia, mes, ano):
        self.dataNascimento = Data()
        self.dataNascimento.alterarDia(dia)
        self.dataNascimento.alterarMes(mes)
        self.dataNascimento.alterarAno(ano)

    def setEmail(self,email):
        self.email = email
    
    def setCPF(self, cpf):
        self.cpf = cpf

    def setSenha(self, senha):
        self.__senha = senha
    
    def validarSenha(self, senhaDigitada):
        if self.__senha == senhaDigitada:
            return True
        else:
            return False
        
    def bloquear(self):
        self.__bloqueado = True

    def getNome(self):
        return self.nome
    
    def getSobrenome(self):
        return sobrenome



cliente = CadastroCliente()

nome = input('Digite nome: ')
cliente.setNome(nome)
sobrenome = input('Digite sobrenome: ')
cliente.setSobrenome(sobrenome)
senhaCriada = input('Digite a nova senha: ')
cliente.setSenha(senhaCriada)



contTentativas = 0
acertouSenha = False

while contTentativas < 3 and not acertouSenha:
    senhaDigitada = input('Digite sua senha: ')
    validacao = cliente.validarSenha(senhaDigitada)
    if validacao == True:
        acertouSenha = True
    else:
        print('Senha incorreta!')
    contTentativas = contTentativas + 1

if (acertouSenha == False):
    cliente.bloquear()
    print('Conta bloqueada!')

else:
    print('Dados do cliente: ')
    print(cliente.getNome(), ' ', cliente.getSobrenome())