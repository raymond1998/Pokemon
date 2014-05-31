import pygame
from base import *

_scrsize = [0, 0]
_texturesize = 0
def init(scrsize, texturesize):
	global _scrsize, _texturesize
	_scrsize = scrsize[:]
	_texturesize = texturesize

class MapManager(object):
	def __init__(self):
		self.maps = {}
		self._current = None

	def add(self, map_inst):
		self.maps[tuple(map_inst.getRect())] = map_inst

	def getMap(self, uPos):
		for i in self.maps:
			if pygame.Rect(*i).collidepoint(*uPos):
				self._current = i
				return self.maps[i]
		raise ValueError(uPos)

	def getCurrentMap(self):
		return self.maps[self._current]


class Map(object):
	def __init__(self, terrain, starting_oft):
		self.sx, self.sy = starting_oft
		self.terrain = terrain
		self.terrain.setShift(*starting_oft)

		self.world = rgine.TerrainWorld(terrain.width*terrain.textureW, terrain.height*terrain.textureH)
		self.world.setProjectionSize(*_scrsize)
		self.world.setTextureFormat(_texturesize, _texturesize)
		self.world.setTerrainShift(*starting_oft)

	def getRect(self):
		return pygame.Rect(self.sx, self.sy, self.terrain.width, self.terrain.height)

	# def getShift(self):
	# 	return self.sx, self.sy
