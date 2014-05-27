from basics import *
from resources_loader import *

__author__ = 'Charles-Jianye Chen'

import sys
path = sys.path[0]
if not path: path = sys.path[1]
_battle_bk = rgine.surface_buffer.read_buffer(path+"/resources/battle", 1920, 1200)

ATK = 1
DEF = 2

class choice1(object):
	def init(self, hWnd):
		self.wmacros = rgine.windows.WindowsMacros()
		self._handle = hWnd
		self._umsg = 0
		self._hasresult = False
		x, y, w, h = self.getRect()
		self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
		self._buttons = {0: "ATTACK", 1: "BAG", 2:"POKEMON", 3:"RUN"}
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize

		button_size = self.wmacros.button_size[0]//2, self.wmacros.button_size[1]//2
		button_surf = pygame.transform.scale(self.wmacros.button.copy(), button_size)
		pygame.draw.rect(button_surf, (0, 0, 0), button_surf.get_rect(), 1)

		t_handles = []
		k = list(self._buttons.keys())
		k.sort()
		for i in k:
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
		self._buttons = self._args[0]
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize

		button_size = self.wmacros.button_size[0]*2//3, self.wmacros.button_size[1]*2//3
		button_surf = pygame.transform.scale(self.wmacros.button.copy(), button_size)
		pygame.draw.rect(button_surf, (0, 0, 0), button_surf.get_rect(), 1)

		t_handles = []
		for i in range(len(self._buttons)):
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
		if event.isKeyHit(pygame.K_ESCAPE):
			self._umsg = -1
			self._hasresult = True
			return True
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
			self._bk_.blit(surface, pos)
			if msg == self.wmacros.HIT and hWnd in self._hWnds:
				self._umsg = self._hWnds[hWnd]
				self._hasresult = True
		return True


class uiStatus(choice1):
	def init(self, hWnd):
		self.wmacros = rgine.windows.WindowsMacros()
		self._handle = hWnd
		self._umsg = 0
		self._hasresult = False
		x, y, w, h = self.getRect()
		self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
		# self._buttons = self._args[0]
		self._owner = self._args[0]
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize
		px, py = 100, 25
		self._pgbar_hp = rgine.Progressbar((px, py), (255, 0, 0), 5, 0, 0)
		self._render_pgbar_hp = lambda pgbar: (pgbar.render(), ((x-px)//2, (y-py)*5//10))
		px, py = 100, 10
		self._pgbar_exp = rgine.Progressbar((px, py), (0, 255, 0), 5, 0, 0)
		self._render_pgbar_exp = lambda pgbar: (pgbar.render(), ((x-px)//2, (y-py)*9//10))
		self._ft = pygame.font.SysFont('Times New Romen', 16)
		return True

	def cb(self, event, uMsg):
		return True

	def rd(self):
		self._bk_.fill((255, 255, 255, 255//2))
		self._pgbar_hp.set_pos(self._owner.get_hp_percentage())
		self._pgbar_exp.set_pos(self._owner.get_exp_percentage())
		print("hp percentage:", self._owner.get_hp_percentage(), "%",
		      "hp:", self._owner.getHP(),
		      "pokemon id:", self._owner.getID())
		# for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
		# 	self._bk_.blit(surface, pos)

		self._bk_.blit(*self._render_pgbar_hp(self._pgbar_hp))
		self._bk_.blit(*self._render_pgbar_exp(self._pgbar_exp))
		self._bk_.blit(
			self._ft.render(self._owner.getName()+"  Lv. %d"%self._owner.get_level(), True, (255, 255, 255)),
			(0, 0),
		)
		return self._bk_


class Battle(pEvent):
	def __init__(self, backpack, wm):
		super(Battle, self).__init__()
		self._scene = -1
		self._activated = False
		self._hWnds = {}
		self._atk = None
		self._def = None
		self._backpack = backpack
		self._g_wm = wm

	def setFightingObjects(self, atk, defense):
		if atk is not None: self._atk = atk
		if defense is not None: self._def = defense

	def init(self, evt, wm):
		if not self._activated:
			atk, defense = self._atk, self._def
			backpack = self._backpack
			wm = self._g_wm
			#if atk is None or defense is None: raise ValueError((atk, defense))
			self._activated = True

			def init(self, hWnd):
				nonlocal atk, defense, backpack, wm
				self.wmacros = rgine.windows.WindowsMacros()
				self._handle = hWnd
				self._umsg = 0
				w, h = self._size
				self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
				self._hWnds = {}

				self._atk = atk
				self._def = defense
				self._backpack = backpack
				self._backpack_mode = 0
				self._g_wm = wm

				winsize = 16*10, 9*10
				self._hWnds["uistatus_atk"] = self._wm.CreateWindow(
					self._wm.RegisterClass(False, uiStatus.init, uiStatus.cb, uiStatus.rd, uiStatus.getMsg, uiStatus.rel),
					(winsize, None, self._atk)
					)

				x, y = self._wm.screensize
				# self._wm.MoveWindow(self._hWnds["uistatus_atk"], 0, y-winsize[1])
				self._wm.MoveWindow(self._hWnds["uistatus_atk"], 0, 0)

				winsize = 16*10, 9*10
				self._hWnds["uistatus_def"] = self._wm.CreateWindow(
					self._wm.RegisterClass(False, uiStatus.init, uiStatus.cb, uiStatus.rd, uiStatus.getMsg, uiStatus.rel),
					(winsize, None, self._def)
					)

				x, y = self._wm.screensize
				self._wm.MoveWindow(self._hWnds["uistatus_def"], x-winsize[0], 0)
				# self._wm.MoveWindow(self._hWnds["uistatus_def"], 0, 0)

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
						(winsize, None, self._atk.getSkills())
						)

					x, y = self._wm.screensize
					self._wm.MoveWindow(self._hWnds["choice2"], (x-winsize[0])*1//10, (y-winsize[1])*9.5//10)

				self._init_choice2 = c_choice2

				self._hWnds["choice1"] = 0
				self._hWnds["choice2"] = 0

				self._init_choice1(self)
				self._wm.SetTopmost(self._hWnds["choice1"], True)

				# self._proc = BattleProcedure(self._wm.screensize, self._atk, self._defense)
				self._uiRunning = True
				return True


			def cb(self, event, uMsg):
				# self._bk_.fill((150, 150, 150, 255//2))
				self._bk_ = self._bk.copy()
				x, y = self._wm.screensize
				self._bk_.blit(self._atk.render(False), (0, y-self._atk.get_size()[1]-y+(y-16*8)*9.5//10))
				# t = pygame.Surface((self._atk.get_size()), pygame.SRCALPHA)
				# pygame.draw.rect(t, (255, 0, 0), t.get_rect(), 1)
				# self._bk_.blit(t, (0, y-self._atk.get_size()[1]-y+(y-16*8)*9.5//10))
				self._bk_.blit(self._def.render(True), (x-160-self._atk.get_size()[0], 0))
				if not self._uiRunning:
					import random
					ski = random.randint(0, 3)
					self._def.attack(self._atk, ski)
					if not self._atk.getHP():
						self._umsg = DEF
						return True
					self._uiRunning = True
					self._init_choice1(self)

				if self._backpack_mode:
					msg = self._backpack.getMsg()
					if msg is None:
						self._backpack_mode = 0
					return True

				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
					if hWnd  == self._hWnds["choice1"]:
						r, msg = msg
						if not r: continue
						if msg == 0:
							self._init_choice2(self)
							self._wm.SetTopmost(self._hWnds["choice2"], True)
							self._uiRunning = True
						elif msg == 1:
							if not self._backpack.isRunning():
								self._backpack.setPlayer(self._atk)
								self._backpack.setDefaultTab(2)
								self._backpack.setStatic(True)
								self._backpack.init(event, self._g_wm)
								self._backpack_mode = 2
						elif msg == 2:
							if not self._backpack.isRunning():
								self._backpack.setPlayer(self._atk)
								self._backpack.setDefaultTab(1)
								self._backpack.setStatic(True)
								self._backpack.init(event, self._g_wm)
								self._backpack_mode = 1
						elif msg == 3:
							self._uiRunning = False
							return False
					if hWnd == self._hWnds["choice2"]:
						r, msg = msg
						if not r: continue
						if msg == -1:   # return to choice 1 menu
							tpmst = self._wm.getInstance(self._hWnds["choice1"]).getWindowsManager().GetTopmost()
							self._wm.DestroyWindow(self._hWnds["choice1"])
							self._wm.DestroyWindow(self._hWnds["choice2"])
							self._init_choice1(self)
							self._wm.getInstance(self._hWnds["choice1"]).getWindowsManager().SetTopmost(tpmst)
							self._uiRunning = True
						else:
							self._atk.attack(self._def, msg)
							if not self._def.getHP():
								self._umsg = ATK
								return True
							self._wm.DestroyWindow(self._hWnds["choice1"])
							self._wm.DestroyWindow(self._hWnds["choice2"])
							self._uiRunning = False
				return True

			def rd(self):
				return self._bk_

			def getMsg(self):
				return self._umsg

			def rel(self):
				self._wm.Release()

			winsize = wm.screensize
			surf = pygame.transform.scale(_battle_bk, winsize).convert()
			surf.set_alpha(200)
			self._scene = wm.CreateWindow(
				wm.RegisterClass(False, init, cb, rd, getMsg, rel),
				(winsize, surf)
				)
			x, y = wm.screensize
			wm.MoveWindow(self._scene, (x-winsize[0])//2, (y-winsize[1])//2)

			return True
		return False

	def render(self, evt, wm):
		if self._activated:
			if wm.getInstance(self._scene) is None:
				self.release(wm)
			else:
				umsg = wm.getMsg(self._scene)
				return None, umsg
		return None, None

	def release(self, wm):
		wm.DestroyWindow(self._scene)
		self._scene = -1
		self._activated = False
