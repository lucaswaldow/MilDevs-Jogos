class Placar:
    def __init__(self):
        self.__empates = 0
        self.__vitorias_jogador_1 = 0
        self.__vitorias_jogador_2 = 0

    def set_vitoria_jogador_1(self):
        self.__vitorias_jogador_1 += 1

    def set_vitoria_jogador_2(self):
        self.__vitorias_jogador_2 += 1

    def get_vitorias_jogador_1(self):
        return self.__vitorias_jogador_1

    def get_vitorias_jogador_2(self):
        return self.__vitorias_jogador_2

    def get_empates(self):
        return self.__empates