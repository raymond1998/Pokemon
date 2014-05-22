from basics import *

__author__ = 'Charles-Jianye Chen'

import sys
path = sys.path[0]
if not path: path = sys.path[1]
_backpack_bk = rgine.surface_buffer.read_buffer(path+"/resources/backpack", 2560, 1600)

class uiBackpack(rgine.windows.windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(uiBackpack, self).__init__(wsize, winbk)
		self.setRenderArgs(*args)

		self.player = self._args[0]
		self._handle = 0
		self._surface = pygame.Surface(wsize, pygame.SRCALPHA)
		self._surface.blit(self._bk, (0, 0))
		self._surf = None
		self._state = 0

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0

		return True

	def callback(self, evt, uMsg):
		self._surf = self._surface.copy()
		if evt.isKeyHit(pygame.K_9):
			return False

		for hWnd, msg, surface, pos in self._wm.DispatchMessage(evt):
			self._surf.blit(surface, pos)

		return True

	def render(self):
		return self._surf

	def release(self):
		self._wm.Release()

	def getMsg(self):
		return self._state


class Backpack(pEvent):
	def __init__(self, *args):
		super(Backpack, self).__init__(*args)
		self.player = args[1]
		self._ui = 0
		self._surf = pygame.Surface((0, 0))
		self._uiClass = args[0].RegisterCompleteClass(uiBackpack)

	def setPlayer(self, player):
		self.player = player

	def init(self, evt, wm):
		if not self._activated:
			if self.player is None: raise ValueError(self.player)
			self._ui = wm.CreateWindow(self._uiClass,
			                           (wm.screensize, pygame.transform.scale(_backpack_bk, wm.screensize),
			                            self.player))
			self._activated = True
			return True
		else:
			return False

	def render(self, evt, wm):
		if self._activated:
			if wm.getInstance(self._ui) is None:
				self.release(wm)
			else:
				umsg = wm.getMsg(self._ui)
				return self._surf, umsg
		return None, None

	def release(self, wm):
		wm.DestroyWindow(self._ui)
		self._ui = 0
		self._activated = False