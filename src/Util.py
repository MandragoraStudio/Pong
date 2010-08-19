#Aqui se escribiran las funciones auxiliares del programa

def lerp(self, other, factor):
        #if self.type != other.type:
        #    raise ValueError, "Mismatch in operand types \"float\" and \"byte\""
        lerped = (other - self) * factor + self
        return lerped
def signo(numero):
    if numero<0:
        return -1
    return 1
