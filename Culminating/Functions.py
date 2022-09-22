import pygame as pg
import Globals as g
import math
from random import randint
from time import time
from os import system

#Returns a random integer up to the given number
def rnd(rnd_max): return randint(0,rnd_max)

#Creates an in game box scaled for the game size
def rect(y, x): return pg.Rect(x*g.size, y*g.size, g.size, g.size)

#Clears terminal
def clear(): system("clear")

#Returns a color tuple with lower brightness (scaled by magnitude) than the input color
def darken_color(color, magnitude): return (int(color[0]*magnitude), int(color[1]*magnitude), int(color[2]*magnitude))

#Game variables that are scaled throughout gameplay
#Returns the scaled version of some constant based on two optional parameters
def scalars(scale, param1=0, param2=0):
  if scale == "goals": return int(param1-g.level*param1/51-1)
  elif scale == "color": return g.stage[param1][param2]**(1/6)
  elif scale == "speed": return 0.1*g.level + 5
  elif scale == "size": return int(35*0.96**g.level)
  elif scale == "auto_platform": return 0.1-math.sqrt(100-2*g.level)/100
  elif scale == "click_platform": return round(g.stage[param1][param2]-(0.1-math.sqrt(2*g.level)/100), 2)
  elif scale == "score":
    t = time()-g.start_time
    return int(max(500-200*(t+g.broken)/(g.level+4)-2*t+10*g.level, 0))