#Importing variables from other files
import pygame
import random
import Globals as g

pygame.display.set_caption('Snake Game by Will and Nathan')
#Used to set up screen updates
clock = pygame.time.Clock()

def col(color): #Function used for rainbow snake colour
  if len(g.snake_list) > 35: return (random.randrange(255), random.randrange(255), random.randrange(255))
  else: return color

#Function for defining score
def printScore():
  if len(g.snake_list) > g.high_score: g.high_score = len(g.snake_list)
  score_text = g.font2.render("Your Score: " + str(len(g.snake_list)), True, col(g.yellow))
  high_score_text = g.font2.render("High Score: " + str(g.high_score), True, col(g.yellow))
  g.dis.blit(score_text, (g.dis_width-score_text.get_width()-5, g.dis_height-score_text.get_height()-25))
  g.dis.blit(high_score_text, (g.dis_width-high_score_text.get_width()-5, g.dis_height-high_score_text.get_height()))

#Function to display the snake
def drawSnake():
  if len(g.snake_list) <= 15: #If the user has lower than 15 score, the snake is printed black
    for coord in g.snake_list:
      pygame.draw.rect(g.dis, g.black, [coord[0], coord[1], g.snake_block, g.snake_block])
  elif len(g.snake_list) <= 25: #If the user has between 15 and 25 score, the snake is printed yellow
   for coord in g.snake_list:
    pygame.draw.rect(g.dis, g.yellow, [coord[0], coord[1], g.snake_block, g.snake_block])
  elif len(g.snake_list) <= 35: #If the snake is between 25 and 35 score, the snake is printed purple
   for coord in g.snake_list:
    pygame.draw.rect(g.dis, g.purple, [coord[0], coord[1], g.snake_block, g.snake_block])
  else:
    for coord in g.snake_list: #Rainbow snake if the user is above 35 score
      pygame.draw.rect(g.dis, col(g.red), [coord[0], coord[1], g.snake_block, g.snake_block])

#Function to check if number is positive or negative
def sign(num):
  if num == 0: return 0
  elif num > 0: return 1
  else: return -1

def foodDirection(location): #Function to determine the location of the food
  if location == 'x': return sign(g.foodx-g.x1)
  if location == 'y': return sign(g.foody-g.y1)

def state(num): #Function for converting bool values to corresponding string
  if num == -1: return "FALSE"
  if num == 1: return "TRUE"

def updateDir(x, y): #Function that is utilized to update and change the direction of the snake
  # if sign(g.x_change) == -x and sign(g.y_change) == -y: return #Prevents 180 turn which is instant death
  g.x_change = x*g.snake_block
  g.y_change = y*g.snake_block

def rand(direction): #Function for determining a random location (used for the food and the obstacles and programmed to match the size of the snake, which can be adjustable)
  if direction == 'x':
    return round(random.randrange(0, g.dis_width - g.snake_block) / g.snake_block) * g.snake_block
  if direction == 'y':
    return round(random.randrange(0, g.dis_height - g.snake_block) / g.snake_block) * g.snake_block