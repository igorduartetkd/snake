# Comida.py
from random import randint
import cores_rgb
import Elemento


class Comida(Elemento):
    def __init__(self, orientacao, posicao, cor=cores_rgb.red, lado_quadrado=30 ):
        super().__init__(orientacao, posicao, cor, lado_quadrado)


