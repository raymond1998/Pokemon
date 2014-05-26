import os
import sys
full_path = os.path.realpath(__file__)
sys.path.insert(0, os.path.dirname(full_path))

from exception import *
from event import *
from terrain import *
from progressbar import *
from world import *
from loader import *
import buildinfo

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
__version__ = buildinfo.get(path+"/__init__")
__author__ = 'Charles-Jianye Chen'
sys.path.pop(0)
