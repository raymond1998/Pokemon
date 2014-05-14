from basics import *
from resources_loader import *
__author__ = 'Charles-Jianye Chen'

class _MenuMain(NPC_Skeleton):
	# buttons->dict() id:text
	def __init__(self, buttons):
		super(_MenuMain, self).__init__((-1, -1), None)
		self._buttons = buttons

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			_button_size = self.wmacros.button_size[:]
			_button_size = list(map((lambda x: x//2), _button_size))
			buttons = self._buttons
			def init(self, hWnd):
				nonlocal buttons, _button_size
				self.wmacros = rgine.windows.WindowsMacros()
				self._handle = hWnd
				self._umsg = 0
				self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
				self._hWnds = dict()
				self._buttons = buttons

				cy = 0
				for i in self._buttons:
					self._hWnds[i] = self._wm.CreateWindow(self.wmacros.WC_BUTTON,
									    (_button_size, self.wmacros.button, "%s"%self._buttons[i],
														pygame.font.SysFont('Times New Romen', 16),
														True, (255, 255, 255)), True)
					self._wm.MoveWindowToPos(self._hWnds[i], 0, cy)
					cy += _button_size[1]
				self._wm.SetTopmost(-1, True)
				self._wm.SetTopmost(-1, False)

			def cb(self, event, uMsg):
				x, y, w, h = self.getRect()
				self._bk_ = pygame.Surface((w, h), pygame.SRCALPHA)
				self._bk_.fill((150, 150, 150, 255//2))
				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
					if msg == self.wmacros.HIT:
						for i in self._buttons:
							if hWnd == self._hWnds[i]:
								self._umsg = i
								break
				return True

			def rd(self):
				return self._bk_

			def getMsg(self):
				return self._umsg

			def rel(self):
				self._wm.Release()

			winsize = _button_size[0], _button_size[1]*len(self._buttons)
			self._hWnds["menu"] = wm.CreateWindow(
				wm.RegisterClass(False, init, cb, rd, getMsg, rel), (winsize, None))
			x, y = wm.screensize
			wm.MoveWindow(self._hWnds["menu"], x-_button_size[0], 0)
			return True
		return False

	def render(self, evt, wm):
		if self._activated:
			for i in self._hWnds:
				umsg = wm.getMsg(self._hWnds[i])
				if umsg != 0:
					self.release(wm)
					return umsg

		return False

class MenuManager(object):
	def __init__(self, buttons):
		if 0 in buttons: raise Warning("(int) 0 should not be found in buttons.keys()")
		self._mMain = _MenuMain(buttons)
		self._pEvents = {}
		self._runningEvt = None

	def register(self, bid, pEvent_inst):
		self._pEvents[bid] = pEvent_inst

	def register_dict(self, d_pEvent_inst):
		for i in d_pEvent_inst:
			self.register(i, d_pEvent_inst[i])

	def update(self, evt, wm, key=pygame.K_SPACE):
		if self._runningEvt is None:
			if evt.isKeyHit(key):
				if not self._mMain.isRunning(): self._mMain.init(evt, wm)
				else: self._mMain.release(wm)

			result = self._mMain.render(evt, wm)
			if result:
				r = self._pEvents[result].init(evt, wm)
				if r:
					self._runningEvt = result
					self.update(evt, wm, key)
			return None, None
		else:
			surf, pos = self._pEvents[self._runningEvt].render(evt, wm)
			if not surf:
				self._pEvents[self._runningEvt].release(wm)
				self._runningEvt = None
			return surf, pos

	def release(self, wm):
		if self._runningEvt is not None:
			self._pEvents[self._runningEvt].release(wm)
			self._runningEvt = None


def init_menu(d_buttons, d_pEvents):
	r = MenuManager(d_buttons)
	r.register_dict(d_pEvents)
	return r



import base
class Menu_Help(base.pEvent):
	def __init__(self):
		super(Menu_Help, self).__init__()
		self._count = 0

	def init(self, evt, wm):
		self._count = 0
		print("Help Button Init ... ")
		return True

	def render(self, evt, wm):
		print("Help Button Procedure ... %d"%self._count)
		if self._count == 10:
			return None, (0, 0)
		self._count += 1
		return True, (0, 0)

	def release(self, wm):
		print("Help Button Release ... ")

class Menu_Exit(base.pEvent):
	def render(self, evt, wm):
		return True, None

buttons = {1:"help", 2:"exit"}
inst = {1:Menu_Help(), 2:Menu_Exit()}