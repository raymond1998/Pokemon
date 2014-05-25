import pygame

from common import *


class World(object):
		def __init__(self, width, height):
			self._size = [width, height]
			self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
			self._rect = [0, 0, width, height]

		def setProjectionSize(self, width, height):
			self._rect[2] = width
			self._rect[3] = height

		def setShift(self, x, y):
			self._rect[0] = x
			self._rect[1] = y

		def resize(self, width, height):
			self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
			self._size = [width, height]

		def new(self):
			self._surface = pygame.Surface((width, height), pygame.SRCALPHA)

		def clear(self, alpha=255, rect=None, flag=pygame.BLEND_RGBA_SUB):
			self._surface.fill((0, 0, 0, alpha), rect, flag)

		def shiftH(self, shift):
			self._rect[0] += shift
			if self._rect[0] < 0: self._rect[0] = 0
			elif self._rect[0] > self._size[0] - self._rect[2]:
					self._rect[0] = self._size[0] - self._rect[2]

		def shiftV(self, shift):
			self._rect[1] += shift
			if self._rect[1] < 0: self._rect[1] = 0
			elif self._rect[1] > self._size[1] - self._rect[3]:
					self._rect[1] = self._size[1] - self._rect[3]

		def render(self):
			return self._surface.subsurface(self._rect)

		def render_s(self):
			if self._rect[0] < 0: self._rect[0] = 0
			elif self._rect[0] > self._size[0] - self._rect[2]:
					self._rect[0] = self._size[0] - self._rect[2]
			if self._rect[1] < 0: self._rect[1] = 0
			elif self._rect[1] > self._size[1] - self._rect[3]:
					self._rect[1] = self._size[1] - self._rect[3]
			try:
				return self.render()
			except ValueError:
				x, y, w, h = self._rect
				width, height = self._surface.get_size()
				if x+w > width or x < 0:
					w = min([width, w])
					x = width - w
				if y+h > height or y < 0:
					h = min([height, h])
					y = height - h
				self._rect = [x, y, w, h]
				# print(self._rect)
				return self.render()

		def blit(self, surface, pos):
			return self._surface.blit(surface, pos)

		def getShift(self):
			return self._rect[:2]

		def getSurface(self):
			return self._surface

		def getRect(self):
			return self._rect

		def getSize(self):
			return tuple(self._size)

		def transform(self, rect):
			x, y, w, h = rect
			return pygame.Rect(x-self._rect[0], y-self._rect[1], w, h)

class TerrainWorld(World):
	def __init__(self, width, height):
		super(TerrainWorld, self).__init__(width, height)
		self._textureW = 1
		self._textureH = 1

	def setTextureFormat(self, textureWidth, textureHeight):
		self._textureW = textureWidth
		self._textureH = textureHeight

	def getTerrainRange(self):
		x, y, w, h = self._rect
		return [x//self._textureW, (x+w)//self._textureW], [y//self._textureH, (y+h)//self._textureH]

	def Terrain2World(self, x, y):
		return x*self._textureW, y*self._textureH

def getTerrainByPos(terrain, mouseX, mouseY, shiftX, shiftY):
		a, b = terrain.getTerrainByRelativeRect((mouseX-shiftX, mouseY-shiftY, 0, 0))
		return a[0], b[0]