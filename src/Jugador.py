from Util import *

class Jugador:
    #clase jugador

    def __init__(self,juego,humano=True):
        self.bordesuperior=100
        self.bordeinferior=-100
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
        paso=0.5
	if self.arriba:
            self.vx-=paso
	if self.abajo:
            self.vx+=paso
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)
        #rozamiento=0.2
        #self.vx=lerp(self.vx,0,rozamiento)
        rozamiento = 0.15
        max = 4
        self.vx-=rozamiento*signo(self.vx)
        if (self.vx*signo(self.vx)<rozamiento*2):
            self.vx=0
        if self.vx>max:
            self.vx=max
        if self.vx<-max:
            self.vx=-max
        if self.modelo.getZ()>self.bordesuperior:
            self.modelo.setZ(self.bordesuperior)
        if self.modelo.getZ()<self.bordeinferior:
            self.modelo.setZ(self.bordeinferior)
	return task.cont