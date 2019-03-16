#muro.py
from elemento import Elemento
import cores_rgb


class Muro():
    def __init__(self, tamanho_tela, lado_quadrado=30):
        [xtela, ytela] = tamanho_tela
        self.__tijolos = []
        for x in range(xtela):
            self.__tijolos.append(Elemento(0, [x, 0], cores_rgb.blue, lado_quadrado))
            self.__tijolos.append(Elemento(0, [x, ytela - 1], cores_rgb.green, lado_quadrado))
        for y in range(ytela):
            self.__tijolos.append((Elemento(0, [0, y], cores_rgb.green, lado_quadrado)))
            self.__tijolos.append((Elemento(0, [xtela - 1, y], cores_rgb.green, lado_quadrado)))

    def checar_colisao(self, posicao):
        for tijolo in self.__tijolos:
            if tijolo.get_posicao() == posicao:
                return True

        return False

    def get_tijolos(self):
        return self.__tijolos
