
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


        self.victoria= TextNode('victoria')
        self.victoria.setText("")
        #self.victoria.setWordwrap(7.0)
        nodo3 = self.juego.aspect2d.attachNewNode(self.victoria)
        nodo3.setScale(0.2)
        nodo3.setPos(-1.1,0,0)

        self.jugando=True

    def update(self):
        if self.jugando:
            self.puntuacion1.setText(str(self.juego.puntos1))
            self.puntuacion2.setText(str(self.juego.puntos2))
            if self.juego.puntos1>9:
                self.gana(1)
            if self.juego.puntos2>0:
                self.gana(2)

    def gana(self,quien):
        cadena="El jugador "+str(quien)+" ha vencido!!"
        self.juego.sonidovictoria.play()
        self.victoria.setText(cadena)
        self.juego.taskMgr.remove("control del jugador")
        self.jugando=False



