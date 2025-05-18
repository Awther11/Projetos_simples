from gerador_senhas import Gerador_Senha

if __name__ == '__main__':
    gerador = Gerador_Senha()
    gerador.Definir_Tamanho()
    senha = gerador.Geração()
    if senha:
        print('Senha criada: ', senha)