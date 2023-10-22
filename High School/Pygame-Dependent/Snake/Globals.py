import pygame
import gameFunctions as gf
import autopilots as a

pygame.init() #Initates the pygame program

keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s] #Array to store the different movements keys avaliable

autos = [a.none, a.default, a.simple, a.diagonal, a.smart] #Array to store the different autopolits avaliable, smart doesn't work

#Colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (230,30,250)

#Sets the width and height of the screen
dis_width = 800
dis_height = 600

#Title of the game
dis = pygame.display.set_mode((dis_width, dis_height))

#Variables for starting and ending the game
game_over = False
playing = True

#Starts your character at the center
x1 = 0
y1 = 0

#Variables of storing where you are
x_change = 0
y_change = 0

#Coordinates of the snake, as well as its overall length
snake_list = []
obstacles = []
high_score = 0

#Determines the initial size and speed of the snake
snake_block = 10
snake_speed = 15

#Randomizes the location of the food
foodx = 0
foody = 0

#Fonts for the game
font1 = pygame.font.SysFont("bahnschrift", 25)
font2 = pygame.font.SysFont("comicsansms", 35)

#Variables for customisation
invert = -1
auto = 0
obstacle = 1

#Function to reset game values
def resetVars():
  global game_over, game_close, x1, y1, x_change, y_change, snake_list, obstacles, foodx, foody
  game_over = False
  game_close = False
  x1 = gf.rand('x')
  y1 = gf.rand('y')
  x_change = 0
  y_change = 0
  snake_list = []
  obstacles = []
  foodx = gf.rand('x')
  foody = gf.rand('y')