import random
# Inteligencia artificial del pong, necesita mejora con herencia de clases


class IA:
    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1


    def update(self,unkown,task):
        #miramos si la pelota ha pasado del rango de accion de la IA
        if self.pelotahapasado():
            #si se le ha pasado la pelota se para
            self.parado()
        #miramos si la pelota esta por encima y si esta vamos a por ella
        elif self.pelotaporencima():
            self.arriba()
        #miramos si la pelota esta por encima y si esta vamos a por ella
        elif self.pelotaporabajo():
            self.abajo()
        else:
            self.parado()
        return task.cont


    def abajo(self):
        #dejamos de subir
        self.juego.arriba2false()
        #empezamos a bajar
        self.juego.abajo2true()

    def arriba(self):
        #dejamos de bajar
        self.juego.abajo2false()
        #empezamos a subir
        self.juego.arriba2true()

    def parado(self):
        #dejamos de subir y de bajar
        self.juego.arriba2false()
        self.juego.abajo2false()

    def pelotaporencima(self):
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
            self.arriba()
        elif self.pelotaporabajo():
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
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-22)>0

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-23)<0

    def pelotahapasado(self):
        return self.juego.pelota.modelo.getX()-self.juego.player2.modelo.getX()>0

# version mejorada, mas precisa. Version lavadora.
class IAcabrona:

    def __init__(self,juego):
        self.juego=juego
        self.dificultad=1
        self.i=0


    def update(self,unkown,task):
        if self.pelotahapasado():
            self.parado()
        elif self.pelotaporencima():
            self.arriba()
        elif self.pelotaporabajo():
            self.abajo()
        else:
            self.parado()

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
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-22)>0

    def pelotaporabajo(self):
        return self.juego.pelota.modelo.getZ()-(self.juego.player2.modelo.getZ()-23)<0

    def pelotahapasado(self):
        return self.juego.pelota.modelo.getX()-self.juego.player2.modelo.getX()>0

