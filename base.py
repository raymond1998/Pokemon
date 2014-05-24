from basics import *
from resources_loader import *
__author__ = 'Charles-Jianye Chen', "Raymond Li"

class TestNPC(NPC_Skeleton):
		def __init__(self, pos, res_walk):
				super(TestNPC, self).__init__(pos, res_walk)

		def init(self, evt, wm):
				if not self._activated:
						self._activated = True
						_button_size = self.wmacros.button_size[:]
						# _button_size = list(map((lambda x: x//2), _button_size))
						msgbox = wm.CreateWindow(self.wmacros.WC_MSGBOX,
												 ((400, 200), None, "MessageBox!", None, None, None,
												  "Good Morning! How Are You? ",
												  self.wmacros.MB_ICONWARNING | self.wmacros.MB_CANCELTRYCONTINUE
												  , [_button_size[0]//2, _button_size[1]//2]))
						self._hWnds["msgbox"] = msgbox
						return True
				return False

		def render(self, evt, wm):
				if self._activated:
						umsg = wm.getMsg(self._hWnds["msgbox"])
						if umsg is None: self.release(wm) # is terminated
						else:
								if umsg != self.wmacros.IDNORESULT:
										self.release(wm)

				return self.render_scene()


class CoversationNPC(NPC_Skeleton):
		def __init__(self, pos, res_walk, sentences):
				if not len(sentences): raise ValueError(len(sentences))
				super(CoversationNPC, self).__init__(pos, res_walk)
				self._sentences = sentences
				for i in range(len(self._sentences)):
						self._sentences[i] = "    "+self._sentences[i]
				self._dir = DOWN

		def init(self, evt, wm):
				if not self._activated:
						self._activated = True
						_button_size = self.wmacros.button_size[:]
						_button_size = list(map((lambda x: x//2), _button_size))
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
																	(_button_size, self.wmacros.button, "OK",
																										pygame.font.SysFont('Times New Romen', 16),
																										True, (255, 255, 255)), True)
								self._text0 = self._wm.CreateWindow(self.wmacros.WC_TEXT,
																	((x-(x*2//10), y*6//10), None, self._text[self._text_indx],
																												pygame.font.SysFont('Times New Romen', 16),
																												True, (255, 255, 255)), True)

								self._wm.MoveWindow(self._button0, x//2-_button_size[0]//2, (y-_button_size[1])*8//10)
								self._wm.MoveWindow(self._text0, x*1//10, y*1//10)
								self._wm.SetTopmost(self._button0, True)
								self._wm.SetTopmost(self._button0, False)

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
														self._wm.MoveWindowToPos(self._text0, x*1//10, y*1//10)
														self._wm.SetTopmost(self._button0, True)
														self._wm.SetTopmost(self._button0, False)
								return True

						def rd(self):
								return self._bk_

						def getMsg(self):
								return self._umsg

						def rel(self):
								self._wm.Release()

						dboxsize = 16*20, 9*20
						self._hWnds["dbox"] = wm.CreateWindow(
								wm.RegisterClass(True, init, cb, rd, getMsg, rel), (dboxsize, None, "CoversationNPC",
																												  pygame.font.SysFont('Times New Romen', 16),
																												  True, (255, 255, 255)))
						x, y = wm.screensize
						wm.MoveWindow(self._hWnds["dbox"], (x-dboxsize[0])//2, (y-dboxsize[1])//2)
						return True
				return False

		def render(self, evt, wm):
				if self._activated:
						for i in self._hWnds:
								umsg = wm.getMsg(self._hWnds[i])
								if umsg is None:
										self.release(wm)

				return self.render_scene()

class ShopNPC(NPC_Skeleton):
		def __init__(self, pos, res_walk, items={}):
				super(ShopNPC, self).__init__(pos, res_walk)
				self._items = items

		def init(self, evt, wm):
				if not self._activated:
						self._activated = True
						_button_size = [100, 30]

						def init(self, hWnd):   #init
								nonlocal _button_size
								self.macros= rgine.windows.WindowsMacros()
								self.button_id = -1

								cx = cy = tx = ty = 0

								x, y = self._size
								self._hWnds = {}
								self._stable = []
								buttons = self._args[4]
								for i in buttons:
										self._button0 = self._wm.CreateWindow(self.macros.WC_BUTTON, (_button_size, self.macros.button, "%s"%i,
																									  pygame.font.SysFont('Times New Roman', 16),
																									  True, (255, 255, 255)), True)
										Times_New_Roman = pygame.font.SysFont('Times New Roman', 16)
										self._text0 = Times_New_Roman.render("%s"%str(buttons[i]), True, (0, 0, 0))

										self._wm.MoveWindow(self._button0, cx+20, cy+20)
										tx = _button_size[0]/2 - self._text0.get_width()/2 + cx +20
										ty = _button_size[1]+cy+20
										cx += _button_size[0]+1

										self._stable.append((self._text0, (tx, ty)))



										if cx + 20 > self.getRect()[2]:
												cx = 0
												cy += (2 * _button_size[1]+1)
										if tx + 20 > self.getRect()[2]:
												tx = 0
												ty += (2 * _button_size[1]+1)
										self._hWnds[i] = (self._button0)
								self._exit_button =  self._wm.CreateWindow(self.macros.WC_BUTTON, (_button_size, self.macros.button, "Exit",
																								   pygame.font.SysFont('Times New Romen', 16),
																								   True, (255, 255, 255)), True)
								print(self._exit_button)
								x,y = self.getClientSize()
								self._wm.MoveWindow(self._exit_button, x-_button_size[0]-20, y-_button_size[1]-20)
								self._hWnds[exit] = (self._exit_button)
								self._handle = hWnd
								self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
								self.msgbox = 0
								return True


						def cb(self, event, uMsg):  #callback
								nonlocal _button_size
								self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
								for i in self._stable:
										self._bk_.blit(*i)
								for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
										self._bk_.blit(surface, pos)

										if msg == self.macros.HIT and hWnd == self._hWnds[exit]:
												print("exit hit")
												return False
										for x in self._hWnds:
												self.umsg = msg
												if msg == self.macros.HIT and hWnd == self._hWnds[x]:
														self.msgbox = self._wm.CreateWindow(self.macros.WC_MSGBOX,
																				((400, 200), None, "Shop", None, None, None,
																				"Are you sure? ",
																				self.macros.MB_ICONWARNING | self.macros.MB_YESNO
																				, [16*5, 9*5]))
														self._wm.SetTopmost(self.msgbox, True)

														return self._hWnds[x]
										if hWnd == self.msgbox and msg != self.macros.IDNORESULT:
												if msg == self.macros.IDYES:
														print("Yes")
												else:
														print("No")

								return True

						def rd(self):   #render
								return self._bk_

						def getMsg(self):
								return self.button_id

						def rel(self):  #release
								self._wm.Release()

						# def background(self, shop):
						#         if shop is not None: self._shop = shop
						#
						background = pygame.image.load("Pokemon Shop.jpg")
						dboxsize = wm.screensize[0]*3//4, wm.screensize[1]*3//4
						background = pygame.transform.scale(background, dboxsize).convert()
						background.set_alpha(200)

						self._hWnds["shop"] = wm.CreateWindow(wm.RegisterClass(True, init, cb, rd, getMsg, rel), (dboxsize, background , "Shop",
																												  pygame.font.SysFont('Times New Romen', 16),
																												  True, (255, 255, 255), self._items))

						wm.MoveWindow(self._hWnds["shop"], wm.screensize[0]/2-dboxsize[0]/2, wm.screensize[1]/2-dboxsize[1]/2)
						wm.SetTopmost(self._hWnds["shop"])
						return True
				return False

		def render(self, evt, wm):
						if not self._activated: return self._res.front[1], self._pos
						for i in self._hWnds:
								umsg = wm.getMsg(self._hWnds[i])
								if umsg is None: self.release(wm)
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
										  "Comeon Raymond! What are you doing there! ",
								  ]
)
pos = (8, 8)
npcs[tuple(pos)] = ShopNPC(pos, res_walk(surf, 3, 4, 0)[0], {"Raymond Doll": 1000})
