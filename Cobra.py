# Cobra.py
import cores_rgb
from Elemento import Elemento
import math


class Cobra():
    def __init__(self, posicao_inicial=[10,10], cor=cores_rgb.blue, tamanho_inicial=3, lado_quadrado=30):
        xini, yini = posicao_inicial
        self.__corpo = [Elemento(0, [x, yini], cor, lado_quadrado) for x in range(xini, tamanho_inicial)]
        self.__pontos_engorda = []
        self.__cor = cor
        self.__lado_quadrado = lado_quadrado

    def get_corpo(self):
        return self.__corpo

    def get_cabeca(self):
        return self.__corpo[-1]

    def get_rabo(self):
        return self.__corpo[0]

    def deslocar(self):
        # criando quadrado novo (cabeca):
        cabeca = self.get_cabeca()
        x = math.cos(cabeca.get_orientacao())
        y = math.sin(cabeca.get_orientacao())
        xc, yc = cabeca.get_posicao()
        self.__corpo.append(Elemento(cabeca.get_orientacao(), [xc+x, yc+y], self.__cor, self.__lado_quadrado))

        # apagando quadrado antigo (rabo):
        rabo = self.get_rabo()
        if rabo.get_posicao() not in self.__pontos_engorda:
            del self.__corpo[0]

    def engordar(self, ponto):
        self.__pontos_engorda.append(ponto)