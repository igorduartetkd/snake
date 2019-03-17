# play.py

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from comida import Comida
from muro import Muro
from cobra import Cobra
import time
from random import randint


class play():
    def __init__(self):

        self.lado_quadrado = 20
        self.tam_tela_pixel = [900, 600]
        self.tam_tela = [int(self.tam_tela_pixel[0] / self.lado_quadrado),
                         int(self.tam_tela_pixel[1] / self.lado_quadrado)]
        self.cobra = Cobra(lado_quadrado=self.lado_quadrado)
        self.comida = Comida(0, [1, 1], lado_quadrado=self.lado_quadrado)
        self.muro = Muro(self.tam_tela, self.lado_quadrado)
        self.taxa_atualizacao = 1
        self.tela_habilitada = 1
        self.mudanca_orientacao = 0
        self.sortear_comida()
        self.score = 0
        self.score_maximo = 0
        self.cheat = 0


    def init(self):
        x, y = self.tam_tela_pixel
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(x, y)
        glutInitWindowPosition(200, 900)
        glutCreateWindow(b'Snake')

        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)

        gluOrtho2D(0, x, 0, y)
        glMatrixMode(GL_MODELVIEW)

        glClearColor(0.0, 0.0, 0.0, 0.0)

    def clock(self):
        glClear(GL_COLOR_BUFFER_BIT)

        if self.tela_habilitada == 1:       # tela de inicio
            self.desenhar_tela_inicio()
        elif self.tela_habilitada == 2:     # tela do jogo
            self.regras_jogo()
            self.desenhar_tela_jogo()
            glutPostRedisplay()
            time.sleep(1 / self.taxa_atualizacao)
        elif self.tela_habilitada == 3:     # tela final game over
            self.desenhar_tela_fim()
        elif self.tela_habilitada == 4:     # tela de pause
            self.desenhar_tela_pause()

        glFlush()

    def desenhar_tela_inicio(self):
        x, y = self.tam_tela_pixel
        glColor(1.0, 1.0, 1.0)
        self.desenhar_texto(" Snake Game", x*0.45, y/2)
        self.desenhar_retangulo(round(x*0.45), round(y*0.4), round(x*0.6), round(y*0.45))
        self.desenhar_texto("START", round(x*0.48), round(y*0.41))

    def desenhar_tela_jogo(self):
        x, y = self.tam_tela_pixel
        self.desenhar_muro()
        self.desenhar_comida()
        self.desenhar_cobra()
        glColor(0.0, 1.0, 1.0)
        self.desenhar_texto(str(self.score), x*0.9, y*0.9)

    def desenhar_tela_fim(self):
        x, y = self.tam_tela_pixel
        glColor(1.0, 0.0, 0.0)
        self.desenhar_texto("GAME OVER", x * 0.45, y / 2)
        glColor(1.0, 1.0, 1.0)
        self.desenhar_retangulo(round(x * 0.45), round(y * 0.4), round(x * 0.6), round(y * 0.45))
        self.desenhar_texto("RESTART", round(x * 0.465), round(y * 0.41))
        glColor(0.0, 1.0, 1.0)
        self.desenhar_texto("Your score  " + str(self.score), x * 0.02, y*0.9)
        glColor(0.0, 1.0, 0.0)
        self.desenhar_texto("Max. score  " + str(self.score_maximo), x * 0.02, y * 0.86)

    def desenhar_tela_pause(self):
        x, y = self.tam_tela_pixel
        self.desenhar_tela_jogo()
        glColor(1.0, 1.0, 0.0)
        self.desenhar_texto("PAUSE", round(x * 0.465), round(y * 0.41))

    def regras_jogo(self):
        self.cobra.set_orientacao(self.mudanca_orientacao)
        self.cobra.deslocar()

        cabeca = self.cobra.get_cabeca()
        corpo = self.cobra.get_corpo()
        posicao_cabeca = cabeca.get_posicao()

        # testando colisao com o proprio corpo
        for gomo in corpo[:-1]:
            if gomo.get_posicao() == posicao_cabeca: # colidiu com o proprio corpo
                self.tela_habilitada = 3

        # testando colisao com o muro
        if self.muro.checar_colisao(posicao_cabeca):
            self.tela_habilitada = 3

        # testando se comeu algo
        if self.comida.get_posicao() == posicao_cabeca:
            self.cobra.engordar(self.comida.get_posicao())
            self.sortear_comida()
            self.score += 10
            if self.score > self.score_maximo:
                self.score_maximo = self.score

        self.taxa_atualizacao = self.cheat + 5 + self.score / 50

    def reinicializar_jogo(self):
        del self.cobra
        self.cobra = Cobra(lado_quadrado=self.lado_quadrado)
        self.sortear_comida()
        self.score = 0
        self.mudanca_orientacao = 0
        self.taxa_atualizacao = 1
        self.cheat = 0

    def desenhar_muro(self):
        tijolos = self.muro.get_tijolos()
        r, g, b = tijolos[0].get_cor()
        glColor(r, g, b)
        glPolygonMode(GL_FRONT, GL_FILL)
        for tijolo in tijolos:
            self.desenhar_quadrado(tijolo.get_posicao(), tijolo.get_lado_quadrado())

    def desenhar_comida(self):
        r, g, b = self.comida.get_cor()
        glColor(r, g, b)
        glPolygonMode(GL_FRONT, GL_FILL)
        self.desenhar_quadrado(self.comida.get_posicao(), self.comida.get_lado_quadrado())

    def desenhar_cobra(self):
        corpo = self.cobra.get_corpo()
        r, g, b = corpo[0].get_cor()
        glColor(r, g, b)
        glPolygonMode(GL_FRONT, GL_LINE)
        for gomo in corpo:
            self.desenhar_quadrado(gomo.get_posicao(), gomo.get_lado_quadrado())

    def sortear_comida(self):
        corpo = self.cobra.get_corpo()
        xr, yr = 0, 0
        tentar_novamente = True
        while(tentar_novamente):
            tentar_novamente = False
            xr = randint(1, self.tam_tela[0] - 2)
            yr = randint(1, self.tam_tela[1] - 2)
            for gomo in corpo:
                if gomo.get_posicao() == [xr, yr]:
                    tentar_novamente = True
        self.comida.set_posicao([xr, yr])

    def desenhar_quadrado(self, pos_inicial, lado):
        x, y = pos_inicial
        x *= lado
        y *= lado

        glBegin(GL_POLYGON)
        glVertex2i(x, y)
        glVertex2i(x + lado, y)
        glVertex2i(x + lado, y + lado)
        glVertex2i(x, y + lado)
        glEnd()

    def desenhar_texto(self, texto, x, y):
        glRasterPos2f(x, y)
        for letra in texto:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(letra))
        glutSwapBuffers()

    def desenhar_retangulo(self, x_inicio, y_inicio, x_fim, y_fim):
        glPolygonMode(GL_FRONT, GL_LINE)
        glBegin(GL_POLYGON)
        glVertex2i(x_inicio, y_inicio)
        glVertex2i(x_fim, y_inicio)
        glVertex2i(x_fim, y_fim)
        glVertex2i(x_inicio, y_fim)
        glEnd()

    def mouse_inicio(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            xt, yt = self.tam_tela_pixel
            x1 = round(xt*0.45)
            x2 = round(xt*0.6)
            y1 = round(yt*0.55)
            y2 = round(yt*0.6)
            if x1 < x < x2 and y1 < y < y2:
                if self.tela_habilitada == 1:
                    self.tela_habilitada = 2
                    glutPostRedisplay()

                elif self.tela_habilitada == 3:
                    self.reinicializar_jogo()
                    self.tela_habilitada = 2
                    glutPostRedisplay()

    def keyboard_especiais(self, key,  x,  y):
        if self.tela_habilitada == 2:
            if key == GLUT_KEY_LEFT:    # seta esquerda
                if self.cobra.get_orientacao() != 0:
                    self.mudanca_orientacao = 180
            elif key == GLUT_KEY_RIGHT:   #seta direita
                if self.cobra.get_orientacao() != 180:
                    self.mudanca_orientacao = 0
            elif key == GLUT_KEY_UP:      # seta cima
                if self.cobra.get_orientacao() != 270:
                    self.mudanca_orientacao = 90
            elif key == GLUT_KEY_DOWN:    # seta baxo
                if self.cobra.get_orientacao() != 90:
                    self.mudanca_orientacao = 270

        if key == GLUT_KEY_PAGE_UP:
            self.cheat += 1
        elif key == GLUT_KEY_PAGE_DOWN:
            if self.cheat > -4:
                self.cheat -= 1

    def keyboard(self, key, x, y):
        if ord(key) == 27:   # esc
            exit(0);
        elif ord(key) == 32: # space
            if self.tela_habilitada == 2:
                self.tela_habilitada = 4
                glutPostRedisplay()
            elif self.tela_habilitada == 4:
                self.tela_habilitada = 2
                glutPostRedisplay()
            elif self.tela_habilitada == 1:
                self.tela_habilitada = 2
                glutPostRedisplay()
            elif self.tela_habilitada == 3:
                self.reinicializar_jogo()
                self.tela_habilitada = 2
                glutPostRedisplay()


if __name__ == '__main__':
    
    game = play()
    glutInit()
    game.init()
    glutDisplayFunc(game.clock)
    glutMouseFunc(game.mouse_inicio)
    glutKeyboardFunc(game.keyboard)
    glutSpecialFunc(game.keyboard_especiais)
    glutMainLoop()
