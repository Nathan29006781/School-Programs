import pygame as pg
import Functions as f
from time import time

#Base game variables
users = []
width = 800
height = 400
board = pg.display.set_mode((width, height+100))

#Color dictionaries of default values (can be overriden by user)
colors = {
  "white": (255, 255, 255),
  "yellow": (255, 255, 102),
  "black": (10, 5, 0),
  "red": (213, 50, 80),
  "green": (70, 180, 70),
  "blue": (50, 153, 213),
  "brown": (80, 50, 35)
}

#Gameplay variables
level = 0
size = 0
speed = 0
score = 0
broken = 0

#Score variables
broken_total = 0
start_time = 0

#Easter egg variables
platform_count = 0
background_count = 0

#Action mode flag
breaking = True

#Movement variables
x = 0
y = 0
x_change = 0
y_change = 0

#2d array that contains game field
stage = []

#Resets variables (called on new round)
def set_vars():
  global size, speed, height, width, x, y, x_change, y_change, broken, start_time, platform_count, background_count
  
  size = f.scalars("size")
  speed = f.scalars("speed")

  height = round(height/size)*size-1
  width = round(width/size)*size-1

  x = 0
  y = int(height/size)-1
  x_change = 0
  y_change = 0

  broken = 0
  start_time = time()

  platform_count = 0
  background_count = 0