import random
def cria_tabuleiro(tamanho): #1
    tabuleiro = []
    for coluna in range(tamanho):
        matriz_temp = []
        for linha in range(tamanho):
            matriz_temp.append('.')
        tabuleiro.append(matriz_temp)

    return tabuleiro

def insere_jogada(tabuleiro,linha ,coluna, caracter): #2
    tabuleiro[linha - 1][coluna - 1] = caracter
    return tabuleiro

def existe_posicao_jogada(tamanho,linha,coluna):#3
    if 0 < linha < tamanho+1 and 0 < coluna < tamanho+1:
        return True
    else:
        return False

def posicao_esta_livre(tabuleiro,linha,coluna):#4
    return True if tabuleiro[linha - 1][coluna - 1] == '.' else False

def obter_linha_coluna():
    entrada_ok = False
    while not (entrada_ok):
        try:
            linha, coluna = map(int, input("Digite dois valores separados por espaco LINHA COLUNA: ").strip(" ").split(' '))
            entrada_ok = True
        except ValueError:
            print("[ERRO] Informe apenas dois valores separados por espaço.")
    return linha, coluna

def obter_jogada_usuario(tabuleiro):#6
    tamanho = len(tabuleiro)
    entrada_ok = False
    while not(entrada_ok):
        linha, coluna = obter_linha_coluna()
        entrada_ok = True
        if entrada_ok:
            #valida se jogada é permitida baseado na memoria do tabuleiro do jogo
            #nao e permitido uma posicao que nao existe e nem uma posicao que ja esta preenchida
            if existe_posicao_jogada(tamanho, linha, coluna):
                entrada_ok = posicao_esta_livre(tabuleiro, linha, coluna)
            else:
                entrada_ok = False
            if not(entrada_ok):
                print("[ERRO] Você não pode jogar nesta posição, pois ela já foi jogada anteriormente.")
    return linha, coluna

def obter_jogada_computador(tabuleiro):#7
    tamanho = len(tabuleiro)
    while True:
        linha = random.randint(0, tamanho)
        coluna = random.randint(0, tamanho)
        verifica_jogadapc = posicao_esta_livre(tabuleiro, linha, coluna)
        if verifica_jogadapc:
            return linha, coluna

def retorna_conteudo_posicao(tabuleiro,linha,coluna):#8
    return tabuleiro[linha - 1][coluna - 1]

def imprime_tabuleiro(tabuleiro_usuario,tabuleiro_computador):#9
    ''' Esta funcao tem como objetivo imprimir uma estrutura visual que apresente a atual situacao
         do jogo. Apresentando os dois tabuleiros e quais posicoes estao marcadas.
         Para isto a funcao recebe dois tabuleiros '''
    tamanhoTabuleiro = len(tabuleiro_usuario)
    espaco = ' ' * 9  # espaco entre os tabuleiros
    print(f'Tabuleiro Usuario{espaco}      {" " * (tamanhoTabuleiro + 2)}Tabuleiro Computador\n')
    sequencia = ''
    for numero in range(tamanhoTabuleiro):
        if numero + 1 > 9:
            sequencia += str(numero + 1)
        else:
            sequencia += str(numero + 1) + ' '
    print(f"            {sequencia}{espaco}             {sequencia}\n")  # numeros das colunas
    # sempre formar o tamnho exato de - que vou precisar para fazer a parte de cima do tabuleiro
    linha_comeco_final = '-' * ((tamanhoTabuleiro * 2) + 1)
    print(f"          +{linha_comeco_final}+                   +{linha_comeco_final}+")  # partede cima do tabuleiro
    # ira imprimir todas linhas e seus conteudos, de um jeito que pareca um tabuleiro
    for linha in range(tamanhoTabuleiro):
        if linha + 1 > 9:
            print(f"{linha + 1}        | ", end="")
        else:
            print(f"{linha + 1}         | ", end="")
        for coluna in range(tamanhoTabuleiro):
            # caso estiver na ultima coluna nao deve imprimir o |
            if coluna == tamanhoTabuleiro - 1:
                print(f"{tabuleiro_usuario[linha][coluna]}", end="")
            else:
                print(f"{tabuleiro_usuario[linha][coluna]} ", end="")
        # quado estiver na ultima linha nao deve imprimir o tracejado
        if linha != tamanhoTabuleiro:
            print(f' |{espaco}', end='')
            # aqui imprimi a parte do tabuleiro do computador (tabuleiro_2)
            if linha + 1 > 9:
                print(f"{linha + 1}        | ", end="")
            else:
                print(f"{linha + 1}         | ", end="")
            for coluna in range(tamanhoTabuleiro):
                # caso estiver na ultima coluna nao deve imprimir o |
                if coluna == tamanhoTabuleiro - 1:
                    print(f"{tabuleiro_computador[linha][coluna]}", end="")
                else:
                    print(f"{tabuleiro_computador[linha][coluna]} ", end="")
            if linha != tamanhoTabuleiro:
                print(' |')

    print(f"          +{linha_comeco_final}+ {espaco}{espaco}+{linha_comeco_final}+")
    print("\n")

def inicializar_tabuleiro_usuario(tabuleiro_usuario):#10
    print('digite as pasicoes dos seus barcos')
    tabuleiro_posicoes_marcadas = tabuleiro_usuario
    for n in range(8):
        linha, coluna = obter_jogada_usuario(tabuleiro_posicoes_marcadas)
        tabuleiro_posicoes_marcadas = insere_jogada(tabuleiro_posicoes_marcadas, linha, coluna, 'X')
        print(tabuleiro_posicoes_marcadas)
    return tabuleiro_posicoes_marcadas

def inicializar_tabuleiro_computador(tabuleiro_computador):#11
    tabuleiro_posicoes_marcadas = tabuleiro_computador
    for n in range(8):
        linha, coluna = obter_jogada_computador(tabuleiro_posicoes_marcadas)
        tabuleiro_posicoes_marcadas = insere_jogada(tabuleiro_posicoes_marcadas, linha, coluna, 'X')
    return tabuleiro_posicoes_marcadas

def marcar_posicao_atingida(tabuleiro, linha, coluna):#12
    caracter_posicao = retorna_conteudo_posicao(tabuleiro, linha, coluna)
    if caracter_posicao == '.':
        tabuleiro_atualizado = insere_jogada(tabuleiro,linha, coluna, '*')
        return tabuleiro_atualizado, False
    elif caracter_posicao == 'X':
        tabuleiro_atualizado = insere_jogada(tabuleiro, linha, coluna, '#')
        return tabuleiro_atualizado, True


print(cria_tabuleiro(8))
tabuleiro_usuario = cria_tabuleiro(8)
tabuleiro_Computador = cria_tabuleiro(8)
inicializar_tabuleiro_usuario(tabuleiro_usuario)
tamanho = len(tabuleiro_Computador)
# linha, coluna = obter_jogada_usuario(tabuleiro_usuario)
# print(type(linha))
# tabuleiro_usuario = insere_jogada(tabuleiro_usuario, linha, coluna, 'caracter')
# print(retorna_conteudo_posicao(tabuleiro_usuario, linha, coluna))
# linha, coluna = map(int,input("Digite dois valores separados por espaco LINHA COLUNA: ").split(' '))
# print(insere_jogada(tabuleiro,linha,coluna))
#print(existe_posicao_jogada(linha, coluna))
# print(posicao_esta_livre(linha, coluna))