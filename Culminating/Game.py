import pygame as pg
import Globals as g
import Menu as m
import Functions as f
from random import randint

#Changes game colors based on level
def easter_eggs():
  if 25 <= g.level and g.level < 30: g.colors["green"] = (randint(0, 255), randint(0, 255), randint(0, 255))
  if 30 <= g.level and g.level < 40: g.colors["red"] = (randint(0, 255), randint(0, 255), randint(0, 255))
  if 40 <= g.level: g.colors["yellow"] = (randint(0, 255), randint(0, 255), randint(0, 255))
  if not (g.background_count and g.platform_count):
    return True
  return False

#draws the game board on the screen
def draw_board():
  #Draws background based on colour
  for y in range(len(g.stage)):#Loops through 2d array of game board
    for x in range(len(g.stage[y])):
      if g.stage[y][x] == 1: g.platform_count += 1
      elif g.stage[y][x] == 0: g.background_count += 1
      fix_screen(y, x)

#Draws a given square in the correct color
def fix_screen(y, x):
  if block_type(y, x) == "background": pg.draw.rect(g.board, g.colors["black"], f.rect(y, x))
  elif block_type(y, x) == "platform": pg.draw.rect(g.board, f.darken_color(g.colors["green"], f.scalars("color", y, x)), f.rect(y, x))
  elif block_type(y, x) == "goal": pg.draw.rect(g.board, g.colors["yellow"], f.rect(y, x))

#Returns a string representation of the type of block located at (y,x)
def block_type(y, x):
  val = g.stage[y][x]
  if val <= 0: return "background"
  if 0 < val and val <= 1: return "platform"
  if val == 2: return "goal"

#If the block (y,x) is within game bounds
def block_in_range(y, x):
  return int(y) in range(int(g.height/g.size)) and int(x) in range(int(g.width/g.size))

#Generates field
def create_board():
  #To generate background
  g.stage = []
  for h in range(int(g.height/g.size)):
    row = []#creates a row to be filled
    for w in range(int(g.width/g.size)):
      if w != 0 and row[w-1]: box = f.rnd(10) #platform continuation probability
      else: box = not f.rnd(15) #background probability generation
      row.append(bool(box))
    row[0] = 0
    row[int(g.width/g.size)-1] = 0 #trims row so blocks fit in game size
    g.stage.append(row) #saves row

  #To generate goal
  goals = []
  for y in range(len(g.stage)):
    for x in range(len(g.stage[y])):
      if block_in_range(y+1, x) and block_in_range(y-1, x):
        if block_type(y+1, x) == "platform" and block_type(y-1, x) == "background": goals.append((y, x))

  goal = goals[f.scalars("goals", len(goals))]
  g.stage[goal[0]][goal[1]] = 2
  g.background_count -= int(g.height/g.size) + 1

  draw_board()#Draws the created field to the screen
  pg.display.update()

#Check for key presses
def register_events():
  pg.event.pump()#pumps event handle to get presses
  keys = pg.key.get_pressed()#checks for movement keys
  g.x_change = keys[pg.K_RIGHT]-keys[pg.K_LEFT]
  g.y_change = keys[pg.K_DOWN]-keys[pg.K_UP]

  for event in pg.event.get():
    if event.type == pg.KEYDOWN: #looks for presses
      if event.key == pg.K_b: g.breaking = not g.breaking #switch break mode
      if event.key == pg.K_c: m.color_util() #opens color changer
      if event.key == pg.K_l: m.leaderboard() #opens leaderboard
      if event.key == pg.K_h:
        if m.help() == 0: return 0 #opens help (0 means quit)
      if event.key == pg.K_q: return 0 #Quit game

    if event.type == pg.MOUSEBUTTONDOWN: #checks for clicks
      x, y = int(event.pos[0]/g.size), int(event.pos[1]/g.size) #gets location of press
      if block_in_range(y, x): #if it's a valid press
        if abs(g.x-x) <=2 and abs(g.y-y) <=2: #if its nearby
            #Breaking
            if g.breaking:
              if block_type(y, x) == "platform":
                if g.stage[y][x] == 1: g.broken += 1 #records new breaks for score penalty
                g.stage[y][x] = f.scalars("click_platform", y, x) #lowers block integrity
                if g.stage[y][x] <= 0: #upon complete destruction
                  g.broken_total += 1 #records break for inventory
                  g.background_count += 1 #records count change for easter eggs
                  g.platform_count -= 1
            #Placing
            elif not g.breaking:
              if block_type(y, x) == "background" and g.broken_total > 0: #if inventory has blocks
                g.broken_total -= 1 #removes block from inventory
                g.background_count -= 1 #records count change for easter eggs
                g.platform_count += 1
                g.stage[y][x] = 1 #sets block to platform type

        fix_screen(y, x) #Changes the block color based on the click
  return 1;

#1 round of the game
def level():
  clock = pg.time.Clock() #timer
  no_fall_count = 0 #gravity
  while (True):
    if not register_events(): #Quit game
      f.clear() #if user wanted to quit
      if 'y' in input("Are you sure you want to quit?\n").lower(): return 0
      else: print("Not quitting.\n")
    m.draw_menu(False, False, True, False, True, True) #Updates values at the bottom
    
    #Player Turn
    fix_screen(g.y, g.x)
    if block_in_range(g.y+g.y_change, g.x+g.x_change):
      if block_type(g.y+g.y_change, g.x+g.x_change) != "platform":
        g.x += g.x_change
        g.y += g.y_change
        #Checks if in the air
        if g.y <= g.height/g.size-2 and block_type(g.y+1, g.x) != "platform": no_fall_count += 1
        else: no_fall_count = 0

    #Gravity
    if no_fall_count > 2: #If airtime is more than 2 cycles
      no_fall_count = 0
      fix_screen(g.y, g.x)
      while g.y <= g.height/g.size-2 and block_type(g.y+1, g.x) != "platform": g.y += 1 #Drops them back down

    #Auto platform breaking
    x, y = (g.x, g.y+1)
    if block_in_range(y, x):
      if block_type(y, x) == "platform": g.stage[y][x] -= f.scalars("auto_platform") #Makes blocks take a little damage
      fix_screen(y, x)

    #Screen Update
    pg.draw.rect(g.board, g.colors["red"], f.rect(g.y, g.x)) #draws the player in their updated position
    pg.display.update()
    clock.tick(g.speed)

    #Exit conditions
    if(easter_eggs()):
      g.level = 51
      g.board.fill((0, 0, 0))
      return 2
    if g.stage[g.y][g.x] == 2:
      g.score += f.scalars("score")
      g.level += 1
      if g.level >= 30: g.colors["green"] = (70, 180, 70)
      if g.level >= 40: g.colors["red"] = (213, 50, 80)
      return 1