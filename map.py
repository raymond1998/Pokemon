import pygame
from base import *
class MapManager(object):
    def __init__(self):
        self.maps = {}

    def add(self, map_inst):
        self.maps[(map_inst.sx, map_inst.sy)] = map_inst

    def chg(self, nxt, offset):
        pass

        
class Map(object):
    def __init__(self, terrain, starting_oft):
        self.sx, self.sy = starting_oft
        self.terrain = terrain

    def getRect(self):
        return pygame.Rect(self.sx, self.sy, self.terrain.width, self.terrain.height

