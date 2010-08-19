from Util import *

class Jugador:
    #clase jugador

    def __init__(self,juego):
        self.arriba=False
        self.abajo=False
        self.juego=juego
        self.modelo = juego.loader.loadModel("barra")
	self.modelo.setScale(0.5, 0.5, 0.5)
	self.modelo.reparentTo(juego.render)
        self.vx=0
        self.vy=0
        self.vz=0
        juego.taskMgr.add(self.update,'control del jugador', extraArgs=[self], appendTask=True)

    def update(self,unknown,task):
	if self.arriba:
            self.vx-=1
	if self.abajo:
            self.vx+=1
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)
        rozamiento=0.3
        self.vx=lerp(self.vx,0,rozamiento)
	return task.cont