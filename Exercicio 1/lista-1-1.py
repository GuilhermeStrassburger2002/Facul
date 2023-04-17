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
# dia = int(input('informe o dia '))
# mes = int(input('informe o mes '))
# ano = int(input('informe o ano '))

data = Data(2023,12,5)

data.imprimidata()
data.imprimirdataporextensão(cidade)
