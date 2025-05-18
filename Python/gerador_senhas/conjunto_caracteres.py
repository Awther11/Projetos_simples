import string
import random

class Conjunto_de_Caracteres:
    def __init__(self):
        self.maiusculas = string.ascii_uppercase
        self.minusculas = string.ascii_lowercase
        self.digitos = string.digits
        self.simbolos = '!@#$%&*'
        self.conjunto_completo = ''

    def Construir_Conjunto(self):
        self.conjunto_completo = (
            self.maiusculas +
            self.minusculas +
            self.digitos +
            self.simbolos
        )

    def Caracteres_Aleatorios(self):
        if not self.conjunto_completo:
            self.Construir_Conjunto()
        return random.choice(self.conjunto_completo)