import pygame

import rgine as rgine

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

def init_terrain(terrain_name, texture_name, is_display_mode_set=True, textureSize=32):
	terrain = rgine.Terrain("r", textureSize, textureSize)
	terrain.readTerrain(terrain_name)
	terrain.readTextureFromFile(texture_name)
	if is_display_mode_set: terrain.convert_alpha()
	return terrain

def test(property_byte, digit):
	return rgine.byte2bool(bytes([property_byte]))[digit]

def renderInitScene(screensize, pgbar):
	x, y = screensize
	screen = pygame.Surface(screensize, pygame.SRCALPHA)
	running = True
	while running:
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT:
				running = False
		screen.fill ((0,0,0))
		progressbar = pgbar.render()
		sx, sy = progressbar.get_size()
		screen.blit(progressbar,((x-sx)//2,(y-sy)//3*2))
		pgbar.increase(1)
		if pgbar.get_pos() >= 125:
			pgbar.set_pos(int("-25"))
		yield screen

def approx(a, b):
	c = a-b
	if 0.99 <= c <= 1: return True
	if -1 <= c <= -0.99: return True
	return False


class pEvent(object):
	def __init__(self, *args):
		pass

	def init(self, evt, wm):
		"""
		Will be called right after this event is activated.
		Return False will remove the event, but the release method will NOT be called.
		:rgine.Event evt:
		:rgine.windows.WindowsManager wm:
		:return bool:
		"""
		return True

	def render(self, evt, wm):
		"""
		Render the scene, if surf is None, the event will be released.
		:rgine.Event evt:
		:rgine.windows.WindowsManager wm:
		:return pygame.Surface, tuple/list(pos):
		"""
		return None, (0, 0)

	def release(self, wm):
		"""
		Release all resources.
		Note that you are responsible for relasing created windows in WindowsManager
		:rgine.windows.WindowsManager wm:
		"""
		pass


class NPC(pEvent):
	# npcs are events
	# using terrain pos ALL THE TIME
	# wm could render to screen directly
	def __init__(self, pos, res_walk):
		super(NPC, self).__init__()
		self._pos = pos
		self._res = res_walk
		self._activated = False
		self._dir = 1

	def init(self, evt, wm):
		"""
		Prepare for the activation of this event, create windows objects.
		:rgine.Event evt:
		:rgine.windows.WindowsManager wm:
		:return bool:
		"""
		return True

	def render(self, evt, wm):
		"""
		Render the scene.
		Note that this function will be called anyways, you are responsible to figure out if the event is activated.
		:rgine.Event evt:
		:rgine.windows.WindowsManager wm:
		:return pygame.Surface, tuple/list(pos)(terrain pos):
		"""
		return self._res.front[1], self._pos

	def release(self, wm):
		"""
		Prepare for the next activation of this event, cleanup.
		Note that you are responsible for destroying windows in WindowsManager
		:rgine.windows.WindowsManager wm:
		"""
		pass

	def hasEvent(self, x, y):
		if (x, y) == tuple(self._pos):
			return True
		return False

	def getPos(self):
		return self._pos

	def setPos(self, pos):
		self._pos = pos

	def isRunning(self):
		return self._activated

	def chgDir(self, dir_val):
		self._dir = dir_val

	def render_scene(self):
		if self._dir == DOWN:
			return self._res.front[1], self._pos
		elif self._dir == UP:
			return self._res.back[1], self._pos
		elif self._dir == LEFT:
			return self._res.left[1], self._pos
		elif self._dir == RIGHT:
			return self._res.right[1], self._pos
		raise ValueError(self._dir)
		

class NPC_Skeleton(NPC):
	wmacros = rgine.windows.WindowsMacros()

	def __init__(self, pos, res_walk):
		super(NPC_Skeleton, self).__init__(pos, res_walk)
		self._hWnds = {}

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			return True
		return False

	def render(self, evt, wm):
		if self._activated:
			for i in self._hWnds:
				umsg = wm.getMsg(self._hWnds[i])
		return self.render_scene()

	def release(self, wm):
		for i in self._hWnds:
			wm.DestroyWindow(self._hWnds[i])
		self._hWnds = {}
		self._activated = False


class PlayerManager(object):
		def __init__(self, player, terrain, playerEvent, npcs):
				self._player = player
				self._terrain = terrain
				self.playerEvent = playerEvent
				self.npcs = npcs
				self._evt = None
				self._wm = None

		def testTerrain(self, x, y, digit):
				prpty = self._terrain.getProperty_s(x, y)
				if prpty is None: return False
				r = test(prpty, digit)
				if r:
						return True
				else:
						return False

		def isTerrainReachable(self, x, y):
				return self.testTerrain(x, y, 0)

		def isPlayerEvent(self, x, y):
				# r = self.testTerrain(x, y, 1)
				if (x, y) in self.playerEvent:
					return self.playerEvent[(x, y)]
				else:
					return False

		def isNpcEvent(self, x, y):
				if (x, y) in self.npcs:
					return True
				else:
					return False

		def updateEvent(self, evt, wm):
				self._evt = evt
				self._wm = wm

		def update(self, x, y):
				self._player.chgDir(x, y)
				self._player.normalize_pos()
				tx, ty = self._player.getPos()
				tx += x
				ty += y
				if tx<0 or ty<0 or (not self.isTerrainReachable(int(tx), int(ty))):
					return self._player.render(self._evt), -1, False

				r = self.isNpcEvent(int(tx), int(ty))
				if r: return self._player.render(self._evt), -1, False

				r = self.isPlayerEvent(int(tx), int(ty))
				if r: return self._player.render(self._evt), r, False

				r = self._player.move(x, y)
				return self._player.render(self._evt), -1, not r

		def getPlayer(self):
			return self._player


class NPCManager(object):
	# using terrain offsets
		def __init__(self):
			self._npc = []

		def new(self, x, y, obj):
			obj.setPos((x, y))
			self._npc.append(obj)

		def update(self, terrainRect, uPos):
			for i in self._npc:
				if terrainRect.collidepoint(*i.getPos()):
					if i.hasEvent(*uPos): yield i, True
					else: yield i, False

		def delete(self, obj):
			if obj in self._npc:
				self._npc.remove(obj)
				return True
			return False

# playerEvent = {}    # pos(terrain)->tuple: pEvent/inh. class, init_args
# npcs = {}   # load these npcs before game starts
# 			# (x, y): npc_object
