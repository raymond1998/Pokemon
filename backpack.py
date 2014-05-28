from basics import *

__author__ = 'Charles-Jianye Chen'

import sys
path = sys.path[0]
if not path: path = sys.path[1]
_backpack_bk = rgine.surface_buffer.read_buffer(path+"/resources/backpack", 2560, 1600)
_backpack_img = rgine.surface_buffer.read_buffer(path+"/resources/backpack_img", 52, 60)
class uiBackpack(rgine.windows.windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(uiBackpack, self).__init__(wsize, winbk)
		self.setRenderArgs(*args)

		self.player = self._args[0]
		self._default_tab = 1
		if len(self._args) >= 2:
			self._default_tab = self._args[1]
		self._static_tab = False
		if len(self._args) >= 3:
			self._static_tab = bool(self._args[2])

		self._handle = 0
		self._surface = pygame.Surface(wsize, pygame.SRCALPHA)
		self._surface.blit(self._bk, (0, 0))

		self._surface.blit(
			pygame.transform.scale(_backpack_img, (_backpack_img.get_width()*3, _backpack_img.get_height()*3))
			, (self._surface.get_width()*1//10, self._surface.get_height()*1//10)
		)

		self._surf = None
		self._state = 0
		self._button_return = 0
		self._tab = 0
		self._ask = 0
		self._main_window_pokemon = 0
		self._main_window_backpack = 0
		self.wmacros = rgine.windows.WindowsMacros()
		self._ctab = 0
		self.create_askbox = lambda : self._wm.CreateWindow(
			self._wm.RegisterClass(True, askbox.init, askbox.cb, askbox.rd, askbox.getMsg, askbox.rel),
			((100, 50), None, "Confirm?")
		)
		self.hClass = self._wm.RegisterCompleteClass(uiBackpack_scroll)
		self._askbox = 0
		self._askbox_item = 0

	def _create_w_pokemon(self, bk):
		self._main_window_pokemon = self._wm.CreateWindow(
				self.hClass,
				(
				(400, 300), bk, (400, 600),
				[("pokemon!", 1), ("whatever", 2)],
				)
	                                          )
		self._wm.MoveWindow(self._main_window_pokemon, 300, 125)

	def _create_w_backpack(self, bk):
		self._main_window_backpack = self._wm.CreateWindow(
				self.hClass,
				(
				(400, 300), bk, (400, 600),
				self.player.getBackpackInfo(),
				)
	                                          )
		self._wm.MoveWindow(self._main_window_backpack, 300, 125)

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0
		self._askbox_item = 0
		self._button_return = self._wm.CreateWindow(self.wmacros.WC_BUTTON, ((100, 20), None, "Return"))
		self._wm.MoveWindow(self._button_return, 100, 400)

		self._tab = self._wm.CreateWindow(self.wmacros.WC_TAB, ((400, 50), None,
						      (200, 50), None,
						      [("Pokemon", 1), ("Backpack", 2)], self._static_tab)
		)
		self._wm.getInstance(self._tab).set_tab(self._default_tab)
		self._wm.MoveWindow(self._tab, 300, 50)

		surf = pygame.Surface((400, 300), pygame.SRCALPHA)
		surf.fill((111, 111, 111, 20))
		pygame.draw.line(surf, (0, 0, 0), (0, 0), surf.get_size())
		if self._wm.getInstance(self._tab).getMsg() == 1:
			self._ctab = 1
		elif self._wm.getInstance(self._tab).getMsg() == 2:
			self._ctab = 2
		else:
			raise ValueError(self._wm.getInstance(self._tab).getMsg())


		self._create_w_backpack(surf)
		self._create_w_pokemon(surf)

		return True

	def callback(self, evt, uMsg):
		self._surf = self._surface.copy()

		t_tab = self._ctab

		self._ctab = self._wm.getMsg(self._tab)
		if self._ctab == 1:
			if self._wm.GetTopmost() == self._main_window_backpack:
				self._wm.SetTopmost(self._main_window_pokemon, False)

		if self._ctab == 2:
			if self._wm.GetTopmost() == self._main_window_pokemon:
				self._wm.SetTopmost(self._main_window_backpack, False)


		if self._askbox:
			self._wm.SetTopmost(self._askbox, True)
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(evt):
			if self._ctab == 1 and hWnd == self._main_window_backpack:
				continue
			if self._ctab == 2 and hWnd == self._main_window_pokemon:
				continue
			self._surf.blit(surface, pos)
			if hWnd == self._button_return and msg == self.wmacros.HIT:
				return False
			elif hWnd == self._tab:
				if msg != self._ctab:
					t_tab = msg

			if hWnd == self._main_window_pokemon and msg != 0 and not self._askbox:
				self._askbox = self.create_askbox()
				self._wm.MoveWindow(self._askbox, 350, 300)
				self._wm.SetTopmost(self._askbox, True)
				self._askbox_item = msg
			elif hWnd == self._main_window_backpack and msg != 0 and not self._askbox:
				self._askbox = self.create_askbox()
				self._wm.MoveWindow(self._askbox, 350, 300)
				self._wm.SetTopmost(self._askbox, True)
				self._askbox_item = msg

			if hWnd == self._askbox and msg[1] != 0:
				self._wm.SetTopmost(self._askbox, False)
				self._wm.DestroyWindow(self._askbox)
				self._askbox = 0
				if msg[1] == 1:
					print("Use")
					# self.player.useItem()
					if self._ctab == 1:
						pass
					elif self._ctab == 2:
						self.player.useItem(self._askbox_item)
						self._wm.DestroyWindow(self._main_window_backpack)
						surf = pygame.Surface((400, 300), pygame.SRCALPHA)
						surf.fill((111, 111, 111, 20))
						pygame.draw.line(surf, (0, 0, 0), (0, 0), surf.get_size())
						self._create_w_backpack(surf)
					if self._static_tab:
						return False


		if t_tab != self._ctab:
			if t_tab == 1:
				self._wm.SetTopmost(self._main_window_pokemon, False)
			elif t_tab == 2:
				self._wm.SetTopmost(self._main_window_backpack, False)
			self._ctab = t_tab

		return True

	def render(self):
		return self._surf

	def release(self):
		self._wm.Release()

	def getMsg(self):
		return self._state


class uiBackpack_scroll(rgine.windows.windowScrollable):
	def __init__(self, wsize, winbk=None, *args):
		super(uiBackpack_scroll, self).__init__(wsize, winbk, *args)
		# args[0] world size
		self.wmacros = rgine.windows.WindowsMacros()
		self._test = 0
		self._handle = 0
		self._state = 0
		self._buttons = []
		self._buttonsize = [self._size[0], 25]
		self._button_img = None

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0
		self._buttons = []
		addbutton = (lambda x, val: self._buttons.append(
			(self._wm.CreateWindow(self.wmacros.WC_BUTTON, (self._buttonsize, self._button_img, x), False), val)
			))
		cy = 0
		for i in self._args[1]:
			addbutton(*i)
			self._wm.MoveWindow(self._buttons[-1][0], 0, cy)
			cy += self._buttonsize[1]
		self._wm.SetTopmost(-1, False)
		return True

	def callback(self, evt, uMsg):
		if uMsg == self.wmacros.WM_SETFOCUS:
			if self._buttons: self._wm.SetTopmost(self._buttons[0][0], False)
		elif uMsg == self.wmacros.WM_KILLFOCUS:
			self._wm.SetTopmost(-1, False)
		elif self.getRect().collidepoint(evt.getMousePos()):
			if evt.isMouseHit(evt.MOUSE_SCROLL_UP):
				self._world.shiftV(-25)
			elif evt.isMouseHit(evt.MOUSE_SCROLL_DOWN):
				self._world.shiftV(+25)

		subsurf = self._world.getSurface().subsurface(self._world.getRect())
		self._world.clear(rect=self._world.getRect())
		subsurf.blit(self._bk, (0, 0))


		sx, sy = self._world.getShift()
		evt.shiftMousePos(sx, sy)

		if self._state:
			self._state = 0
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(evt):
			if pygame.Rect(self._world.getRect()).collidepoint(*pos):
				self._world.blit(surface, pos)
			if msg == self.wmacros.HIT:
				for i in self._buttons:
					if i[0] == hWnd:
						self._state = i[1]
						break

		evt.shiftMousePos(-sx, -sy)

		return True

class askbox(object):
	def init(self, hWnd):
		self.wmacros = rgine.windows.WindowsMacros()
		self._handle = hWnd
		self._umsg = 0
		self._hasresult = False
		x, y, w, h = self.getRect()
		self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
		self._buttons = {1: "Use", 2: "Cancel"}
		self._hWnds = {}
		cy = 0
		x, y = self._wm.screensize

		button_size = [100, 25]
		button_surf = pygame.transform.scale(self.wmacros.button.copy(), button_size)
		pygame.draw.rect(button_surf, (0, 0, 0), button_surf.get_rect(), 1)

		t_handles = []
		k = list(self._buttons.keys())
		k.sort()
		for i in k:
			h = self._wm.CreateWindow(self.wmacros.WC_BUTTON,
								(button_size, button_surf, "%s"%self._buttons[i],
												pygame.font.SysFont('Times New Romen', 16),
												True, (255, 255, 255)), False)
			t_handles.append(h)
			self._hWnds[h] = i

		tx, ty = 0, 0
		self._wm.MoveWindowToPos(t_handles[0], tx, ty)
		self._wm.MoveWindowToPos(t_handles[1], tx, ty+button_size[1])
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


class Backpack(pEvent):
	def __init__(self, *args):
		super(Backpack, self).__init__(*args)
		self.player = args[1]
		self._ui = 0
		self._surf = pygame.Surface((0, 0))
		self._uiClass = args[0].RegisterCompleteClass(uiBackpack)
		self._lastmsg = None
		self._deftab = 1
		self._static = False

	def setPlayer(self, player):
		self.player = player

	def setDefaultTab(self, val):
		self._deftab = val

	def setStatic(self, state):
		self._static = bool(state)

	def init(self, evt, wm):
		if not self._activated:
			if self.player is None: raise ValueError(self.player)
			self._ui = wm.CreateWindow(self._uiClass,
			                           (wm.screensize, pygame.transform.scale(_backpack_bk, wm.screensize),
			                            self.player, self._deftab, self._static))
			self._static = False
			self._activated = True
			return True
		else:
			return False

	def render(self, evt, wm):
		if self._activated:
			if wm.getInstance(self._ui) is None:
				self.release(wm)
			else:
				self._lastmsg = wm.getMsg(self._ui)
				return self._surf, self._lastmsg
		return None, None

	def release(self, wm):
		wm.DestroyWindow(self._ui)
		self._ui = 0
		self._activated = False
		self._lastmsg = None

	def getMsg(self):
		return self._lastmsg
