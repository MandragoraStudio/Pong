from Util import *
from direct.actor.Actor import Actor
#NOTA: debido a un cambio de coordenadas, la vx mueve al jugador en el eje Z
#esto es debido a que aunque la vx se aplica al movimiento en el eje X, este esta hecho tomando como referencia el modelo, que esta girado 90 grados
class Jugador:
    #clase jugador

    def __init__(self,juego,humano=True):
        #inicializa variables
        self.bordesuperior=80
        self.bordeinferior=-120
        self.arriba=False
        self.abajo=False
        self.juego=juego
        self.vx=0
        self.vy=0
        self.vz=0
        self.humano=humano
        
        #carga el modelo
        
        #self.modelo = Actor("Modelos/barra",{"animacion": "Modelos/barraAni"})
        self.modelo = juego.loader.loadModel("Modelos/barra")
	self.modelo.setScale(10, 10, 15)
	self.modelo.reparentTo(juego.render)

        #agrega el update del jugador al task manager
        juego.taskMgr.add(self.update,'control del jugador', extraArgs=[self], appendTask=True)

    def update(self,unknown,task):
        #IMPORTANTE
        #modificador de velocidad, si te parece que los jugadores van rapido o lento
        #toca solo este valor
        modificadorvelocidad=2
        #update, aqui se actualiza la posicion del jugador asi como sus variables (velocidad principalmente por ahora)
        paso=0.03*modificadorvelocidad #aceleracion
        #cambiando la velocidad
	if self.arriba:
            self.vx-=paso
	if self.abajo:
            self.vx+=paso
        #moviendo el modelo
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)
        #rozamiento=0.2
        #self.vx=lerp(self.vx,0,rozamiento)
        rozamiento = 0.007*modificadorvelocidad
        max = 0.1*modificadorvelocidad
        #aplicando rozamiento
        self.vx-=rozamiento*signo(self.vx)
        if (self.vx*signo(self.vx)<rozamiento *2):
            self.vx=0
        #velocidades maximas
        if self.vx>max:
            self.vx=max
        if self.vx<-max:
            self.vx=- max
        #chocando contra el borde del campo
        if self.modelo.getZ()>self.bordesuperior:
            self.vx=0
            self.modelo.setZ(self.bordesuperior)
        if self.modelo.getZ()<self.bordeinferior:
            self.vx=0
            self.modelo.setZ(self.bordeinferior)
	return task.cont