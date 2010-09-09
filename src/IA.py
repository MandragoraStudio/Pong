import random
# Inteligencia artificial del pong


class IA:
    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1


    def update(self,unkown,task):
        if self.pelotahapasado():
            self.parado()
        elif self.pelotaporencima():
            #print "---------------------------------arriba"
            self.arriba()
        elif self.pelotaporabajo():
            #print "---------------------------------abajo"
            self.abajo()
        else:
            self.parado()
        return task.cont


    def abajo(self):
        self.juego.arriba2false()
        self.juego.abajo2true()

    def arriba(self):
        self.juego.abajo2false()
        self.juego.arriba2true()

    def parado(self):
        self.juego.arriba2false()
        self.juego.abajo2false()

    def pelotaporencima(self):
        #print self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ())
        #print "x: "+str(self.juego.player2.modelo.getX())
        #print "z: "+str(self.juego.player2.modelo.getZ())
        #print "x1: "+str(self.juego.player1.modelo.getX())
        #print "z1: "+str(self.juego.player1.modelo.getZ())
        #print "Jugador1: "+str(self.juego.puntos1)+" -- Jugador2: "+str(self.juego.puntos2)
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ())>0

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-45)<0

    def pelotahapasado(self):
        return self.juego.pelota.modelo.getX()-self.juego.player2.modelo.getX()>0


# Inteligencia artificial del pong
# version mejorada, mas precisa

class IA2:
    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1


    def update(self,unkown,task):
        if self.pelotahapasado():
            self.parado()
        elif self.pelotaporencima():
            #print "---------------------------------arriba"
            self.arriba()
        elif self.pelotaporabajo():
            #print "---------------------------------abajo"
            self.abajo()
        else:
            self.parado()
        return task.cont


    def abajo(self):
        self.juego.arriba2false()
        self.juego.abajo2true()

    def arriba(self):
        self.juego.abajo2false()
        self.juego.arriba2true()

    def parado(self):
        self.juego.arriba2false()
        self.juego.abajo2false()

    def pelotaporencima(self):
        #print self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ())
        #print "x: "+str(self.juego.player2.modelo.getX())
        #print "z: "+str(self.juego.player2.modelo.getZ())
        #print "x1: "+str(self.juego.player1.modelo.getX())
        #print "z1: "+str(self.juego.player1.modelo.getZ())
        #print "Jugador1: "+str(self.juego.puntos1)+" -- Jugador2: "+str(self.juego.puntos2)
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-22)>0

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-23)<0

    def pelotahapasado(self):
        return self.juego.pelota.modelo.getX()-self.juego.player2.modelo.getX()>0

class IAcabrona:

    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1
        self.i=0


    def update(self,unkown,task):
        if self.pelotahapasado():
            self.parado()
        elif self.pelotaporencima():
            #print "---------------------------------arriba"
            self.arriba()
        elif self.pelotaporabajo():
            #print "---------------------------------abajo"
            self.abajo()
        else:
            self.parado()
        #self.juego.camera.setY( self.juego.camera.getY()+ math.sin((self.i/1)))
        #self.i+=1
        #if self.i>100:
        #    i=-100
        self.juego.camera.setR(self.juego.camera.getR()+random.random()*1.5)
        return task.cont


    def abajo(self):
        self.juego.arriba2false()
        self.juego.abajo2true()

    def arriba(self):
        self.juego.abajo2false()
        self.juego.arriba2true()

    def parado(self):
        self.juego.arriba2false()
        self.juego.abajo2false()

    def pelotaporencima(self):
        #print self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ())
        #print "x: "+str(self.juego.player2.modelo.getX())
        #print "z: "+str(self.juego.player2.modelo.getZ())
        #print "x1: "+str(self.juego.player1.modelo.getX())
        #print "z1: "+str(self.juego.player1.modelo.getZ())
        #print "Jugador1: "+str(self.juego.puntos1)+" -- Jugador2: "+str(self.juego.puntos2)
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-22)>0

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-23)<0

    def pelotahapasado(self):
        return self.juego.pelota.modelo.getX()-self.juego.player2.modelo.getX()>0

