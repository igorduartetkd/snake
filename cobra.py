# cobra.py
import cores_rgb
from elemento import Elemento
import math


class Cobra():
    def __init__(self, posicao_inicial=[10,10], cor=cores_rgb.green, tamanho_inicial=3, lado_quadrado=30):
        xini, yini = posicao_inicial
        self.__corpo = [Elemento(0, [x, yini], cor, lado_quadrado) for x in range(xini, xini + tamanho_inicial)]
        self.__cor = cor
        self.__lado_quadrado = lado_quadrado
        self.__comeu = 0

    def get_corpo(self):
        return self.__corpo

    def get_cabeca(self):
        return self.__corpo[-1]

    def get_rabo(self):
        return self.__corpo[0]

    def get_orientacao(self):
        return self.get_cabeca().get_orientacao()

    def get_cabeca_futuro(self):
        cabeca = self.get_cabeca()
        x = int(math.cos(math.radians(cabeca.get_orientacao())))
        y = int(math.sin(math.radians(cabeca.get_orientacao())))
        xc, yc = cabeca.get_posicao()
        return Elemento(cabeca.get_orientacao(), [xc+x, yc+y], self.__cor, self.__lado_quadrado) 

    def set_orientacao(self, orientacao):
        self.__corpo[-1].set_orientacao(orientacao)

    def deslocar(self):
        # criando quadrado novo (cabeca):
        cabeca = self.get_cabeca()
        x = int(math.cos(math.radians(cabeca.get_orientacao())))
        y = int(math.sin(math.radians(cabeca.get_orientacao())))
        xc, yc = cabeca.get_posicao()
        self.__corpo.append(Elemento(cabeca.get_orientacao(), [xc+x, yc+y], self.__cor, self.__lado_quadrado))

        if self.__comeu:
            self.__comeu = 0
        else:
            del self.__corpo[0]


    def engordar(self, ponto):
        self.__comeu = 1
