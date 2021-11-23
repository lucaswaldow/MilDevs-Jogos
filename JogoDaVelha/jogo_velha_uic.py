from PyQt6.QtWidgets import QMessageBox, QWidget, QPushButton
from PyQt6 import uic
from placar import Placar

class jogo_velha(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui\\velha.ui", self)

        self.placar = Placar()

        self.memoria = []
        self.jogador = "X"

        self.setWindowTitle('Vez do jogador X')
        # inicializa a memoria e os atributos dos botoes
        self.inicializar_jogo()

        # associa o metodo a ser executado quando ocorrer um click no botao
        # passa o botao clicado como parametro
        self.btn_0_0.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_0_0))
        self.btn_0_1.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_0_1))
        self.btn_0_2.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_0_2))
        self.btn_1_0.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_1_0))
        self.btn_1_1.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_1_1))
        self.btn_1_2.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_1_2))
        self.btn_2_0.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_2_0))
        self.btn_2_2.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_2_2))
        self.btn_2_1.clicked.connect(lambda x: self.btn_generico_clicked(self.btn_2_1))

    def inicializar_jogo(self):
        # inicializa o texto dos botoes para ""
        # para cada componente grafico do formulario
        for componente in self.children():
            # testa para verificar se o componente é um botao
            if isinstance(componente, QPushButton):
                #print(componente.objectName())
                # habilita o botão
                componente.setEnabled(True)
                # configura o atributo texto para ""
                componente.setText("")

        # inicializa a memoria com posicoes vazias
        self.memoria.clear()
        for linha in range(3):
            temp = []
            for coluna in range(3):
                temp.append("")
            self.memoria.append(temp)

    def ocorreu_empate(self):
        count = 0
        # para cada componente grafico do formulario
        for componente in self.children():
            # testa para verificar se o componente é um botao
            if isinstance(componente, QPushButton):
                # print(componente.objectName())
                # habilita o botão
                if componente.isEnabled() == False:
                    count += 1

        if count == 9:
            return True
        else:
            return False

    def verificar_ganhador(self):
        jogador = self.jogador
        matriz = self.memoria

        tamanho = len(matriz)
        contador = 0

        # testando se o ganhou nas linhas
        for linha in range(tamanho):
            elementos = []
            for coluna in range(tamanho):
                # conta a quantidade de posicoes marcadas pelo mesmo jogador
                if (matriz[linha][coluna] == jogador):
                    contador += 1
                # se nao tiver a marcacao do jogador em questao na sequencia
                # nao tem como ele ter ganhado. Finaliza o laco
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

    def exibir_msg_empate(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Deu Velha!!!")
        msgBox.setText(f"Boa sorte aos jogadores no próximo jogo.")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    def apresentar_msg_ganhador(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Parabéns ao Ganhador")
        msgBox.setText(f"Parabéns ao jogador {self.jogador}!           ")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    def btn_generico_clicked(self, obj):
        #if self.msg_confirma_jogada() == True:
            # if self.msg_confirma_jogada():
            # obtem a linha e coluna a partir do nome do botao clicado
            linha = int(obj.objectName()[4:5])
            coluna = int(obj.objectName()[6:7])

            #atualiza a memoria do tabuleiro
            self.memoria[linha][coluna] = self.jogador
            #ajusta a propriedade text do botão para exibir qual jogador fez a marcação
            obj.setText(self.jogador.strip())
            #desabilita o botao para que nao seja possivel uma nova jogada no botão
            obj.setEnabled(False)

            print()

            if self.verificar_ganhador():
                self.apresentar_msg_ganhador()

                if self.jogador == "O":
                    self.placar.set_vitoria_jogador_1()
                    self.lbl_jogador_o.setText(f"Jogador O: {self.placar.get_vitorias_jogador_1()}")
                else:
                    self.placar.set_vitoria_jogador_2()
                    self.lbl_jogador_x.setText(f"Jogador X: {self.placar.get_vitorias_jogador_2()}")

                self.inicializar_jogo()
            elif self.ocorreu_empate():
                self.exibir_msg_empate()
                self.inicializar_jogo()
            else:
                if self.jogador == "O":
                    self.jogador = "X"
                else:
                    self.jogador = "O"

                self.setWindowTitle(f'Vez do jogador {self.jogador}')