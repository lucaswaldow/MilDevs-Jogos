import random
import os
def constroi_memoria(tamanho):
    memoria = []
    for coluna in range(tamanho):
        matriz_temp = []
        for linha in range(tamanho):
            matriz_temp.append('     ')
        memoria.append(matriz_temp)

    return memoria

def constroi_posicoes_livres(tamanho):
    posicoes_livres = []
    for linha in range(tamanho):
        for coluna in range(tamanho):
            posicoes_livres.append(str(linha)+str(coluna))

    return posicoes_livres

def retorna_posicoes_livres(posicoes_diagonal, ultima_jogada):
    posicoes_livres = []

    # converte a ultima jogada do usuario para
    # uma jogada possivel das posicoes da matriz
    linha = int(ultima_jogada[0:1]) - 1
    coluna = int(ultima_jogada[1:2]) - 1
    ultima_jogada = str(linha) + str(coluna)

    # pesquisa se a posicao jogada do usuario esta na lista de posicoes
    if ultima_jogada in posicoes_diagonal:
        # se estiver pegamos cada uma destas posicoes e acessamos o conteudo da memoria
        for valor in posicoes_diagonal:
            # obtem a linha e a coluna
            linha = valor[0:1]
            coluna = valor[1:2]
            # obtem o conteudo da memoria
            conteudo = memoria[int(linha)][int(coluna)]

            # se ja existir uma jogada do computador na diagonal
            if conteudo == '  0  ':
                # limpa as posicoes livres
                posicoes_livres.clear()
                return posicoes_livres
            elif conteudo == '     ':
                # se as posicoes estiverem vazias adiciona a posicao na lista de posicoes livres
                posicoes_livres.append(str(linha) + str(coluna))

    return posicoes_livres

def ganha_na_diagonal_principal(memoria, ultima_jogada):
    # grava em uma lista todas as posicoes existentes na diagonal principal
    posicoes_diagonal_principal = []
    for i in range(len(memoria)):
        posicoes_diagonal_principal.append(str(i) + str(i))

    return retorna_posicoes_livres(posicoes_diagonal_principal, ultima_jogada)

def ganha_na_diagonal_secundaria(memoria, ultima_jogada):
    # grava em uma lista todas as posicoes existentes na diagonal secundaria
    posicoes_diagonal_secundaria = []
    for i in range(len(memoria)):
        posicoes_diagonal_secundaria.append(str(i) + str(len(memoria) - 1 - i))

    return retorna_posicoes_livres(posicoes_diagonal_secundaria, ultima_jogada)

def ganha_na_coluna(memoria, ultima_jogada):
    '''funcao que descobre se o usuario pode ganhar na coluna baseado na sua ultima jogada.
        Se o usuario puder ganhar, retorna a lista com as posicoes vazias em que o usuario pode jogar,
        se nao puder ganhar, retorna uma lista vazia'''
    # converter coluna da jogda do usuario para
    # coluna equivalente da matriz
    coluna = int(ultima_jogada[1:2]) - 1
    posicoes_livres = []

    for i in range(len(memoria)):
        conteudo = memoria[i][coluna]
        if conteudo == '  0  ':
            posicoes_livres.clear()
            break
        elif conteudo == '     ':
            posicoes_livres.append(str(i) + str(coluna))
    return posicoes_livres

def ganha_na_linha(memoria, ultima_jogada):
    '''funcao que descobre se o usuario pode ganhar na linha baseado na sua ultima jogada.
    Se o usuario puder ganhar, retorna a lista com as posicoes vazias em que o usuario pode jogar,
    se nao puder ganhar, retorna uma lista vazia'''
    # converter a linha da jogda do usuario para
    # linha equivalente da matriz
    linha = int(ultima_jogada[0:1]) - 1
    posicoes_livres = []

    # descobre as posicoes livres na linha em que o usuario fez a ultima jogada
    for i in range(len(memoria)):
        conteudo = memoria[linha][i]
        if conteudo == '  0  ':
            # se tiver nesta linha uma jogada do computador, deve parar o laco pois
            # nao tem como o jogadar usuario ganhar na proxima jogada completando a linha
            # garante que nao tem nenhuma posicao salva em posicoes livres
            posicoes_livres.clear()
            break
        # conteudo esta vazio, o jogador pode jogar nas proximas jogadas nesta posicao para ganhar
        elif conteudo == '     ':
            posicoes_livres.append(str(linha) + str(i))
    return posicoes_livres

def valida_ganhador(matriz, jogador):
    # verifica se tem ganhador
    tamanho = len(matriz)
    contador = 0
    # testando se o ganhou nas linhas
    for linha in range(tamanho):
        for coluna in range(tamanho):
            # conta a quantidade de posicoes marcadas pelo mesmo jogador
            if (matriz[linha][coluna] == jogador):
                contador += 1
            # se nao tiver a marcacao do jogador em questao na sequencia
            # ao tem como ele ter ganhado. Finaliza o laco
            else:
                break
        # caso a quantidade de marcacoes for equivalente ao tamanho
        # da matriz, tivemos um ganhador
        if contador == tamanho:
            return True
        contador = 0

    contador = 0
    # testa se ganhou nas colunas
    for linha in range(tamanho):
        for coluna in range(tamanho):
            if (matriz[coluna][linha] == jogador):
                contador += 1
            else:
                break
        if contador == tamanho:
            return True
        contador = 0

    contador = 0
    # testa se ganhou na diagonal principal
    for valor in range(tamanho):
        if (matriz[valor][valor] == jogador):
            contador += 1
        else:
            break

        if contador == tamanho:
            return True

    contador = 0
    # testa se ganhou na diagonal secundaria
    for valor in range(tamanho):
        if (matriz[valor][(tamanho - valor) - 1] == jogador):
            contador += 1
        else:
            break

        if contador == tamanho:
            return True

    return False

def remove_jogada(posicoes_livres, linha, coluna):
    '''Funcao que remove a jogada de um usuario das posicoes livres'''
    posicao = str(linha - 1) + str(coluna - 1)
    posicoes_livres.remove(posicao)
    return posicoes_livres

def valida_jogada(posicoes_livres, linha, coluna):
    '''A funcao deve percorrer a lista de posicoes livres e retornar
    verdadeiro se a concatenacao de LinhaColuna existe na lista, ou
    false se nao existir'''
    posicao = str(linha - 1) + str(coluna - 1)
    return posicao in posicoes_livres

def imprimi_desenho_matriz(memoria):
    '''Esta funcao tem como objetivo imprimir uma estrutura visual que apresente a atual situacao
     do jogo da velha. Apresentando quais posicoes estao vazias e quais estao preenchidas.
     Para isto a funcao recebe a lista XxX (X linhas e X colunas) '''
    os.system('cls')
    tamanhoMatriz = len(memoria)

    print('Coluna:          1      2       3   \n')

    for linha in range(tamanhoMatriz):
        print(f'linha {linha + 1}         ', end='')
        for coluna in range(tamanhoMatriz):
            # caso estiver na ultima coluna nao deve imprimir o |
            if coluna == tamanhoMatriz - 1:
                print(f'{memoria[linha][coluna]}', end='')
            else:
                print(f'{memoria[linha][coluna]}|', end='')
        # quado estiver na ultima linha nao deve imprimir o tracejado
        if linha != tamanhoMatriz - 1:
            print('\n               ---------------------')
    print('\n')

TAMANHO = 3
# Chama a função para contruir a memoria
memoria = constroi_memoria(TAMANHO)
# contem as posicoes livres que podem ser jogadas ao longo do jogo
posicoes_livres = constroi_posicoes_livres(TAMANHO)
print('==== Bem vindo ao Jogo da Velha ====\n')
jogador = True  # jogador = True --> usuario  jogador = False --> computador
teve_ganhador = False
empate = False
# enquanto nao tiver um jogador ganhador, repete o laco
while not (teve_ganhador):
    imprimi_desenho_matriz(memoria)
    jogadaOK = False
    # enguanto nao tiver uma jogada ok repete a leitura
    while not (jogadaOK):
        # vez do jogador
        if jogador == True:
            linha, coluna = input('Digite dois valores separados por espaco LINHA COLUNA: ').split(' ')
            simbolo_jogador = '  X  '
        # vez do computador
        else:
            # descobrir as possibilidades de jogo do usuario para permitir que o computador se defenda
            ultima_posicao_joagada = str(linha) + str(coluna)
            proximas_posicoes = []

            proximas_posicoes.append(ganha_na_linha(memoria, ultima_posicao_joagada))
            proximas_posicoes.append(ganha_na_coluna(memoria, ultima_posicao_joagada))
            proximas_posicoes.append(ganha_na_diagonal_principal(memoria, ultima_posicao_joagada))
            proximas_posicoes.append(ganha_na_diagonal_secundaria(memoria, ultima_posicao_joagada))
            jogadapc = []
            for pl in proximas_posicoes:
                jogadapc.extend(pl)
                if len(pl) == 1:
                    jogadapc = pl
                    break

            if len(jogadapc) ==0:
                empate = True
                break
            jogada = random.choice(jogadapc)
            linha = int(jogada[0:1]) + 1
            coluna = int(jogada[1:2]) + 1
            simbolo_jogador = '  0  '

        linha = int(linha)
        coluna = int(coluna)
        # verifica se joagada realizada esta dentro das possiveis posicoes
        # e se nao esta sendo jogado em uma posicao que ja esteja ocupada
        jogadaOK = valida_jogada(posicoes_livres, linha, coluna)
        if not (jogadaOK):
            print('Jogada neste posicao nao e permitida!')
    if not(empate):
        # grava na memoria a posicao jogada
        memoria[linha - 1][coluna - 1] = simbolo_jogador
        # remove de posicoes livres a ultima posicao jogada
        posicoes_livres = remove_jogada(posicoes_livres, linha, coluna)
        # verifica se o atual jogador venceu
        teve_ganhador = valida_ganhador(memoria, simbolo_jogador)
        # Verifica se teve ganhador para poder mandar uma mensagem
        if teve_ganhador:
            imprimi_desenho_matriz(memoria)
            # Mensagem se usuario ganhar
            if simbolo_jogador == '  X  ':
                print('='*30)
                print(f'X0X0X0X0\033[92m {"Parabens"}\033[00m X0X0X0X0')
                print('Você ganhou!')
                print('=' * 30)
            # Mensagem se computador ganhou
            else:
                print('=' * 30)
                print(f'Você perdeu!!!\nX0X0X0X0\033[91m {"Tente novamente"}\033[00m X0X0X0X0')
                print('=' * 30)


        # faz a alternancia entre jogador e computador
        jogador = not (jogador)
    # Caso o jogo empate
    else:
        imprimi_desenho_matriz(memoria)
        print('X0' * 30)
        print(str(f'\033[94m {"Deu velha"}\033[00m').center(60))
        print('X0' * 30)
        break
