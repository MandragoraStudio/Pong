from Util import *

class Pelota:
    def __init__(self,juego):
        self.juego=juego
        self.vx=0.2#velocidad en el eje x
        self.vy=0 #velocidad en el eje y (no usar!! es la profundidad)
        self.vz=0.2 # velocidad en el eje z
        self.i=5
        self.modelo = juego.loader.loadModel("models/misc/sphere.egg.pz")
	self.modelo.setScale(1, 1, 1)
	self.modelo.reparentTo(juego.render)
	self.modelo.setPos(0,0,20)
        #escala la pelota
        self.modelo.setScale(self.i,self.i,self.i)
        #anande el update de la pelota al task manager
        juego.taskMgr.add(self.update,'control de la pelota', extraArgs=[self], appendTask=True)

    def update(self,unkown,task):
        self.modelo.setPos(self.modelo,self.vx,self.vy,self.vz)
	
        return task.cont
