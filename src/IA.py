# Inteligencia artificial del pong

class IA:
    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1


    def update(self,unkown,task):
        if self.pelotaporencima():
            print "---------------------------------arriba"
            self.arriba()
        elif self.pelotaporabajo():
            print "---------------------------------abajo"
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
        print self.juego.pelota.modelo.getZ()-21
        print self.juego.player2.modelo.getX()-170
        return self.juego.pelota.modelo.getZ()-21>self.juego.player2.modelo.getX()-160

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-21<self.juego.player2.modelo.getX()-160


