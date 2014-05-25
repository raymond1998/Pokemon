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
		self._main_window = 0
		self.wmacros = rgine.windows.WindowsMacros()

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0
		self._button_return = self._wm.CreateWindow(self.wmacros.WC_BUTTON, ((100, 20), None, "Return"))
		self._wm.MoveWindow(self._button_return, 100, 400)

		self._tab = self._wm.CreateWindow(self.wmacros.WC_TAB, ((400, 100), None,
						      (200, 50), None,
						      [("Pokemon", 1), ("Backpack", 2)])
		)
		self._wm.MoveWindow(self._tab, 300, 50)

		surf = pygame.Surface((400, 300), pygame.SRCALPHA)
		surf.fill((111, 111, 111, 20))
		pygame.draw.line(surf, (0, 0, 0), (0, 0), surf.get_size())
		self._main_window = self._wm.CreateWindow(
			self._wm.RegisterCompleteClass(uiBackpack_scroll),
			(
			(400, 300), surf, (400, 600),
			),
		                                          )
		self._wm.MoveWindow(self._main_window, 300, 125)

		return True

	def callback(self, evt, uMsg):
		self._surf = self._surface.copy()

		for hWnd, msg, surface, pos in self._wm.DispatchMessage(evt):
			self._surf.blit(surface, pos)
			if hWnd == self._button_return and msg == self.wmacros.HIT:
				return False

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
		self.wmacros = rgine.windows.WindowsMacros()
		self._test = 0

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0
		self._test = self._wm.CreateWindow(self.wmacros.WC_BUTTON, ((100, 20), None, "test_button"))
		self._wm.MoveWindow(self._test, 100, 100)
		return True

	def callback(self, evt, uMsg):
		if self.getRect().collidepoint(evt.getMousePos()):
			if evt.isMouseHit(evt.MOUSE_SCROLL_UP):
				self._world.shiftV(-20)
			elif evt.isMouseHit(evt.MOUSE_SCROLL_DOWN):
				self._world.shiftV(+20)

		subsurf = self._world.getSurface().subsurface(self._world.getRect())
		self._world.clear(rect=self._world.getRect())
		subsurf.blit(self._bk, (0, 0))

		for hWnd, msg, surface, pos in self._wm.DispatchMessage(evt):
			if pygame.Rect(self._world.getRect()).collidepoint(*pos):
				self._world.blit(surface, pos)

		return True


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