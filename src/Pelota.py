from Util import *
import random

class Pelota:
    def __init__(self,juego):
        self.juego=juego
        
        self.i=0.15
        self.modelo = juego.loader.loadModel("pelota")
	self.modelo.reparentTo(juego.render)
        #escala la pelota
        self.modelo.setScale(self.i,self.i,self.i)
        #coloca la pelota e inicia las variables
        self.start()
        #anande el update de la pelota al task manager
        juego.taskMgr.add(self.update,'control de la pelota', extraArgs=[self], appendTask=True)

    def choca(self):
        self.juego.golpe.play()
        self.vx*=-1

        #comprueba contra que jugador
        self.jugador=self.juego.player1
        if self.modelo.getX()>0:
            self.jugador=self.juego.player2
        #impulso vertical dado a la pelota por el jugador
        self.vz=self.vz-(self.jugador.vx/20)
        #aceleracion horizontal de la pelota con cada choque
        self.vx+=0.01*signo(self.vx)

    def update(self,unkown,task):
        #movimiento de la pelota
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)

        #colision de la pelota contra los bordes superiores e inferiores
	if (self.modelo.getZ()+25)*signo(self.modelo.getZ())>120:
            self.vz*=-1

        if (self.modelo.getX()<-160):
            self.juego.puntojugador2()
            self.juego.gol.play()

        if self.modelo.getX()>200:
            self.juego.puntojugador1()
            self.juego.gol.play()


        return task.cont

    def start(self):
        self.vx=(12+random.random()*10)*(signo(random.random()-0.5))#velocidad en el eje x
        self.vy=0 #velocidad en el eje y (no usar!! es la profundidad)
        self.vz=(12+random.random()*10)*(signo(random.random()-0.5)) # velocidad en el eje z
	self.modelo.setPos(0,0,20)
        self.juego.marcador.update()

