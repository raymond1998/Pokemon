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


# pos(terrain)->tuple: pEvent/inh. class, init_args
playerEvent = {}
# load these npcs before game starts # (x, y): npc_object
npcs = {}

surf = rgine.read_buffer("pic1", 96, 128)
pos = (9, 9)
npcs[tuple(pos)] = TestNPC(pos, res_walk(surf, 3, 4, 0)[0])
