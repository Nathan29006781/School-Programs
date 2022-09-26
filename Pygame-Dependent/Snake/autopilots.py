#Importing variables and functions from other files
import pygame
import gameFunctions as gf
import Globals as g

#Autos call none() after, so user can still override the autopilot

#User control
def none():
  #Movement for the snake, compatable with ASWD and Arrow Keys
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == g.keys[0] or event.key == g.keys[4]: gf.updateDir(g.invert, 0)
      elif event.key == g.keys[1] or event.key == g.keys[5]: gf.updateDir(-g.invert, 0)
      elif event.key == g.keys[2] or event.key == g.keys[6]: gf.updateDir(0, g.invert)
      elif event.key == g.keys[3] or event.key == g.keys[7]: gf.updateDir(0, -g.invert)

  g.x1 += g.x_change
  g.y1 += g.y_change

#Goes to each food first in the y, then x
def default():
  if g.y1 != g.foody: gf.updateDir(0, gf.foodDirection('y'))
  else: gf.updateDir(gf.foodDirection('x'), 0)
  none()

#Makes the turn for you if headed in the right direction
def simple():
  if g.x_change == 0:
    if g.y1 == g.foody: gf.updateDir(gf.foodDirection('x'), 0)
  elif g.y_change == 0:
    if g.x1 == g.foodx: gf.updateDir(0, gf.foodDirection('y'))
  none()

#Goes diagonally to each food
def diagonal():
  gf.updateDir(gf.foodDirection('x'), gf.foodDirection('y'))
  none()

#Smart kinda failed, oops
#0 is x, 1 is y
prevFoodX = False
prevFoodY = False
def smart():
  global direction, prevFoodX, prevFoodY
  gf.updateDir(gf.foodDirection('x'), 0)

  prevFoodX = (g.x1 == g.foodx)
  prevFoodY = (g.y1 == g.foody)

  if prevFoodX == True:
    gf.updateDir(0, gf.foodDirection('y'))
    prevFoodX = False
  elif prevFoodY == True:
    gf.updateDir(gf.foodDirection('x'), 0)
    prevFoodY = False

  colorAhead = g.dis.get_at((g.x1+g.x_change, g.y1+g.y_change))
  if colorAhead != g.blue and colorAhead != g.green:
    print("TRYING TO AVOID")
    if g.x_change == 0: gf.updateDir(gf.foodDirection('x'), 0)
    if g.y_change == 0: gf.updateDir(0, gf.foodDirection('y'))

  none()