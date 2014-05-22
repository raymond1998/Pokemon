from basics import *

__author__ = 'Charles-Jianye Chen'

class uiBackpack(rgine.windows.windowBase):
	pass

class Backpack(pEvent):
	def __init__(self, *args):
		super(Backpack, self).__init__(*args)
		self.player = None

	def setPlayer(self, player):
		self.player = player

	def init(self, evt, wm):
		if self.player is None: raise ValueError(self.player)
		return True

	def render(self, evt, wm):
		return None, (0, 0)

	def release(self, wm):
		pass