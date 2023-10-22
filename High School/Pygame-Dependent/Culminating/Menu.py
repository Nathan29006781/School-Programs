import pygame as pg
import Globals as g
import Functions as f
import Game
from time import time

#To print text to the screen
def prnt_to_scrn(msg, color, x, y):
  font = pg.font.SysFont("comicsansms", 30)
  text = font.render(msg, False, color)
  g.board.blit(text, (x, y+g.height))

#Rectangle to block previous text for overwriting
def rect(x=75, y=0, x_size=75, y_size=25):
  return pg.Rect(x, g.height+y, x_size, y_size)

#Draws any amount of data to the screen based on the parameters
def draw_menu(menu, level, score, total, inventory, breaking):
  if menu: #Titles and game area
    g.board.fill(g.colors["black"])

    w, h = pg.display.get_surface().get_size() #Actual screen size
    pg.draw.rect(g.board, g.colors["white"], [0, g.height, w, h-g.height]) #Setting up game borders
    pg.draw.rect(g.board, g.colors["brown"], [0, g.height-g.size+1, w, g.size-1])
    pg.draw.rect(g.board, g.colors["brown"], [g.width-g.size*2, 0, 100, g.height])
    prnt_to_scrn(f"Level:", g.colors["blue"], 0, 0) #Various data labels
    prnt_to_scrn(f"Score:", g.colors["blue"], 0, 20)
    prnt_to_scrn(f"Inventory:", g.colors["blue"], 0, 40)
    prnt_to_scrn(f"Total Score:", g.colors["blue"], g.width-215, 0)
    prnt_to_scrn(f"Action:", g.colors["blue"], g.width-215, 20)
    prnt_to_scrn(f"Press H for Help", g.colors["blue"], g.width/2-75, 0)
  if level:
    pg.draw.rect(g.board, g.colors["white"], rect())
    prnt_to_scrn(str(g.level), g.colors["blue"], 75, 0)
  if score:
    pg.draw.rect(g.board, g.colors["white"], rect(75, 20))
    prnt_to_scrn(str(f.scalars('score')), g.colors["blue"], 75, 20)
  if inventory:
    pg.draw.rect(g.board, g.colors["white"], rect(120, 40))
    prnt_to_scrn(str(g.broken_total), g.colors["blue"], 120, 40)
  if total:
    pg.draw.rect(g.board, g.colors["white"], rect(g.width-70, 0))
    prnt_to_scrn(str(g.score), g.colors["blue"], g.width-70, 0)
  if breaking:
    pg.draw.rect(g.board, g.colors["white"], rect(g.width-120, 20, 120))
    prnt_to_scrn("Breaking" if g.breaking else "Placing", g.colors["blue"], g.width-120, 20)

  pg.display.update()

#Displays leaderboard
def leaderboard():
  pause_time = time() #Saves current time
  ranking = []
  for user in g.users: #Sort players
    ranking.append(user[:3])
  ranking.sort(key=lambda x: -int(x[2])) #To sort by score in descending order

  g.board.fill(g.colors["white"])

  #shows a max of 10 players
  count = min(len(ranking), 11)
  for i in range(count):
    user = ranking[i] #prints user info in the correct location for their rank
    prnt_to_scrn(f"{i+1}: {user[0]}", (255*i/(count-1),255*(1-i/(count-1)),0), 50, g.height*(i/count-1)+50)
    prnt_to_scrn(f"{user[1]}   {user[2]}", (0, 0, 0), g.width-200, g.height*(i/count-1)+50)

  prnt_to_scrn("Press Enter to go back", (0, 0, 0), g.width/2-100, 50)

  pg.display.update() 

  #check for enter key to exit
  while True:
    for event in pg.event.get():
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
          break
    else: continue #Weird syntax but lets me leave the loop upon 'enter'
    break

  g.start_time += time()-pause_time #Catches up game time to real time
  draw_menu(True, True, True, True, True, True) #Redraws game
  Game.draw_board()


def color_util():
  pause_time = time() #Saves current time
  settings = [ #Colors for various things
    ["Blocks:", "green", 85],
    ["Player:", "red", 135],
    ["Goal:", "yellow", 185],
    ["Background:", "black", 235],
    ["Floor:", "brown", 285],
    ["Text:", "blue", 335],
  ]

  g.board.fill(g.colors["white"])

  #Prints the color changer to the screen
  for setting in settings:
    pg.draw.rect(g.board, g.colors[setting[1]], [200, setting[2]-10, 35, 35])
    prnt_to_scrn(setting[0], (0,0,0), 50, setting[2]-g.height)
  index = 0
  setting = settings[index]
  pg.draw.rect(g.board, (0, 0, 0), [45, setting[2]-10, 120, 35])
  prnt_to_scrn(setting[0], g.colors["white"], 50, setting[2]-g.height)
  f.clear()

  #cycles through each color
  while True:
    pg.display.update() #shows color to the screen
    setting=settings[index]
    pg.draw.rect(g.board, (255, 255, 255), [45, setting[2]-10, 120, 35])
    prnt_to_scrn(setting[0], (0,0,0), 50, setting[2]-g.height)
    
    #gets user input
    color = 0
    while True:
      color = input(f"\033[0mEnter a hex color code for {setting[0]} (leave blank for no change) ")
      if not color: #for blank input
        color = g.colors[setting[1]]
        f.clear()
        break
      try: #Tries to use the new code
        color = (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))
        f.clear()
        break
      except:
        f.clear()
        print("\033[31mInvalid Code")

    #saves color
    g.colors[setting[1]] = color
    pg.draw.rect(g.board, g.colors[setting[1]], [200, setting[2]-10, 35, 35])

    #Advances to next color
    index += 1
    if index == 6: break
    setting=settings[index]
    pg.draw.rect(g.board, (0, 0, 0), [45, setting[2]-10, 120, 35])
    prnt_to_scrn(setting[0], g.colors["white"], 50, setting[2]-g.height)
  
  g.start_time += time()-pause_time #Catches up game time to real time
  draw_menu(True, True, True, True, True, True)
  Game.draw_board()

#Instruction screen
def help():
  pause_time = time() #Saves current time
  g.board.fill((180, 125, 220))

#List of choices to do
  settings = [
    ["Press C to change colors", 30],
    ["Press B to change breaking mode", 70],
    ["Press L to see leaderboards", 110],
    ["Press R to return to game", 150],
    ["Press Q to save and quit game", 190],
  ]

  #print gameplay instructions
  prnt_to_scrn("INSTRUCTIONS:", (0,0,0), 25, 300-g.height)
  prnt_to_scrn("In this game, you are a single 'red' block trying to get to the 'yellow' block.", (0,0,0), 25, 325-g.height)
  prnt_to_scrn("Jump on the 'green' platforms to get to your goal. The game will get harder the", (0,0,0), 25, 350-g.height)
  prnt_to_scrn("longer you play. Blocks you stand on can break from under you. Watch out!", (0,0,0), 25, 375-g.height)
  prnt_to_scrn("You may break/place blocks near you. However your score will take a hit!", (0,0,0), 25, 400-g.height)
  prnt_to_scrn("You are able to pass through gaps and stick to blocks above and to the side.", (0,0,0), 25, 425-g.height)
  prnt_to_scrn("Use these to your advantage. And most of all HAVE FUN!", (0,0,0), 25, 450-g.height)

  #prints the choices
  for setting in settings: prnt_to_scrn(setting[0], (0,0,0), 50, setting[1]-g.height)

  pg.display.update()

  while True: #checks for key presses
    for event in pg.event.get():
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_b: g.breaking = not g.breaking
        elif event.key == pg.K_c: color_util()
        elif event.key == pg.K_l: leaderboard()
        elif event.key == pg.K_r: #go to game
          g.start_time += time()-pause_time #Catches up game time to real time
          draw_menu(True, True, True, True, True, True)
          Game.draw_board()
          pg.display.update()
          return 1 #Return to game
        elif event.key == pg.K_q: #quit
          g.start_time += time()-pause_time #Catches up game time to real time
          draw_menu(True, True, True, True, True, True)
          Game.draw_board()
          pg.display.update()
          return 0 #Quit game

        #redraw instructions if anything was pressed
        g.board.fill((180, 125, 220))
        prnt_to_scrn("INSTRUCTIONS:", (0,0,0), 25, 300-g.height)
        prnt_to_scrn("In this game, you are a single 'red' block trying to get to the 'yellow' block.", (0,0,0), 25, 325-g.height)
        prnt_to_scrn("Jump on the 'green' platforms to get to your goal. The game will get harder the", (0,0,0), 25, 350-g.height)
        prnt_to_scrn("longer you play. Blocks you stand on can break from under you. Watch out!", (0,0,0), 25, 375-g.height)
        prnt_to_scrn("You may break/place blocks near you. However your score will take a hit!", (0,0,0), 25, 400-g.height)
        prnt_to_scrn("You are able to pass through gaps and stick to blocks above and to the side.", (0,0,0), 25, 425-g.height)
        prnt_to_scrn("Use these to your advantage. And most of all HAVE FUN!", (0,0,0), 25, 450-g.height)

        for setting in settings: prnt_to_scrn(setting[0], (0,0,0), 50, setting[1]-g.height)

        pg.display.update()