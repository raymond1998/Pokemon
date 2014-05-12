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
	def __init__(self, pos, res_walk, sentences):
		if not len(sentences): raise ValueError(len(sentences))
		super(CoversationNPC, self).__init__(pos, res_walk)
		self._sentences = sentences
		for i in range(len(self._sentences)):
			self._sentences[i] = "    "+self._sentences[i]

	def init(self, evt, wm):
		if not self._activated:
			self._activated = True
			_button_size = [158*2//3, 59*2//3]
			text = self._sentences
			def init(self, hWnd):
				nonlocal text
				self._text = text
				self._text_indx = 0
				self.wmacros = rgine.windows.WindowsMacros()
				self._handle = hWnd
				self._umsg = 0
				self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
				x, y = self._size

				self._button0 = self._wm.CreateWindow(self.wmacros.WC_BUTTON,
				                                    (_button_size, rgine.windows._button, "OK",
												        pygame.font.SysFont('Times New Romen', 16),
												        True, (255, 255, 255)), True)
				self._text0 = self._wm.CreateWindow(self.wmacros.WC_TEXT,
				                                    ((x-(x*2//10), y*6//10), None, self._text[self._text_indx],
														pygame.font.SysFont('Times New Romen', 16),
														True, (255, 255, 255)), True)

				self._wm.MoveWindow(self._button0, x//2-_button_size[0]//2, (y-_button_size[1])*8//10)
				self._wm.MoveWindow(self._text0, x*1//10, y*1//10)

			def cb(self, event, uMsg):
				self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
				self._bk_.fill((150, 150, 150, 255//2))
				for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
					self._bk_.blit(surface, pos)
					if hWnd == self._button0:
						self._umsg = msg
						if msg == self.wmacros.HIT:
							self._text_indx += 1
							if self._text_indx == len(self._text): return False
							self._wm.DestroyWindow(self._text0)
							x, y = self._size
							self._text0 = self._wm.CreateWindow(self.wmacros.WC_TEXT,
				                                    ((x-(x*2//10), y*6//10), None, self._text[self._text_indx],
														pygame.font.SysFont('Times New Romen', 16),
														True, (255, 255, 255)), True)
							self._wm.MoveWindow(self._text0, x*1//10, y*1//10)
				return True

			def rd(self):
				return self._bk_

			def getMsg(self):
				return self._umsg

			def rel(self):
				self._wm.Release()

			self._hWnds["dbox"] = wm.CreateWindow(
				wm.RegisterClass(True, init, cb, rd, getMsg, rel), ((16*20, 9*20), None, "CoversationNPC",
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

npcs[tuple(pos)] = CoversationNPC(pos, res_walk(surf, 3, 4, 0)[0],
                                  [
	                                  "hello ",
	                                  # "how are you? ",
	                                  # "see you later ",
                                      "My name is Charles. Welcome to the world of Pokemon! ",
                                  ]
)