import random
       
opções = ('Pedra' , 'Papel', 'Tesoura')

vitórias_usuario = 0
vitórias_computador = 0

def formatar(msg):
        tamanho = len(msg)
        print('_' * tamanho)
        print(msg)
        print('_' * tamanho)

while True:
    print('\nPedra, Papel, Tesoura\n')
    usuario = input('\nInforme sua escolha: ').capitalize()
    
    computador = random.choice(opções)
    
    if usuario not in opções:
        print('\nOpção inválida! escolha uma opção entre Pedra, Papel e Tesoura.\n')
        continue
        
    formatar(f'\nVocê escolheu {usuario}\nE o computador escolheu {computador}\n')
    
    if usuario == computador:
        formatar('\nHouve empate!\n')
        
    elif(
        (usuario == 'Pedra' and computador == 'Tesoura') or 
        (usuario == 'Papel' and computador == 'Pedra') or 
        (usuario == 'Tesoura' and computador == 'Papel')
    ):
        print('\nVocê venceu!\n')

        vitórias_usuario += 1

    else:
        print('\nO computador venceu!\n')
        vitórias_computador += 1
        
    print(f'Placar de vitórias do usuário: {vitórias_usuario}\nPlacar de vitórias do computador: {vitórias_computador}')
    
    while True:
        jogar_novamente = input('\nDeseja continuar jogando? (Sim / Não): \n').capitalize()
        if jogar_novamente in ['Sim', 'S']:
            break
        elif jogar_novamente in ['Nao', 'Não', 'N', 'Ñ']:
            print('Saindo...')
            break
        else:    
            print('Opcão inválida!')
    if jogar_novamente in ['Nao', 'Não', 'N', 'Ñ']:
        break