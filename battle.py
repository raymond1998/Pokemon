from basics import *
from resources_loader import *
__author__ = 'Charles-Jianye Chen'

class Battle(pEvent):
	def __init__(self):
		super(Battle, self).__init__()
		self._scene = -1
		self._activated = False
		self._hWnds = {}

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			
			def init(self, hWnd):
				self.wmacros = rgine.windows.WindowsMacros()
				self._handle = hWnd
				self._umsg = 0
				w, h = self._size
				self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
				self._hWnds = {}

				def init(self, hWnd):
					self.wmacros = rgine.windows.WindowsMacros()
					self._handle = hWnd
					self._umsg = 0
					x, y, w, h = self.getRect()
					self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
					return True

				def cb(self, event, uMsg):
					self._bk_.fill((255, 255, 255, 255//2))
					for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
						self._bk_.blit(surface, pos)
					return True

				def rd(self):
					return self._bk_

				def getMsg(self):
					return self._umsg

				def rel(self):
					self._wm.Release()

				winsize = 9*10, 16*8
				self._hWnds["choice1"] = self._wm.CreateWindow(
					self._wm.RegisterClass(False, init, cb, rd, getMsg, rel), (winsize, None)
					)
				x, y = self._wm.screensize
				self._wm.MoveWindow(self._hWnds["choice1"], (x-winsize[0])*9//10, (y-winsize[1])*9.5//10)
				
				
				winsize = 16*30, 16*8
				self._hWnds["choice2"] = self._wm.CreateWindow(
					self._wm.RegisterClass(False, init, cb, rd, getMsg, rel), (winsize, None)
					)

				x, y = self._wm.screensize
				self._wm.MoveWindow(self._hWnds["choice2"], (x-winsize[0])*1//10, (y-winsize[1])*9.5//10)

				return True

			def cb(self, event, uMsg):
				self._bk_.fill((150, 150, 150, 255//2))
				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
				return True

			def rd(self):
				return self._bk_

			def getMsg(self):
				return self._umsg

			def rel(self):
				self._wm.Release()

			winsize = wm.screensize
			self._scene = wm.CreateWindow(
				wm.RegisterClass(False, init, cb, rd, getMsg, rel), (winsize, None)
				)
			x, y = wm.screensize
			wm.MoveWindow(self._scene, (x-winsize[0])//2, (y-winsize[1])//2)
			
			return True
		return False

	def render(self, evt, wm):
		if self._activated:
			umsg = wm.getMsg(self._scene)
			return None, umsg
		return None, None

	def release(self, wm):
		wm.DestroyWindow(self._scene)
		self._scene = -1
		self._activated = False
