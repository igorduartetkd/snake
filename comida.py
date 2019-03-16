#comida.py
import cores_rgb
from elemento import Elemento


class Comida(Elemento):
    def __init__(self, orientacao=0, posicao=[1, 1], cor=cores_rgb.red, lado_quadrado=30 ):
        super().__init__(orientacao, posicao, cor, lado_quadrado)


