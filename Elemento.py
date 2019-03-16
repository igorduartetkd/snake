# Elemento.py


class Elemento():
    def __init__(self, orientacao, posicao, cor, lado_quadrado):
        self.__orientacao = orientacao
        self.__posicao = posicao
        self.__cor = cor
        self.__lado_quadrado = lado_quadrado

    def get_orientacao(self):
        return self.__orientacao

    def get_posicao(self):
        return self.__posicao

    def get_cor(self):
        return self.__cor

    def get_lado_quadrado(self):
        return self.__lado_quadrado

    def set_orientacao(self, orientacao):
        self.__orientacao = orientacao

    def set_posicao(self, posicao):
        self.__posicao = posicao

    def set_cor(self, cor):
        self.__cor = cor

    def set_lado_quadrado(self, lado_quadrado):
        self.__lado_quadrado = lado_quadrado