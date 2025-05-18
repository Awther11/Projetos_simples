from conjunto_caracteres import Conjunto_de_Caracteres

class Gerador_Senha:
    def __init__(self, tamanho = 0, conjunto = None, senha = ''):
        self.tamanho = tamanho
        self.conjunto = conjunto or Conjunto_de_Caracteres()
        self.senha = senha

    def Definir_Tamanho(self):
        self.tamanho = int(input('Informe o tamanho da senha: '))

    def Validar_Tamanho(self):
        return self.tamanho > 0
    
    def Variedade(self):
        pass

    def Geração(self):
        if not self.Validar_Tamanho():
            print('O tamanho deve ser superior a ZERO')
            return ''
        
        self.conjunto.Construir_Conjunto()
        self.senha = ''.join(
            self.conjunto.Caracteres_Aleatorios()
            for _ in range(self.tamanho)
        )
        return self.senha
