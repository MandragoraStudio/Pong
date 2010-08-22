
from pandac.PandaModules import *
from Jugador import *
from direct.showbase.ShowBase import ShowBase






class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		# Disable the camera trackball controls.
		self.disableMouse()

                # Initialize the collision traverser.
                base.cTrav = CollisionTraverser()

                # Initialize the Pusher collision handler.
                pusher = CollisionHandlerPusher()

		"""
		# Load the environment model.
		self.environ = self.loader.loadModel("models/environment")
		# Reparent the model to render.
		self.environ.reparentTo(self.render)
		# Apply scale and position transforms on the model.
		self.environ.setScale(0.25, 0.25, 0.25)
		self.environ.setPos(-8, 42, 0)
		"""
		# Load and transform the panda actor.

                self.p1 = 1
                self.p2 = 1
                self.px = 1
                self.py = 0
                self.pz = 20
                self.i=5
                self.a=0
                self.abajo1 = False
                self.arriba1 = False
                self.abajo2 = False
                self.arriba2 = False


                #carga los jugadores
		self.player1 = Jugador(self)

		self.player2 = Jugador(self)

                #coloca al jugador 1
		self.player1.modelo.setR(90)
		self.player1.modelo.setPos(-130,0,20)
                # Create a collision node for this object.
                cNode = CollisionNode('player1')
		# Attach a collision sphere solid to the collision node.
                cNode.addSolid(CollisionTube(0, 0, 0, 90, 0, 0, 15))
                player1C = self.player1.modelo.attachNewNode(cNode)
                player1C.show();

                #coloca al jugador 2
		self.player2.modelo.setR(90)
		self.player2.modelo.setPos(170,0,20)
                # Create a collision node for this object.
                cNode = CollisionNode('player2')
                # Attach a collision sphere solid to the collision node.
                cNode.addSolid(CollisionTube(0, 0, 0, 90, 0, 0, 15))
                player2C = self.player2.modelo.attachNewNode(cNode)
                player2C.show();

                #inicia y coloca pelota
                self.pelota = self.loader.loadModel("models/misc/sphere.egg.pz")
		self.pelota.setScale(1, 1, 1)
		self.pelota.reparentTo(self.render)
		self.pelota.setPos(0,0,20)

                # Create a collision node for this object.
                cNode = CollisionNode('pelota')
                # Attach a collision sphere solid to the collision node.
                cNode.addSolid(CollisionSphere(0, 0, 0, 1.5))
                pelotaC = self.pelota.attachNewNode(cNode)

                base.cTrav.addCollider(pelotaC, pusher)
                pusher.addCollider(pelotaC, self.pelota, base.drive.node())

                #coloca la camara
		self.camera.setPos(20,-500,-20)
	
		dlight = DirectionalLight('my dlight')
		dlnp = render.attachNewNode(dlight)
		dlnp.setHpr(20, 20, 0)
		render.setLight(dlnp)
	
		dlight2 = DirectionalLight('my dlight2')
		dlight2.setColor(Vec4(0.2, 0.2, 0.2, 0.1))
		dlnp2 = render.attachNewNode(dlight2)
		dlnp2.setHpr(180, -20, 0)
		render.setLight(dlnp2)
		
		"""
		global polvo
		polvo = ParticleEffect()
		polvo.loadConfig(Filename('dust.ptf'))
		polvo.start()
		polvo.setPos(3.000, 0.000, 2.250)
		"""
	
		self.accept('w',arriba1true,[self])
		self.accept('w-up',arriba1false,[self])
		self.accept('s',abajo1true,[self])
		self.accept('s-up',abajo1false,[self])
		self.accept('o',arriba2true,[self])
		self.accept('o-up',arriba2false,[self])
		self.accept('l',abajo2true,[self])
		self.accept('l-up',abajo2false,[self])
		#self.taskMgr.add(player1c,'control del jugador 1', extraArgs=[self], appendTask=True)
		#self.taskMgr.add(player2c,'control del jugador 2', extraArgs=[self], appendTask=True)
		self.taskMgr.add(pelotac,'control de la pelota', extraArgs=[self], appendTask=True)


def pelotac(self,task):
	self.pelota.setPos(self.px,self.py,self.pz)
	self.px = self.px + 1
	if self.px > 100:
		self.px = -100
	self.pelota.setScale(self.i,self.i,self.i)

        #self.pelota.setR(self.a)
        #self.a+=50
        #if self.a>360:
        #    self.a=0
	#self.i+=0.1
	return task.cont
def arriba1true(self):
	self.player1.arriba= True
def arriba1false(self):
	self.player1.arriba= False
def abajo1true(self):
	self.player1.abajo= True
def abajo1false(self):
	self.player1.abajo= False
def arriba2true(self):
	self.player2.arriba= True
def arriba2false(self):
	self.player2.arriba= False
def abajo2true(self):
	self.player2.abajo= True
def abajo2false(self):
	self.player2.abajo= False

 
app = MyApp()
app.run()