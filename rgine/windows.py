import cProfile
import copy

import pygame

from common import *
from surface_buffer import *
import event



p = cProfile.Profile()
__author__ = "Charles-Jianye Chen"

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
_icon_x = read_buffer(path+"/x", 128, 128)
_button_size = [158, 59]
# _button = read_buffer(path+"/button", _button_size[0], _button_size[1])
_button = pygame.Surface(_button_size, pygame.SRCALPHA)
_button.fill((43, 43, 43, 255//2))
# pygame.draw.rect(_button, (0, 0, 0), _button.get_rect(), 1)
_button_res_focus = pygame.Surface(_button_size, pygame.SRCALPHA)
_button_res_focus.fill((111, 111, 111, 60))
_button_res_down = pygame.Surface(_button_size, pygame.SRCALPHA)
_button_res_down.fill((111, 111, 111, 100))
_icon_help = read_buffer(path+"/res/help", 128, 128)
_icon_info = read_buffer(path+"/res/info", 128, 128)
_icon_stop = read_buffer(path+"/res/stop", 128, 128)
_icon_warning = read_buffer(path+"/res/warning", 128, 128)

pygame.font.init()

def render_text(surfacesize, text, pyFont, *rendering_args):
	"""
	Renders text on the specific surface.  Wrap around after width is exceeded.
	:tuple surfacesize:
	:str text:
	:pygame.font.Font pyFont:
	:list rendering_args:
	"""
	rendering_args = list(rendering_args)
	Surface = pygame.Surface(surfacesize, pygame.SRCALPHA)
	cx = cy = 0
	text = text.replace("\t", " "*4)
	for txt in text.split("\n"):
		cx = 0
		for t in txt.split(" "):
			img = pyFont.render(*([t+" "]+rendering_args))
			if img.get_width()+cx > surfacesize[0]:
				cy += pyFont.get_height()
				if cy > surfacesize[1]: break
				cx = 0
			Surface.blit(img, (cx, cy))
			cx += img.get_width()
		cy += pyFont.get_height()
	return Surface

class WindowsMacros(object):
	# resources
	button = _button
	button_size = _button_size[:]

	# Windows Messages
	WM_NULL = 0
	WM_SETFOCUS = 1
	WM_KILLFOCUS = 2

	# WinClass->__builtin__->hClass
	WC_TEXT = 0
	WC_BUTTON = 1
	WC_FRAME = 2
	WC_MSGBOX = 3
	WC_TAB = 4
	WC_EDITBOX = 5

	# WinClass
	NOFOCUS = 0
	FOCUS = 1
	DOWN = 2
	HIT = 3
	UP = 4
	CONFIRM = 5

	# Msgbox Style
	# Buttons
	MB_OK = 0x00000000
	MB_OKCANCEL = 0x00000001
	MB_ABORTRETRYIGNORE = 0x00000002
	MB_YESNOCANCEL = 0x00000003
	MB_YESNO = 0x00000004
	MB_RETRYCANCEL = 0x00000005
	MB_CANCELTRYCONTINUE = 0x00000006

	# Icons
	MB_ICONSTOP = 0x00000010
	MB_ICONQUESTION = 0x00000020
	MB_ICONWARNING = 0x00000030
	MB_ICONINFORMATION = 0x00000040

	# Returns
	IDNORESULT = 0
	IDOK = 1
	IDCANCEL = 2
	IDABORT = 3
	IDRETRY = 4
	IDIGNORE = 5
	IDYES = 6
	IDNO = 7
	IDTRYAGAIN = 10
	IDCONTINUE = 11

_default_frame_args = {"bk": None, "tbH": 16, "state": WindowsMacros.NOFOCUS,
						"frameW": 1, "tbRect": None, "frameColor": (111, 111, 111, 256//2),
						"titleColor": (0, 0, 0, 256*2//3), "frameMessage": False}

_default_rendering_args = {"font_rendering_args":
							   [None, True, (255, 255, 255)],
						   "text": "Text"}

_default_font = pygame.font.SysFont('Times New Romen', 16)
def getDefaultFrameArgs():
	return _default_frame_args.copy()

def getDefaultRenderingArgs():
	t = copy.deepcopy(_default_rendering_args)
	t["font_rendering_args"][0] = _default_font
	return t

class WindowsManager(object):
	WM_NULL = 0
	WM_SETFOCUS = 1
	WM_KILLFOCUS = 2
	def __init__(self, screensize=(0, 0)):
		"""
		Initializes all variables.
		"""
		self._classes = {0: _windowText,
						 1: _windowButton,
						 2: _windowFrame,
						 3: _windowMsgbox,
						 4: _windowTab,
						 5: _windowEditbox,
						 }
		self._class_id = 9
		self._windows = {}
		self._window_id = 9
		self._current = {"layer": [], "topmost" : -1}
		self._topmost_lock = False
		self.screensize = screensize

	def RegisterCompleteClass(self, wClass):
		"""
		Returns a handle to the new registered class.
		:class(der. from windowBase) wClass:
		:return hClass:
		"""
		self._class_id += 1
		id_ = self._class_id
		self._classes[id_] = wClass
		return id_

	def RegisterClass(self, framed=False, init=None, callback=None, render=None, getMsg=None, release=None):
		"""
		Returns a handle to the new registeted class.
		:bool framed:
		:lambda/function init:
		:lambda/function callback:
		:lambda/function render:
		:lambda/function getMsg:
		:lambda/function release:
		:return hClass:
		"""

		self._class_id += 1
		id_ = self._class_id

		if not framed:
			class _WinClass(windowBase):
				def __init__(self, winsize, winbk=None, *args):
					super(_WinClass, self).__init__(winsize, winbk)
					self.setRenderArgs(*args)

			if init is not None: _WinClass.init = init
			if callback is not None: _WinClass.callback = callback
			if render is not None: _WinClass.render = render
			if getMsg is not None: _WinClass.getMsg = getMsg
			if release is not None: _WinClass.release = release
			self._classes[id_] = _WinClass
		else:
			class _WinClassFramed(windowFramed):
				def __init__(self, winsize, winbk=None, *args):
					super(_WinClassFramed, self).__init__(winsize, winbk, *args)

			if init is not None: _WinClassFramed.init = init
			if callback is not None: _WinClassFramed.callback_ = callback
			if render is not None: _WinClassFramed.render_ = render
			if getMsg is not None: _WinClassFramed.getMsg = getMsg
			if release is not None: _WinClassFramed.release = release
			self._classes[id_] = _WinClassFramed
		return id_

	def UnRegisterClass(self, hClass):
		"""
		Deletes the registered class.  Returns True if succeeded.
		:hClass hClass:
		:return bool:
		"""
		if hClass in self._classes:
			del self._classes[hClass]
			return True
		return False

	def CreateWindow(self, hClass, args, topmost=True):
		"""
		Returns the created window's handle based on the created class.
		:hClass hClass:
		:tuple/list args -> [tuple/list(winsize), pygame.Surface(winbk)(optional), ...(optional, depends on the class)]:
		:bool topmost:
		:return hWnd:
		"""
		self._window_id += 1
		self._windows[self._window_id] = self._classes[hClass](*args)
		self._windows[self._window_id].init(self._window_id)
		if topmost or self._current["topmost"] == -1:
			if self._current["topmost"] != -1:
				self._windows[self._current["topmost"]].callback(event.Event(), self.WM_KILLFOCUS)
			self._current["topmost"] = self._window_id
			self._current["layer"].append(self._window_id)
			self._windows[self._window_id].callback(event.Event(), self.WM_SETFOCUS)
		else:
			self._current["layer"].insert(-2, self._window_id)
		return self._window_id

	def DispatchMessage(self, _RgineEvent):
		"""
		window.callback(_RgineEvent); window.render()
		:rgine.Event _RgineEvent:
		:raise ValueError if it is not a subclass of rgine.Event:
		"""
		if not issubclass(_RgineEvent.__class__, event.Event): raise ValueError()
		dead = []

		last_topmost = self._current["topmost"]
		hasFocus = False
		changed = False

		layer = self._current["layer"]

		if self._topmost_lock:
			changed = False
		elif not _RgineEvent.isMouseHit(_RgineEvent.MOUSE_LEFT) \
				and not _RgineEvent.isMouseHit(_RgineEvent.MOUSE_RIGHT)\
				and not _RgineEvent.isMouseHit(_RgineEvent.MOUSE_MIDDLE):
			changed = False
		else:
			for i in layer:
				if self._windows[i].getRect().collidepoint(_RgineEvent.getMousePos()):
					if i != self._current["topmost"]:
						self._current["topmost"] = i
					hasFocus = True
			if last_topmost != self._current["topmost"]:
				changed = True
			if not hasFocus:
				self._current["topmost"] = -1
				changed = True
			else:
				if changed:
					layer.append(layer.pop(layer.index(self._current["topmost"])))

		for i in layer:
			cbResult = True
			if i == self._current["topmost"] and changed:
				msg = self.WM_SETFOCUS
				cbResult = self._windows[i].callback(_RgineEvent, msg)
			elif i == self._current["topmost"]:
				msg = self.WM_NULL
				cbResult = self._windows[i].callback(_RgineEvent, msg)
			elif i == last_topmost and changed:
				msg = self.WM_KILLFOCUS
				cbResult = self._windows[i].callback(_RgineEvent, msg)
			if cbResult:
				yield i, self._windows[i].getMsg(), self._windows[i].render(), self._windows[i].getPos()
			else:
				if self._topmost_lock:
					self.SetTopmost(self._current["topmost"], False)
				dead.append(i)

		for i in dead:
			self.DestroyWindow(i)

	def DestroyWindow(self, hWnd):
		"""
		Destroys the window in the manager.  The class it belongs to will not be deleted.
		:hWnd hWnd:
		"""
		if hWnd in self._current["layer"]:
			self._windows[hWnd].release()
			del self._windows[hWnd]
			self._current["layer"].remove(hWnd)
			if self._current["topmost"] == hWnd:
				if not self._current["layer"]:
					self._current["topmost"] = -1
				else:
					self._current["topmost"] = self._current["layer"][-1]
			return True
		return False

	def MoveWindow(self, hWnd, x, y):
		"""
		Moves the specific window by x, y
		:hWnd hWnd:
		:int x:
		:int y:
		:return bool:
		"""
		if hWnd in self._current["layer"]:
			self._windows[hWnd].MoveWindow(x, y)
			return True
		return False

	def MoveWindowToPos(self, hWnd, x, y):
		"""
		Moves the specific window to x, y
		:hWnd hWnd:
		:int x:
		:int y:
		:return bool:
		"""
		if hWnd in self._current["layer"]:
			self._windows[hWnd].MoveWindowToPos(x, y)
			return True
		return False

	def SendMessage(self, hWnd, uMsg):
		"""
		Calls the specific window's callback function.  The event argument will be None.
		:hWnd hWnd:
		:uMsg uMsg:
		:return bool / callback()'s return:
		"""
		if hWnd in self._current["layer"]:
			return self._windows[hWnd].callback(event.Event(), uMsg)
		return False

	def SetTopmost(self, hWnd, bSet=True):
		if hWnd == -1:
			if self._current["topmost"] != -1: self.SendMessage(self._current["topmost"], self.WM_KILLFOCUS)
			self._current["topmost"] = -1
			self._topmost_lock = bool(bSet)
			return True
		if hWnd not in self._current["layer"]:
			return False
		if hWnd != self._current["topmost"] and bSet:
			self.SendMessage(self._current["topmost"], self.WM_KILLFOCUS)
			self._current["topmost"] = hWnd
			self.SendMessage(self._current["topmost"], self.WM_SETFOCUS)
			self._current["layer"].append(self._current["layer"].pop(self._current["layer"].index(self._current[
				"topmost"])))
			self._topmost_lock = True
			return True
		elif bSet:
			self._topmost_lock = True
			return False
		elif not bSet:
			self._topmost_lock = False
			self._current["topmost"] = hWnd
			self._current["layer"].append(self._current["layer"].pop(self._current["layer"].index(self._current[
				"topmost"])))
			return True
		else:
			return False

	def GetTopmost(self):
		return self._current["topmost"]

	def GetCurrentWindows(self):
		"""
		Returns a list of handles of present windows
		:return list:
		"""
		return self._current["layer"]

	def Release(self):
		"""
		Releases all the registered class. Call self.DestroyWindow() to all windows.
		"""
		for i in self._current["layer"]: self.DestroyWindow(i)
		self.__init__()

	def Reset(self):
		"""
		Calls self.Release()
		"""
		self.Release()

	def getMsg(self, hWnd):
		if hWnd in self._current["layer"]:
			return self._windows[hWnd].getMsg()
		return None

	def getInstance(self, hWnd):
		if hWnd in self._current["layer"]:
			return self._windows[hWnd]
		return None

	def isWindowPresent(self, hWnd):
		if hWnd in self._current["layer"]:
			return True
		return False


class windowBase(object):
	NOFOCUS = 0
	FOCUS = 1
	DOWN = 2
	HIT = 3
	UP = 4


	def getWindowsManager(self):
		return self._wm

	def getClientRect(self):
		x, y, w, h = self.getRect()
		return pygame.Rect(0, 0, w-self._frame_args["frameW"]*2,h-self._frame_args["tbH"]-self._frame_args["frameW"])

	def getAbsoluteClientRect(self):
		x, y, w, h = self.getRect()
		return pygame.Rect(x+self._frame_args["frameW"], y+self._frame_args["tbH"], w-self._frame_args["frameW"]*2,
						   h-self._frame_args["tbH"]-self._frame_args["frameW"])

	def getClientSize(self):
		x, y, w, h = self.getRect()
		return w-self._frame_args["frameW"]*2, h-self._frame_args["tbH"]-self._frame_args["frameW"]

	def getRelativeClientRect(self):
		x, y, w, h = self.getRect()
		return pygame.Rect(self._frame_args["frameW"], self._frame_args["tbH"], w-self._frame_args["frameW"]*2,
						   h-self._frame_args["tbH"]-self._frame_args["frameW"])

	_frame_args = _default_frame_args
	_rendering_args = _default_rendering_args
	def __init__(self, winsize, winbk=None):
		"""
		:tuple winsize:
		:pygame.Surface winbk:
		"""
		self._rendering_args = copy.deepcopy(_default_rendering_args)
		self._frame_args = copy.deepcopy(_default_frame_args)
		self._rendering_args["font_rendering_args"][0] = _default_font

		self._size = list(winsize)
		if winbk is None:
			self._bk = pygame.Surface(self._size, pygame.SRCALPHA)
		else:
			self._bk = pygame.transform.scale(winbk, winsize)
		self._args = []
		self._pos = [0, 0]

		class _WindowsManager(WindowsManager):
			def __init__(self, *args):
				super(_WindowsManager, self).__init__(*args)
				self._pos = [0, 0]

			def CreateWindow(self, hClass, args, topmost=True):
				self._window_id += 1
				self._windows[self._window_id] = self._classes[hClass](*args)
				self._windows[self._window_id].MoveWindow(*self._pos)
				self._windows[self._window_id].init(self._window_id)
				if topmost or self._current["topmost"] == -1:
					if self._current["topmost"] != -1:
						self._windows[self._current["topmost"]].callback(event.Event(), self.WM_KILLFOCUS)
					self._current["topmost"] = self._window_id
					self._current["layer"].append(self._window_id)
					self._windows[self._window_id].callback(event.Event(), self.WM_SETFOCUS)
				else:
					self._current["layer"].insert(-2, self._window_id)
				return self._window_id

			def DispatchMessage(self, _RgineEvent):
				for hWnd, uMsg, surface, pos in super(_WindowsManager, self).DispatchMessage(_RgineEvent):
					yield hWnd, uMsg, surface, \
						  (self._windows[hWnd].getPos()[0] - self._pos[0],
						   self._windows[hWnd].getPos()[1] - self._pos[1])

			def MoveObject(self, x, y):
				self._pos[0] += x
				self._pos[1] += y

			def MoveObjectToPos(self, x, y):
				self._pos = [x, y]

			def getPos(self):
				return self._pos

		self._wm = _WindowsManager(self._size)

	def init(self, hWnd):
		"""
		Will be called right after an instance is created.
		:hWnd hWnd:
		"""
		pass

	def MoveWindow(self, x, y):
		# should not make pos smaller than 0 anyways ...
		self._pos[0] += x
		self._pos[1] += y
		for hWnd in self._wm.GetCurrentWindows():
			self._wm.MoveWindow(hWnd, x, y)
		self._wm.MoveObject(x, y)

	def MoveWindowToPos(self, x, y):
		self._pos = [x+self._wm.getPos()[0], y+self._wm.getPos()[1]]
		for hWnd in self._wm.GetCurrentWindows():
			self._wm.MoveWindowToPos(hWnd, x, y)
		self._wm.MoveObjectToPos(x, y)

	def getPos(self): return self._pos

	def getRect(self):
		return pygame.Rect(self._pos[0], self._pos[1], self._size[0], self._size[1])

	def getMsg(self):
		"""
		The return value of this function will be the 2nd dispatch result.
		:return anything:
		"""
		return 0

	def setRenderArgs(self, *args):
		for i in range(len(args)):
			if args[i] is None:
				pass
			elif i >= len(self._args):
				self._args.append(args[i])
			else:
				self._args[i] = args[i]

	def render(self):
		"""
		Should be Overwritten.  Will be called right after event update.
		:args self._args:
		"""
		return pygame.Surface((0, 0))

	def callback(self, RgineEvent, uMsg):
		"""
		Should return True if successfully handled.
		This window will be destroyed if return False.
		:int hWnd:
		:rgine.Event RgineEvent:
		"""
		return True

	def release(self):
		"""
		Should be Overwritten.  Will be called before deconstruction.
		"""
		self._wm.Release()


class _windowText(windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(_windowText, self).__init__(wsize, winbk)

		self.setRenderArgs(self._rendering_args["text"],
					 self._rendering_args["font_rendering_args"][0],
					 *self._rendering_args["font_rendering_args"][1:])

		self.setRenderArgs(*args)
		self._bk.blit(render_text(*([self._size]+self._args)), (0, 0))

	def setRenderArgs(self, *args):
		"""
		:str text:
		:pygame.font.Font pyFont:
		:list rendering_args:
		"""
		super(_windowText, self).setRenderArgs(*args)

	def render(self):
		return self._bk

class _windowButton(windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(_windowButton, self).__init__(wsize, winbk)
		self._state = 0

		self.setRenderArgs(self._rendering_args["text"],
					 self._rendering_args["font_rendering_args"][0],
					 *self._rendering_args["font_rendering_args"][1:])

		self.setRenderArgs(*args)

		# self._button_focus = pygame.Surface(self._bk.get_size(), pygame.SRCALPHA)
		# self._button_focus.fill((111, 111, 111, 60))
		# self._button_down = pygame.Surface(self._bk.get_size(), pygame.SRCALPHA)
		# self._button_down.fill((111, 111, 111, 100))
		self._using = "mouse"

	def setRenderArgs(self, *args):
		"""
		:str text:
		:pygame.font.Font pyFont:
		:list rendering_args:
		"""
		super(_windowButton, self).setRenderArgs(*args)

	def render(self):
		bk = self._bk.copy()
		if self._state == self.NOFOCUS:
			pass
		elif self._state == self.FOCUS or self._state == self.UP:
			bk.blit(_button_res_focus, (0, 0))
		elif self._state == self.DOWN:
			bk.blit(_button_res_down, (0, 0))
		elif self._state == self.HIT:
			bk.blit(_button_res_focus, (0, 0))
		else:
			print(self._state)
		Surface = self._args[1].render(*([self._args[0]]+self._args[2:4]))
		x, y = Surface.get_size()
		param = (self._size[0]-x)//2, (self._size[1]-y)//2
		bk.blit(Surface, param)
		return bk

	def getMsg(self):
		return self._state

	def callback(self, RgineEvent, uMsg):
		if uMsg == WindowsMacros.WM_SETFOCUS:
			self._state = self.FOCUS
		elif uMsg == WindowsMacros.WM_KILLFOCUS:
			self._state = self.NOFOCUS
			
		if self._state == self.FOCUS or self._state == self.UP:
			if RgineEvent.isMouseDown(RgineEvent.MOUSE_LEFT) and self.getRect().collidepoint(RgineEvent.getMousePos()):
				self._state = self.DOWN
				self._using = "mouse"
			elif RgineEvent.isKeyDown(pygame.K_RETURN):
				self._state = self.DOWN
				self._using = "key"

		elif self._state == self.DOWN:
			if self._using == "mouse":
				if not RgineEvent.isMouseDown(RgineEvent.MOUSE_LEFT) \
						and self.getRect().collidepoint(RgineEvent.getMousePos()):
					self._state = self.HIT
				elif not RgineEvent.isMouseDown(RgineEvent.MOUSE_LEFT):
					self._state = self.UP
			elif self._using == "key":
				if not RgineEvent.isKeyDown(pygame.K_RETURN):
					self._state = self.HIT
		elif self._state == self.HIT:
			self._state = self.UP

		return True

class windowFramed(windowBase):
	def __init__(self, wsize, winbk=None, *args):
		x, y = wsize
		x += self._frame_args["frameW"]*2
		y += (self._frame_args["frameW"]+self._frame_args["tbH"])
		
		super(windowFramed, self).__init__((x, y), None)
		if winbk is None:
			pass
		else:
			self._bk.blit(winbk, (self._frame_args["frameW"], self._frame_args["tbH"]))

		self.setRenderArgs(self._rendering_args["text"],
					 self._rendering_args["font_rendering_args"][0],
					 *self._rendering_args["font_rendering_args"][1:])

		self.setRenderArgs(*args)

		self._frame = _windowFrame(wsize, self._frame_args, *args)
		self._bk.blit(self._frame.render(), (0, 0))

	def callback(self, RgineEvent, uMsg):
		self._frame.update(RgineEvent, uMsg, self.getAbsoluteClientRect(), self.getRect())
		if self._frame._frame_args["frameMessage"]:
			x, y = self._frame.getMsg()
			if x or y:
				self.MoveWindow(x, y)
			if uMsg != WindowsMacros.WM_SETFOCUS \
				and uMsg != WindowsMacros.WM_KILLFOCUS:
				return True
		RgineEvent.shiftMousePos(-self._frame_args["frameW"], -self._frame_args["tbH"])
		r = self.callback_(RgineEvent, uMsg)
		RgineEvent.shiftMousePos(+self._frame_args["frameW"], +self._frame_args["tbH"])
		return r

	def callback_(self, RgineEvent, uMsg):
		return True

	def render(self):
		bk = self._bk.copy()
		# bk.blit(self._frame.render(), (0, 0))
		# frame change disabled
		bk.subsurface(self.getRelativeClientRect()).blit(self.render_(), (0, 0))
		return bk

	def render_(self):
		return pygame.Surface((0, 0))

	def setRenderArgs(self, *args):
		"""
		:str text:
		:pygame.font.Font pyFont:
		:list rendering_args:
		"""
		super(windowFramed, self).setRenderArgs(*args)


class _windowFrame(windowBase):
	def __init__(self, wsize, frame_args=windowBase._frame_args, *args):
		self._frame_args = frame_args
		x, y = wsize
		x += self._frame_args["frameW"]*2
		y += (self._frame_args["frameW"]+self._frame_args["tbH"])
		super(_windowFrame, self).__init__((x, y), self._frame_args["bk"])

		self.setRenderArgs(self._rendering_args["text"],
			 self._rendering_args["font_rendering_args"][0],
			 *self._rendering_args["font_rendering_args"][1:])

		self.setRenderArgs(*args)

		wasNone = False
		if self._frame_args["bk"] is None:
			self._frame_args["bk"] = pygame.Surface(wsize, pygame.SRCALPHA)
			wasNone = True

		self.applyFrame(wsize[0], self._frame_args["tbH"], self._frame_args["frameW"], self._frame_args[
			"frameColor"], self._frame_args["titleColor"])

		if wasNone:
			self._frame_args["bk"] = None

		self._rel = (0, 0)

	def applyFrame(self, TitleW, TitleH=30, FrameW=1, FrameColor=(111, 111, 111, 256//2), TitleColor=(111, 111, 111,
																									  256//2)):
		bk = pygame.transform.scale(self._frame_args["bk"], self._size)

		self._frame_args["tbRect"] = pygame.Rect(0, 0, TitleW, TitleH)
		self._frame_args["tbW"] = TitleH
		self._frame_args["frameW"] = FrameW

		Surface = self._args[1].render(*([self._args[0]]+self._args[2:4]))
		x, y = Surface.get_size()
		param = (TitleW-x)//2, (TitleH-y)//2

		pygame.draw.rect(bk, TitleColor, (FrameW, FrameW, TitleW, TitleH-FrameW), 0)
		bk.blit(Surface, param)
		pygame.draw.rect(bk, FrameColor, self.getRect(), FrameW)

		self._bk = bk
		self._frame_args["bk"] = bk

	def setRenderArgs(self, *args):
		"""
		:str text:
		:pygame.font.Font pyFont:
		:list rendering_args:
		"""
		super(_windowFrame, self).setRenderArgs(*args)

	def render(self):
		return self._bk

	def getMsg(self):
		return self._rel

	def update(self, RgineEvent, uMsg, absClientRect, Rect):
		self._rel = (0, 0)
		if uMsg == WindowsManager.WM_SETFOCUS:
			self._frame_args["state"] = self.FOCUS
		elif uMsg == WindowsManager.WM_KILLFOCUS:
			self._frame_args["state"] = self.NOFOCUS

		if self._frame_args["state"] == self.NOFOCUS:
			return False

		if RgineEvent.isMouseHit(RgineEvent.MOUSE_LEFT) \
				and (not absClientRect.collidepoint(RgineEvent.getMousePos())) \
				and (Rect.collidepoint(RgineEvent.getMousePos())):
			# print("init")
			self._frame_args["frameMessage"] = True
		elif RgineEvent.isMouseUp(RgineEvent.MOUSE_LEFT):
			self._frame_args["frameMessage"] = False
			# input("rel")

		if self._frame_args["frameMessage"]:
			wasDown = False
			if self._frame_args["state"] == self.FOCUS or self._frame_args["state"] == self.UP:
				if RgineEvent.isMouseDown(RgineEvent.MOUSE_LEFT):
					self._frame_args["state"] = self.DOWN
			elif self._frame_args["state"] == self.DOWN:
				if not RgineEvent.isMouseDown(RgineEvent.MOUSE_LEFT):
					self._frame_args["state"] = self.HIT
				wasDown = True
			elif self._frame_args["state"] == self.HIT:
				self._frame_args["state"] = self.UP

			if self._frame_args["state"] == self.DOWN and wasDown:
				self._rel = RgineEvent.getMouseRel()
		return True

class _windowMsgbox(windowFramed):
	# frame, icon, text, button
	# Msgbox Style
	# Buttons
	MB_OK = 0x00000000
	MB_OKCANCEL = 0x00000001
	MB_ABORTRETRYIGNORE = 0x00000002
	MB_YESNOCANCEL = 0x00000003
	MB_YESNO = 0x00000004
	MB_RETRYCANCEL = 0x00000005
	MB_CANCELTRYCONTINUE = 0x00000006

	# Icons
	MB_ICONSTOP = 0x00000010
	MB_ICONQUESTION = 0x00000020
	MB_ICONWARNING = 0x00000030
	MB_ICONINFORMATION = 0x00000040

	# Returns
	IDNORESULT = 0
	IDOK = 1
	IDCANCEL = 2
	IDABORT = 3
	IDRETRY = 4
	IDIGNORE = 5
	IDYES = 6
	IDNO = 7
	IDTRYAGAIN = 10
	IDCONTINUE = 11
	def __init__(self, wsize, winbk=None, *args):
		super(_windowMsgbox, self).__init__(wsize, winbk, *args)

		self.setRenderArgs(None, None, None, None, "Text", self.MB_OK, _button_size)
		self.setRenderArgs(*args)

		self._text = self._args[4]
		self._type = self._args[5]
		self._buttonsize = self._args[6]
		self._buttons = []
		
		b = self._type & 0x0000000f
		addbutton = (lambda x, val: self._buttons.append(
			(self._wm.CreateWindow(WindowsMacros.WC_BUTTON, (self._buttonsize, _button, x)), val)
			))
		if b == self.MB_OKCANCEL:
			addbutton("OK", self.IDOK)
			addbutton("CANCEL", self.IDCANCEL)
		elif b == self.MB_ABORTRETRYIGNORE:
			addbutton("ABORT", self.IDABORT)
			addbutton("RETRY", self.IDRETRY)
			addbutton("IGNORE", self.IDIGNORE)
		elif b == self.MB_YESNOCANCEL:
			addbutton("YES", self.IDYES)
			addbutton("NO", self.IDNO)
			addbutton("CANCEL", self.IDCANCEL)
		elif b == self.MB_YESNO:
			addbutton("YES", self.IDYES)
			addbutton("NO", self.IDNO)
		elif b == self.MB_RETRYCANCEL:
			addbutton("RETRY", self.IDRETRY)
			addbutton("CANCEL", self.IDCANCEL)
		elif b == self.MB_CANCELTRYCONTINUE:
			addbutton("CANCEL", self.IDCANCEL)
			addbutton("RETRY", self.IDRETRY)
			addbutton("CONTINUE", self.IDCONTINUE)
		else:
			addbutton("OK", self.IDOK)

		icon = self._type & 0x000000f0
		if icon == self.MB_ICONSTOP:
			self._icon = _icon_stop.copy()
		elif icon == self.MB_ICONQUESTION:
			self._icon = _icon_help.copy()
		elif icon == self.MB_ICONWARNING:
			self._icon = _icon_warning.copy()
		elif icon == self.MB_ICONINFORMATION:
			self._icon = _icon_info.copy()
		else:
			self._icon = pygame.Surface((128, 128), pygame.SRCALPHA)

		self._wm.SetTopmost(self._buttons[0][0], True)
		self._wm.SetTopmost(self._buttons[0][0], False)

		self._icon = pygame.transform.scale(self._icon, (64, 64))

		y = wsize[1]*9//10+1-self._buttonsize[1]
		if len(self._buttons):
			li = [i-self._buttonsize[0]//2 for i in range(0, wsize[0], wsize[0]//(len(self._buttons)+1))][1:]
			for i, j in zip(self._buttons, li):
				self._wm.MoveWindow(i[0], j, y)

		self._state = self.IDNORESULT
		tx, ty, w, h = self.getRelativeClientRect()

		self._surface = pygame.Surface((w, h), pygame.SRCALPHA)
		self._surface.blit(self._icon, (0, 0))
		text = render_text((wsize[0]-64, y-16), " "*8+self._text, self._args[1], *self._args[2:4])
		self._surface.blit(text, (64, 16))
		self._surf = self._surface.copy()
		self._done = False
	
	def setRenderArgs(self, *args):
		"""
		:str text:
		:pygame.font.Font pyFont:
		:list rendering_args:
		:MsgboxStyle/int ms:
		"""
		super(_windowMsgbox, self).setRenderArgs(*args)

	def init(self, hWnd):
		pass

	def getMsg(self):
		return self._state
	
	def callback_(self, RgineEvent, uMsg):
		#after done, return True for first time, set state, then return False
		self._surf = self._surface.copy()
		done = False
		if RgineEvent.isKeyHit(pygame.K_TAB) and self._wm.GetTopmost() != -1:
			topmost = self._wm.GetTopmost()
			p = 0
			for i in range(len(self._buttons)):
				p += 1
				if topmost == self._buttons[i][0]:
					break
			if p == len(self._buttons): p = 0
			self._wm.SetTopmost(self._buttons[p][0], True)
			self._wm.SetTopmost(self._buttons[p][0], False)

		for hWnd, msg, surface, pos in self._wm.DispatchMessage(RgineEvent):
			self._surf.blit(surface, pos)
			if msg == WindowsMacros.HIT:
				done = True
				for i in self._buttons:
					if i[0] == hWnd:
						self._state = i[1]
						break
				
		if self._done: return False
		else:
			if done: self._done = True
			return True
		
	def render_(self):
		return self._surf


class _windowEditbox(windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(_windowEditbox, self).__init__(wsize, winbk)
		self.setRenderArgs(*args)
		self._handle = 0
		self._surf = self._bk.copy()
		self._state = 0

		self._focus_img = pygame.Surface(wsize, pygame.SRCALPHA)
		self._focus_img.fill((111, 111, 111, 111))

		self._text = []
		self._font = pygame.font.SysFont('Times New Romen', 16)
		if self._args and isinstance(self._args[0], pygame.font.Font):
				self._font = self._args[0]
		
	def init(self, hWnd):
		self._handle = hWnd
		
		return True
	
	def callback(self, evt, uMsg):
		self._surf = self._bk.copy()
##		for hWnd, msg, surface, pos in self._wm.DispatchMessage(RgineEvent):
##			self._surf.blit(surface, pos)
		if uMsg == WindowsMacros.WM_SETFOCUS:
			self._state = WindowsMacros.FOCUS
		elif uMsg == WindowsMacros.WM_KILLFOCUS:
			self._state = WindowsMacros.NOFOCUS

		if self._state == WindowsMacros.FOCUS:
			self._surf.blit(self._focus_img, (0, 0))
			if evt.type == pygame.KEYDOWN:
				if evt.dict["key"] == pygame.K_BACKSPACE:
					if self._text: self._text.pop()
				elif evt.dict["key"] == pygame.K_RETURN:
					self._text.append("\n")
				elif evt.dict["key"] == pygame.K_TAB:
					self._text.append("\t")
				else:
					if evt.dict["unicode"]:
						self._text.append(evt.dict["unicode"])
			# if self._text: print(self._text)

		surf = render_text(self._surf.get_size(), "".join(self._text),
		            self._font, True, (255, 255, 255))
		self._surf.blit(surf, (0, 0))

		return True
	
	def render(self):
		return self._surf

	def release(self):
		self._wm.Release()

	def getMsg(self):
		return self._state

	
class _windowTab(windowBase):
	def __init__(self, wsize, winbk=None, *args):
		super(_windowTab, self).__init__(wsize, winbk)
		self.setRenderArgs(*args)

		# {button_name: getMsg return}
		self._buttonsize = self._args[0]
		self._button_img = self._args[1]
		self._buttons = []
		self._handle = 0
		self._surface = pygame.Surface(wsize, pygame.SRCALPHA)
		self._surface.blit(self._bk, (0, 0))
		self._surf = None
		self._state = 0
		self._current_tab = [0, (0, 0)]

	def init(self, hWnd):
		self._handle = hWnd
		self._state = 0
		self._buttons = []
		addbutton = (lambda x, val: self._buttons.append(
			(self._wm.CreateWindow(WindowsMacros.WC_BUTTON, (self._buttonsize, self._button_img, x)), val)
			))
		cx = 0
		for i in self._args[2]:
			addbutton(*i)
			self._wm.MoveWindowToPos(self._buttons[-1][0], cx, 0)
			cx += self._buttonsize[0]

		if self._buttons:
			self._wm.SendMessage(self._buttons[-1][0], WindowsMacros.WM_KILLFOCUS)
			self._state = self._buttons[0][1]
			self._current_tab[0] = self._buttons[0][0]
			self._current_tab[1] = (0, 0)

		return True

	def callback(self, RgineEvent, uMsg):
		self._surf = self._surface.copy()

		for hWnd, msg, surface, pos in self._wm.DispatchMessage(RgineEvent):
			if msg == WindowsMacros.HIT:
				for i in self._buttons:
					if i[0] == hWnd:
						self._state = i[1]
						self._current_tab[0] = hWnd
						self._current_tab[1] = pos
						continue
			elif msg == WindowsMacros.UP:
				self._wm.SetTopmost(-1, False)
			self._surf.blit(surface, pos)

		inst = self._wm.getInstance(self._current_tab[0])
		if inst is not None:
			t = inst._state
			inst._state = WindowsMacros.HIT
			surf = inst.render()
			self._surf.blit(surf, self._current_tab[1])
			inst._state = t

		return True

	def render(self):
		return self._surf

	def release(self):
		self._wm.Release()

	def getMsg(self):
		return self._state


def _main():
	# uin = input("input 'f' or  'F' to see the framed example\ninput anything else to see the unframed example\n-> ")
	uin = "f"
	if uin.lower() == "f":
		framed = True
	else:
		framed = False
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	tw = _windowText((158, 59), None)
	tw.setRenderArgs("Hello World!", pygame.font.SysFont('Times New Romen', 16), True, (255, 255, 255))
	s = tw.render()
	screen.blit(s, (0, 0))

	wm = WindowsManager()
	def init(self, hWnd):   #init
		print("Hello World! From hWnd: %d" % hWnd)


		self._button0 = self._wm.CreateWindow(WindowsMacros.WC_BUTTON, (_button_size, _button, "Button 0",
												  pygame.font.SysFont('Times New Romen', 16),
												  True, (255, 255, 255)), True)

		self._text0 = self._wm.CreateWindow(WindowsMacros.WC_TEXT, ((80, 10), None, "Bye World!",
												pygame.font.SysFont('Times New Romen', 16),
												True, (255, 255, 255)), True)

		self._button1 = self._wm.CreateWindow(WindowsMacros.WC_BUTTON, ((158//2, 59//2), _button, "Button 1"))
												  # pygame.font.SysFont('Times New Romen', 16),
												  # True, (255, 255, 255)), True)

		self._wm.MoveWindow(self._button0, 20, 25)
		self._wm.MoveWindow(self._button1, 200-158//2, 200-59//2)
		self._handle = hWnd
		self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)

	def cb(self, event, uMsg):  #callback
		self._bk_ = pygame.Surface(self.getClientSize(), pygame.SRCALPHA)
		for hWnd, msg, surface, pos in self._wm.DispatchMessage(event):
			self._bk_.blit(surface, pos)
			if hWnd == self._button0 and msg == WindowsMacros.HIT:
				print("%d Subwindow Button 0 Hit!"%(self._handle-10))
			elif hWnd == self._button1 and msg == WindowsMacros.HIT:
				print("%d Subwindow Button 1 Hit!"%(self._handle-10))

		return True

	def rd(self):   #render
		return self._bk_

	def getMsg(self):
		return 0

	def rel(self):  #release
		self._wm.Release()

	surf = pygame.Surface((200, 200), pygame.SRCALPHA)
	surf.fill((128, 128, 128, 256*2//3))
	hwnd0 = wm.CreateWindow(wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf, "this is 0",
												  pygame.font.SysFont('Times New Romen', 16),
												  True, (255, 255, 255)))
	hwnd1 = wm.CreateWindow(wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf, "this is 1",
											  pygame.font.SysFont('Times New Romen', 16),
											  True, (255, 255, 255)))
	hwnd2 = wm.CreateWindow(wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf, "this is 2",
											  pygame.font.SysFont('Times New Romen', 16),
											  True, (255, 255, 255)))
	hwnd3 = wm.CreateWindow(wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf, "this is 3",
											  pygame.font.SysFont('Times New Romen', 16),
											  True, (255, 255, 255)))
	hwnd4 = wm.CreateWindow(wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf, "this is 4"))
											  # pygame.font.SysFont('Times New Romen', 16),
											  # True, (255, 255, 255)))
	wm.getInstance(hwnd4)._wm.CreateWindow(wm.getInstance(hwnd4)._wm.RegisterClass(framed, init, cb, rd, getMsg, rel), ((200, 200), surf,
	                                                                                             "this is 4x"))
	ychg = 0
	xchg = 0
	for i in range(5):
		if xchg*200 >= 800:
			xchg = 0
			ychg += 200
		wm.MoveWindow(eval("hwnd"+str(i)), xchg*200, ychg)
		xchg += 1
	evt = event.Event()

	import time
	t = time.clock()
	fps = 0

	msgbox = wm.CreateWindow(WindowsMacros.WC_MSGBOX,
				 ((400, 200), None, "MessageBox!", None, None, None,
				  "Good Morning! How Are You? ",
				  WindowsMacros.MB_ICONWARNING | WindowsMacros.MB_CANCELTRYCONTINUE
				  , [_button_size[0]//2, _button_size[1]//2]))
	wtab = 0
	# wtab = wm.CreateWindow(WindowsMacros.WC_TAB, ((400, 200), pygame.Surface((400, 200)),
	# 					      (100, 100), pygame.Surface((100, 100)),
	# 					      [("1", 2), ("2", 1), ("3", 3), ("4", 4)])
	# )

	weditbox = wm.CreateWindow(WindowsMacros.WC_EDITBOX, ((200, 100), None))

	p.enable()
	running = True
	while running:
		
		evt.update()
		
		if evt.type == pygame.QUIT:
			running = False
		screen.fill((0, 0, 0))
		wm.SetTopmost(15)
		for hWnd, msg, surface, pos in wm.DispatchMessage(evt):
			screen.blit(surface, pos)
			if hWnd == msgbox:
				if msg != WindowsMacros.IDNORESULT:
					print("Messagebox %d !"%msg)
			if hWnd == wtab:
				print(msg)
		pygame.display.flip()

		fps += 1
		if time.clock() - t >= 20000000:
			break
		# print(fps, time.clock()-t)
		# print("Current Topmost: %d"%(wm._current["topmost"]-10))
		# fps = 0
		# t = time.clock()
	wm.Release()
	pygame.quit()

	p.disable()
	p.print_stats()
	input()
	return 0

if __name__ == "__main__": exit(_main())
