# Inteligencia artificial del pong

class IA:
    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1


    def update(self,unkown,task):
        if self.pelotaporencima():
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


