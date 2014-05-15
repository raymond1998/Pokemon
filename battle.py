from basics import *
from resources_loader import *
__author__ = 'Charles-Jianye Chen'

class choice1(object):
	def init(self, hWnd):
		self.wmacros = rgine.windows.WindowsMacros()
		self._handle = hWnd
		self._umsg = 0
		self._hasresult = False
		x, y, w, h = self.getRect()
		self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
		self._buttons = {0: "ATTACK", 1: "SKILLS", 2:"BACKPACK", 3:"ESCAPE"}
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize

		button_size = self.wmacros.button_size[0]//2, self.wmacros.button_size[1]//2
		button_surf = pygame.transform.scale(self.wmacros.button.copy(), button_size)
		pygame.draw.rect(button_surf, (0, 0, 0), button_surf.get_rect(), 1)

		t_handles = []
		for i in self._buttons:
			h = self._wm.CreateWindow(self.wmacros.WC_BUTTON,
							    (button_size, button_surf, "%s"%self._buttons[i],
												pygame.font.SysFont('Times New Romen', 16),
												True, (255, 255, 255)), True)
			t_handles.append(h)
			self._hWnds[h] = i

		tx, ty = ((x//2)-button_size[0])//2, ((y//2)-button_size[1])//2
		self._wm.MoveWindowToPos(t_handles[0], tx, ty)
		self._wm.MoveWindowToPos(t_handles[1], tx+x//2, ty)
		self._wm.MoveWindowToPos(t_handles[2], tx, ty+y//2)
		self._wm.MoveWindowToPos(t_handles[3], tx+x//2, ty+y//2)
		return True

	def cb(self, event, uMsg):
		self._bk_.fill((255, 255, 255, 255//2))
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
			self._bk_.blit(surface, pos)
			if msg == self.wmacros.HIT and hWnd in self._hWnds:
				self._umsg = self._hWnds[hWnd]
				self._hasresult = True
		return True

	def rd(self):
		return self._bk_

	def getMsg(self):
		"""
		:return (bHasResult, msg):
		"""
		if self._hasresult:
			self._hasresult = False
			return True, self._umsg
		return False, self._umsg

	def rel(self):
		self._wm.Release()


class choice2(choice1):
	def init(self, hWnd):
		self.wmacros = rgine.windows.WindowsMacros()
		self._handle = hWnd
		self._umsg = 0
		self._hasresult = False
		x, y, w, h = self.getRect()
		self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
		self._buttons = {0: "Skill 0", 1: "Skill 1", 2:"Skill 2", 3:"Skill 3"}
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize

		button_size = self.wmacros.button_size[0]//2, self.wmacros.button_size[1]//2
		button_surf = pygame.transform.scale(self.wmacros.button.copy(), button_size)
		pygame.draw.rect(button_surf, (0, 0, 0), button_surf.get_rect(), 1)

		t_handles = []
		for i in self._buttons:
			h = self._wm.CreateWindow(self.wmacros.WC_BUTTON,
							    (button_size, button_surf, "%s"%self._buttons[i],
												pygame.font.SysFont('Times New Romen', 16),
												True, (255, 255, 255)), True)
			t_handles.append(h)
			self._hWnds[h] = i

		tx, ty = ((x//2)-button_size[0])//2, ((y//2)-button_size[1])//2
		self._wm.MoveWindowToPos(t_handles[0], tx, ty)
		self._wm.MoveWindowToPos(t_handles[1], tx+x//2, ty)
		self._wm.MoveWindowToPos(t_handles[2], tx, ty+y//2)
		self._wm.MoveWindowToPos(t_handles[3], tx+x//2, ty+y//2)
		return True

	def cb(self, event, uMsg):
		self._bk_.fill((255, 255, 255, 255//2))
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
			self._bk_.blit(surface, pos)
			if msg == self.wmacros.HIT and hWnd in self._hWnds:
				self._umsg = self._hWnds[hWnd]
				self._hasresult = True
		return True


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

				def c_choice1(self):
					winsize = 16*12, 16*8
					self._hWnds["choice1"] = self._wm.CreateWindow(
						self._wm.RegisterClass(False, choice1.init, choice1.cb, choice1.rd, choice1.getMsg, choice1.rel),
						(winsize, None)
						)
					x, y = self._wm.screensize
					self._wm.MoveWindow(self._hWnds["choice1"], (x-winsize[0])*9.5//10, (y-winsize[1])*9.5//10)

				self._init_choice1 = c_choice1
				def c_choice2(self):
					winsize = 16*30, 16*8
					self._hWnds["choice2"] = self._wm.CreateWindow(
						self._wm.RegisterClass(False, choice2.init, choice2.cb, choice2.rd, choice2.getMsg, choice2.rel),
						(winsize, None)
						)

					x, y = self._wm.screensize
					self._wm.MoveWindow(self._hWnds["choice2"], (x-winsize[0])*1//10, (y-winsize[1])*9.5//10)

				self._init_choice2 = c_choice2
				# self._wm.SetTopmost(self._hWnds["choice1"], True)

				self._hWnds["choice1"] = 0
				self._hWnds["choice2"] = 0

				self._init_choice1(self)
				return True


			def cb(self, event, uMsg):
				self._bk_.fill((150, 150, 150, 255//2))
				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
					if hWnd  == self._hWnds["choice1"]:
						r, msg = msg
						if not r: continue
						if msg == 0:
							self._wm.DestroyWindow(self._hWnds["choice1"])
						elif msg == 1:
							self._init_choice2(self)
							self._wm.SetTopmost(self._hWnds["choice2"], True)
						elif msg == 2:
							pass
						elif msg == 3:
							pass
					if hWnd == self._hWnds["choice2"]:
						r, msg = msg
						if not r: continue
						if msg == 0:
							pass
						elif msg == 1:
							pass
						elif msg == 2:
							pass
						elif msg == 3:
							pass
						self._wm.DestroyWindow(self._hWnds["choice1"])
						self._wm.DestroyWindow(self._hWnds["choice2"])
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
