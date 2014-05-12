from basics import *
from resources_loader import *
__author__ = 'Charles-Jianye Chen'

class TestNPC(NPC_Skeleton):
	def __init__(self, pos, res_walk):
		super(TestNPC, self).__init__(pos, res_walk)

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			_button_size = [158, 59]
			msgbox = wm.CreateWindow(self.wmacro.WC_MSGBOX,
						 ((400, 200), None, "MessageBox!", None, None, None,
						  "Good Morning! How Are You? ",
						  self.wmacro.MB_ICONWARNING | self.wmacro.MB_CANCELTRYCONTINUE
						  , [_button_size[0]//2, _button_size[1]//2]))
			self._hWnds["msgbox"] = msgbox
			return True
		return False

	def render(self, evt, wm):
		if not self._activated: return self._res.front[1], self._pos

		umsg = wm.getMsg(self._hWnds["msgbox"])
		if umsg is None: self.release(wm) # is terminated
		else:
			if umsg != self.wmacro.IDNORESULT:
				self.release(wm)
		return self._res.front[1], self._pos


class CoversationNPC(NPC_Skeleton):
	def __init__(self, pos, res_walk, text):
		super(CoversationNPC, self).__init__(pos, res_walk)
		self._text = text

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			_button_size = [158, 59]
			text = self._text
			def init(self, hWnd):
				nonlocal text
				self.wmacros = rgine.windows.WindowsMacros()
				self._button0 = self._wm.CreateWindow(self.wmacros.WC_BUTTON, (_button_size, rgine.windows._button, "OK",
												  pygame.font.SysFont('Times New Romen', 16),
												  True, (255, 255, 255)), True)
				self._text0 = self._wm.CreateWindow(self.wmacros.WC_TEXT, ((100, 100), None, text,
														pygame.font.SysFont('Times New Romen', 16),
														True, (255, 255, 255)), True)
				self._handle = hWnd
				self._wm.MoveWindow(self._button0, 0, 100)
				self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
				self._umsg = 0

			def cb(self, event, uMsg):
				self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
					if hWnd == self._button0:
						self._umsg = msg
						if msg == self.wmacros.HIT:
							return False
				return True

			def rd(self):
				return self._bk_

			def getMsg(self):
				return self._umsg

			def rel(self):
				self._wm.Release()

			self._hWnds["dbox"] = wm.CreateWindow(
				wm.RegisterClass(True, init, cb, rd, getMsg, rel), ((200, 200), None, "this is 0",
														  pygame.font.SysFont('Times New Romen', 16),
														  True, (255, 255, 255)))
			return True
		return False

	def render(self, evt, wm):
		if not self._activated: return self._res.front[1], self._pos

		for i in self._hWnds:
			umsg = wm.getMsg(self._hWnds[i])
			if umsg is None:
				self.release(wm)

		return self._res.front[1], self._pos

# pos(terrain)->tuple: pEvent/inh. class, init_args
playerEvent = {}
# load these npcs before game starts # (x, y): npc_object
npcs = {}

surf = rgine.read_buffer("pic1", 96, 128)
pos = (9, 9)
npcs[tuple(pos)] = TestNPC(pos, res_walk(surf, 3, 4, 0)[0])
pos = (8, 10)
npcs[tuple(pos)] = CoversationNPC(pos, res_walk(surf, 3, 4, 0)[0], "hello")