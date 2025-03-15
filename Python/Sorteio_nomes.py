import random

lista_nomes = []
nomes_sorteados = []

while True:
    opção = input("""
    [1] - Adicione nomes
    [2] - Sortear
    [3] - remover nome da lista
    [4] - Encerrar\n:""")

    if opção == '1':
        escolha = input('Digite o nome: ').strip().capitalize()
        if escolha:
            lista_nomes.append(escolha)
            print(f'"{escolha}" foi adicionado à lista!')
        else:
            print('Nome inválido! Tente novamente.')

    elif opção == '2':
        if not lista_nomes:
            print('Não há nomes para serem sorteados!')
            continue 

        nome_sorteado = random.choice(lista_nomes)
        lista_nomes.remove(nome_sorteado)
        nomes_sorteados.append(nome_sorteado)

        print(f'\n{nome_sorteado} foi sorteado!')
        print(f'Nomes sorteados: {", ".join(nomes_sorteados)}')
        if lista_nomes:
            print(f'Nomes restantes: {", ".join(lista_nomes)}\n')
        else:
            print('Nenhum nome restante.\n')


    elif opção == '3':
        if not lista_nomes:
            print('Não há nomes para serem removidos!')
        else:
            remoção = input('Qual nome deseja remover?: ').capitalize()
            lista_nomes.remove(remoção)
            print(f'O nome {remoção} foi removido')

    elif opção == '4':
        print(f'Programa encerrado!')
        break

    else:
        print('Opção inválida!')
