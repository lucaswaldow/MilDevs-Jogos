import random
import os
def Menu(pc,usuario,empate):
    print("======== Placar ========")
    print(f'Computador = {pc}')
    print(f'Usuario = {usuario}')
    print(f'Empate = {empate}')
    print("======== Menu ========\n")
    print(f'Você tem 4 opções!\n\033[93m{"1 - Pedra"}\033[00m\n\033[93m{"2 - Papel"}\033[00m\n\033[93m{"3 - Tesoura"}\033[00m\n\033[91m{"4 - Finalizar"}\033[00m')

def mostra_jogadas(jogada_usuario,jogada_pc):
    '''Essa função apenas imprime qual a escolha de cada jogador'''
    os.system('cls')
    itens = ['Pedra','Papel','Tesoura']
    print(f'Usuario jogou {itens[jogada_usuario-1]} X Computador jogou {itens[jogada_pc-1]}')

def verifica_quem_ganha(jogada_usuario,jogada_pc):
    '''Essa função verifica se o usuario ou o computador ganhou
    Pega o numero do usuario e subitrai a do computador
    Ela retrona True se usuario ganhar e False se o Computador ganhar,
    alem de imprimir o ganhador'''
    diferenca = jogada_usuario - jogada_pc
    if diferenca == 1 or diferenca == -2:
        print('Usuario ganhou')
        return True
    elif diferenca == -1 or diferenca == 2:
        print('Computador ganhou')
        return False



placar_pc = 0
placar_usuario = 0
empate = 0
while True:
    # Imprime menu
    Menu(placar_pc, placar_usuario, empate)
    # Recole jogada dos jogadores
    jogada_pc = random.randint(1, 3)
    jogada_usuario = int(input('Digite sua opção de jogada: '))
    # Finaliza Jogo caso o usuario queira
    if jogada_usuario == 4:
        break
    # Mostra as opções jogadas pelos jogadores
    mostra_jogadas(jogada_usuario, jogada_pc)
    if jogada_pc == jogada_usuario:
        print('Empate')
        empate +=1
    elif verifica_quem_ganha(jogada_usuario, jogada_pc):
        placar_usuario += 1
    else:
        placar_pc += 1