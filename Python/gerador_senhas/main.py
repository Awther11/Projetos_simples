from gerador_senhas import Gerador_Senha

if __name__ == '__main__':
    gerador = Gerador_Senha()
    gerador.Definir_Tamanho()
    senha = gerador.Geração()
    if senha:
        print(f'Senha criada: {senha}')
        print('A senha possui:', len(senha),'digitos')

# implementações futuras - armazenar as senhas salvas em um arquivo csv
# remodelar melhor a forma como o sistema interage com o usuário, criando um menu de opções
