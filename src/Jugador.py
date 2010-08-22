from Util import *

class Jugador:
    #clase jugador

    def __init__(self,juego,humano=True):
        #inicializa variables
        self.bordesuperior=100
        self.bordeinferior=-100
        self.arriba=False
        self.abajo=False
        self.juego=juego
        self.vx=0
        self.vy=0
        self.vz=0

        #carga el modelo
        self.modelo = juego.loader.loadModel("barra")
	self.modelo.setScale(0.5, 0.5, 0.5)
	self.modelo.reparentTo(juego.render)

        #agrega el control del jugador al task manager
        juego.taskMgr.add(self.update,'control del jugador', extraArgs=[self], appendTask=True)

    def update(self,unknown,task):
        #update, aqui se actualiza la posicion del jugador asi como sus variables (velocidad principalmente por ahora)
        paso=0.5 #aceleracion
        #cambiando la velocidad
	if self.arriba:
            self.vx-=paso
	if self.abajo:
            self.vx+=paso
        #moviendo el modelo
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)
        #rozamiento=0.2
        #self.vx=lerp(self.vx,0,rozamiento)
        rozamiento = 0.15
        max = 4
        #aplicando rozamiento
        self.vx-=rozamiento*signo(self.vx)
        if (self.vx*signo(self.vx)<rozamiento*2):
            self.vx=0
        #velocidades maximas
        if self.vx>max:
            self.vx=max
        if self.vx<-max:
            self.vx=-max
        #chocando contra el borde del campo
        if self.modelo.getZ()>self.bordesuperior:
            self.modelo.setZ(self.bordesuperior)
        if self.modelo.getZ()<self.bordeinferior:
            self.modelo.setZ(self.bordeinferior)
	return task.cont