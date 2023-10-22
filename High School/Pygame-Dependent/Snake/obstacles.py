#Imports functions and variables from other files
import Globals as g
import gameFunctions as gf
import pygame

def createObstacle(): #Creates the obstacles
  if g.obstacle == 1: #Only works if the obstacle option is true
    obstaclex = gf.rand('x') #Randomizes the location of the obstacles
    obstacley = gf.rand('y')
    g.obstacles.append((obstaclex, obstacley)) #Adds the obstacle to the array

def drawObstacle():
  if g.obstacle == 1: #Only works if the obstacle option is true
    for x,y in g.obstacles: #Draws the obstacles in the array in red
      pygame.draw.rect(g.dis, gf.col(g.red), [x, y, g.snake_block, g.snake_block])

def checkObstacle():
  if g.obstacle == 1: #Only works if the obstacle option is true
    for x,y in g.obstacles:
      if g.x1 == x and g.y1 == y:
        print("HIT OBSTACLE")
        g.game_over = True
        #Checks if the player/snake has hit the obstacle, ending the game if this is the case