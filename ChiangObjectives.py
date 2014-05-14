import random
import time

from pygame import *

from resources_loader import *




_CURRENT_ID = 0
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

TYPE_PLAYER = 0
TYPE_NPC = 1

_res = {}
screen = display.set_mode((1,1))
t=res_walk(pygame.image.load("pic1.png").convert_alpha(),3,4,FRONT_LEFT_RIGHT_BACK)
_res["name"] = t[0]
display.quit()

class _object(object):
	def __init__(self, typ, name):
		self._type = typ
		self._name = name

		self._res = _res[name]
		#Surfaces of picture

		self._pos = [0, 0]
		self._endframe = 1
		self._frame_count = self._endframe
		self._di = DOWN
		self.lastcall = time.clock()
		self.lastcall_pos = time.clock()
		self._walking = False
		self._poschg = []
		self._endpos = self._pos[:]

	def getPos(self):
		return self._pos

	def getDirection(self):
		return self._di

	def normalize_pos(self):
		x, y = self._pos
		if 0.99 < x-int(x) < 1:
			x = int(x) + 1
		if 0.99 < y-int(y) < 1:
			y = int(y) + 1
		self._pos = [x, y]

	def render(self, evt):
		chg = time.clock()-self.lastcall
		di = self._di

		if self._walking:
			# if time.clock()-self.lastcall_pos > 1/3/10/32:
			# 	self.lastcall_pos = time.clock()
			# 	self._pos[0] += self._poschg[0]*3/32
			# 	self._pos[1] += self._poschg[1]*3/32
			if chg > 1/3/10:    # 1/3/6 is good for slow speed
				self.lastcall = time.clock()
				# self.lastcall_pos = time.clock()
				self._pos[0] += self._poschg[0]
				self._pos[1] += self._poschg[1]
				self._frame_count+=1
				if self._frame_count == len(self._res.left): self._frame_count=0
				if self._frame_count == self._endframe:
					self._walking = False
					self._pos = self._endpos[:]

		if di == UP:
			return(self._res.back[self._frame_count]), self._pos

		elif di == LEFT:
			return(self._res.left[self._frame_count]), self._pos

		elif di == DOWN:
			return(self._res.front[self._frame_count]), self._pos

		elif di == RIGHT:
			return(self._res.right[self._frame_count]), self._pos

	def move(self, x, y):
		if self._walking or x==y==0: return False

		self._walking = True
		self.lastcall = time.clock()
		self.lastcall_pos = time.clock()

		self._poschg = [x/3, y/3]
		self._endpos = self._pos[0]+x, self._pos[1]+y

		return True

	def chgDir(self, x, y):
		if self._walking: return
		if x<0:
			self._di=LEFT
		if x>0:
			self._di=RIGHT
		if y<0:
			self._di=UP
		if y>0:
			self._di=DOWN

	def setPos(self, x, y):
		self._pos = [x, y]
		self._endpos = [x, y]

	def release(self):
		pass


class Character(_object):
	def __init__(self,name,typ,level):
		self._level=level
		super(Character, self).__init__(typ, name)

	def update(self, evt, wm):
##        if
##            x=Surface((800,600))
##            x.blit(self.update_(evtid), (0, 0))
##                return x
##            if evt.isMouseHit and evt.getMousePos()== :
		return False

		#msgloop
		#in the msgloop
		#you call
		#self.update_(evtid)
		#which should be overwritten by its subclasses



	def update_(self, evtid):
		pass

class Pokemon(Character):
	def __init__(self,name,typ,level):
		super(Pokemon, self).__init__(name, typ, level)
		self.hp =100
		self.A1 = ["attack",[0,10],5,2]

	def defence(self,pokemon):
		dmgDealt=int(pokemon.A1[1][random.randint[pokemon.A1[1][0]:pokemon.A1[1][-1]]])*pokemon.A1[3]
		self.hp=self.hp-dmgDelt
		return self.hp

	def isAlive(hp):
		if hp==0:
			return False
		else:
			return True

class Player(Character):
	def __init__(self,pokemons,items,name,level):
		global _CURRENT_ID
		super(Player, self).__init__(name, TYPE_PLAYER, level)
		self.id = _CURRENT_ID
		_CURRENT_ID += 1
		self.pokemon=[]
		self.backpack=[]

		for pokemon in pokemons:
			self.pokemon.append(pokemons)
		for item in items:
			self.backpack.append(item)
	def addItem(item):
		self.backpack.append(item)
	def delItem(item):
		self.backpack.remove(item)

class NPC(Character):
	def __init__(self,pos,pokemons,name,level):
		super(NPC, self).__init__(name, TYPE_NPC, level)
		self.pokemon=[]
		for pokemon in pokemons:
			self.pokemon.append(pokemon)
		self._NPCTalk=0
		self._NPCEVENT=False

		def npcTalk(self):
			if self.NPCEVENT:
				self._NPCTALK+=1
				self.NPCEVENT=False

		def npcText(self):
			pass


player = Player([], [], "name", 0)
player.setPos(0, 10)
