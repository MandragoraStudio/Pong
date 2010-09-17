from direct.showbase import DirectObject
from pandac.PandaModules import *
class ManejadorDeColisiones(DirectObject.DirectObject):
    def __init__(self,juego):
        
        self.juego = juego


        # Initialize the collision traverser.
        base.cTrav = CollisionTraverser()
        # Initialize the Pusher collision handler.
        pusher = CollisionHandlerPusher()
        pusher.addInPattern('pelota-again-player1')
        #pusher.addInPattern('pelota-into-player2')

        # Create a collision node for this object.
        cNode = CollisionNode('player1')
        # Attach a collision sphere solid to the collision node.
        cNode.addSolid(CollisionTube(0, 0, 0, 0, 0, 0, 0))
        player1C = self.juego.player1.modelo.attachNewNode(cNode)
        #player1C.show()

        # Create a collision node for this object.
        cNode = CollisionNode('player2')

        # Attach a collision sphere solid to the collision node.
        cNode.addSolid(CollisionTube(0, 0, 0, 0, 0, 0, 0))
        player2C = self.juego.player2.modelo.attachNewNode(cNode)
        player2C.show()

        # Create a collision node for this object.
        cNode = CollisionNode('pelota')
        # Attach a collision sphere solid to the collision node.
        cNode.addSolid(CollisionSphere(0, 0, 0, 37.0))
        pelotaC = self.juego.pelota.modelo.attachNewNode(cNode)
        pelotaC.show()

        base.cTrav.addCollider(pelotaC, pusher)
        pusher.addCollider(pelotaC, self.juego.pelota.modelo, base.drive.node())



        self.accept('pelota-again-player1', self.pelota_choca)
        #self.accept('pelota-into-player2', self.pelota_choca)

    def pelota_choca(self, entry):
        """messenger.toggleVerbose()
        print messenger
        messenger.clear()
        """
        self.juego.pelota.choca()
        #print "la pelota ha chocado"
        #print entry
