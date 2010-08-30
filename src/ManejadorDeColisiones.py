from direct.showbase import DirectObject

class ManejadorDeColisiones(DirectObject.DirectObject):
    def __init__(self,pelota):
      self.accept('pelota-into-player1', self.pelota_choca)
      #self.accept('pelota-into-player2', self.pelota_choca)
      self.pelota = pelota

    def pelota_choca(self, entry):
        """messenger.toggleVerbose()
        print messenger
        messenger.clear()
        """
        self.pelota.choca()
        print "la pelota ha chocado"
        #print entry
