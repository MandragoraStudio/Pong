
from pandac.PandaModules import TextNode

class Marcador:
    def __init__(self,juego):

        self.juego=juego

        self.puntuacion1 = TextNode('puntuacion1')
        self.puntuacion1.setText(str(self.juego.puntos1))
        nodo1 = self.juego.aspect2d.attachNewNode(self.puntuacion1)
        nodo1.setScale(0.1)
        nodo1.setPos(-0.5,0, 0.7)
        #nodo1.setPos(-0.5,-0.5)

        self.puntuacion2= TextNode('puntuacion1')
        self.puntuacion2.setText(str(self.juego.puntos2))
        nodo2 = self.juego.aspect2d.attachNewNode(self.puntuacion2)
        nodo2.setScale(0.1)
        nodo2.setPos(0.5,0,0.7)

    def update(self):
        self.puntuacion1.setText(str(self.juego.puntos1))
        self.puntuacion2.setText(str(self.juego.puntos2))





