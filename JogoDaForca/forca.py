from random import randint
def sorteia_palavra_no_arquivo():
    '''Essa função sortei uma palavra dentro de um arquivo txt.
    Percorre as linhas do arquivo e guarda elas na lista palavras.
    Faz um randint com inicio 0 e final tamanho da lista de palvras e
    retorna uma palavar na posição do randint'''
    palavras = []
    caminho_aquivo_txt = 'c:\\forca.txt' #aqui vc deve colocar o caminho do arquivo forca.txt
    with open(f"{caminho_aquivo_txt}", encoding='utf-8', mode='r') as reader:
        line = reader.readline()
        while line != '':
            palavras.append(line)

            line = reader.readline()
    inicio = 0
    fim = len(palavras)
    sorteio_numero = randint(inicio, fim)
    return palavras[sorteio_numero].upper()

tentativas = 6
letras = []
palavra = sorteia_palavra_no_arquivo()#linha do arquivo sorteada
print('=== Bem vindo ao jogo da forca ===\n\n')
mascara = list('_'*(len(palavra) -1))
qnt_ = 1
while tentativas != 0 and qnt_:

    print(f'Tentativas restantes: {tentativas}')
    print(f'Letras tentadas: {" ".join(letras)}')
    print(f"Palavra a ser descoberta: {' '.join(mascara)}")
    letra = input('Digite uma letra: ').upper()
    letras.append(letra)
    acertou = False
    for l in range(len(palavra)):
        if palavra[l] == letra:
            mascara[l] = palavra[l]
            acertou = True
    if acertou == False:
        tentativas -= 1

    qnt_ = mascara.count('_') != 0
if qnt_ == 0:
    print('=' * 50)
    print(str(f'\033[92m {"Parabens"}\033[00m').center(50))
    print('Voce decobriu a palavra!    \O/')
    espaco = ' ' * 27

    print(f'{espaco}  | ')
    print(f'{espaco} / \  ')
    print('=' * 50)
else:
    print('='*50)
    print(str(f'\033[91m {"Loser"}\033[00m').center(50))
    print('Infelismente voce nao decobriu a palavra!     0')
    espaco = ' '*44

    print(f'{espaco} /|\  ')
    print(f'{espaco} / \  ')
    print(f'A palavra era {palavra}')
    print('=' * 50)