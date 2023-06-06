class Veiculo:
    def __init__(self, marca, ano, modelo):
        marca = ''
        ano = 0
        modelo  = ''

    def acelerar():
        print('Acelerando o veículo!')

    def frear():
        print('Freando o veículo!')

class Carro(Veiculo):
    def __init__(self, marca, ano, modelo, cor):
        cor = ''
        super().__init__(marca, ano, modelo)

    def ligar_radio():
        print('FreanLigando o rádio do carro!')  
    
    def ligar_radio():
        print('Abrindo a porta do carro!')

class Moto(Veiculo):
    def __init__(self, marca, ano, modelo, cilindrada):
        cilindrada = ''
        super().__init__(marca, ano, modelo)

    def Empinar():
        print('Empinando a moto!')

    def Buzinar():
        print('Buzinando a moto!')        

class Caminhao(Veiculo):
    def __init__(self, marca, ano, modelo, carga_max):
        carga_max = ''
        super().__init__(marca, ano, modelo)

    def Carregar():
        print('Carregando o caminhão!')

    def Descarregar():
        print('Descarregando o caminhão!')

class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            letra_cifrada = chr(ord(letra) ^ self.chave)
            texto_cifrado += letra_cifrada
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)
    
class CifraCesar(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('a'))
                texto_cifrado += letra_cifrada
            else:
                texto_cifrado += letra
        return texto_cifrado

    def decifrar(self, cifrado):
        decifrado = ""
        for letra in cifrado:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('a'))
                decifrado += letra_decifrada
            else:
                decifrado += letra
        return decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            letra_cifrada = chr(ord(letra) ^ self.chave)
            texto_cifrado += letra_cifrada
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)
    
texto = "Macarena!"
chave_cesar = 3
chave_xor = 7

cifra_cesar = CifraCesar(chave_cesar)
texto_cifrado_cesar = cifra_cesar.cifrar(texto)
texto_decifrado_cesar = cifra_cesar.decifrar(texto_cifrado_cesar)

cifra_xor = CifraXor(chave_xor)
texto_cifrado_xor = cifra_xor.cifrar(texto)
texto_decifrado_xor = cifra_xor.decifrar(texto_cifrado_xor)

print("Cifra de César:")
print("Texto cifrado:", texto_cifrado_cesar)
print("Texto decifrado:", texto_decifrado_cesar)

print("\nAlgoritmo XOR:")
print("Texto cifrado:", texto_cifrado_xor)
print("Texto decifrado:", texto_decifrado_xor)