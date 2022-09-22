import pygame as pg
import Globals as g
import Menu as m
import Functions as f
import Game
from time import sleep
from csv import reader, writer
from ast import literal_eval

########################################
#              Culminating             #
#             Nathan Menezes           #
#                ICS3U0                #
#    A fireboy/watergirl style game    #
#   where you progress through levels  #
#     by moving/jumping to the goal    #
########################################

# **Cry** my coordinates are (y,x) not (x, y)
f.clear()
g.users = list(reader(open('Database.csv') , delimiter=",")) #Saves csv file to list

user_found = False
pg.init()
g.set_vars()

#Check for user
while not user_found:
  username = input("Please enter your username: ")
  if username.replace(' ', '') == '': continue;
  for user in g.users: #Pure match
    if username.lower() == user[0].lower():
      username = user[0] #Saves user data
      g.level = int(user[1])
      g.score = int(user[2])
      g.broken_total = int(user[3])
      g.colors = literal_eval(user[4])
      print(f"Welcome back {username}!")
      user_found = True;
      break;
  else:
    for user in g.users: #Partial match
      if username.lower() in user[0].lower():
        username = user[0] #Saves user data
        g.level = int(user[1])
        g.score = int(user[2])
        g.broken_total = int(user[3])
        g.colors = literal_eval(user[4])
        print(f"Welcome back {username}!")
        user_found = True;
        break;

    else: #Not found
      choice = input("Do you want to select this username?\n").lower()
      if 'yes' in choice or 'y' == choice:
        print("Creating new game")
        g.board.fill(g.colors["white"])
        m.prnt_to_scrn("Loading Instruction Screen", g.colors["red"], g.width/2-150, -g.height/2)
        pg.display.update()
        sleep(2) #Instructions
        print("\nPlease read the instructions on the pygame screen carefully. Remember to use both the terminal and the pygame window. Movements are by the arrow keys.\nIf it says 'press', you have to be in the pygame window. If it says 'enter' or 'type', that's the terminal.\n Please quit through the game to save your score. Remember to press 'H' for help, or 'Q' to quit. Thanks!")
        if m.help() == 0: quit()
        g.board.fill(g.colors["white"])
        pg.display.update()
        user_found = True;

#Game screens setup
pg.display.set_caption("Atari Fireboy")
print("\nGame starts in \033[s")
sleep(1)
print("\033[u3...")
sleep(1)
print("\033[u2...")
sleep(1)
print("\033[u1...")
sleep(1)
f.clear()
print("GO!")

#Game loop for 50 levels
while g.level <= 50:
  g.set_vars()
  m.draw_menu(True, True, True, True, True, True)
  Game.create_board()
  if Game.level() == 0: break;
else:
  print(f"\033[92mCONGRATULATIONS {username}! YOU BEAT THE GAME! HOPE TO SEE YOU AGAIN SOON!")

#Loops to find the user's info
for user in g.users:
  if user[0] == username:
    user[1:] = g.level, g.score, g.broken_total, g.colors #Saves updated info
    break;
else: #Creates a new user if not found
  g.users.append([username, g.level, g.score, g.broken_total, g.colors])

#Writes new info to file (database)
with open('Database.csv', 'w') as file_writer: #Opens a csv writer to update the info
  write = writer(file_writer)
  for user in g.users: #Saves data back to file row by row
    write.writerow(user)
  print(f"Bye! Thank you for playing {username}!") #Confirms it has been saved

g.board.fill(g.colors["white"])
font = pg.font.SysFont("comicsansms", 75)
g.board.blit(font.render("END", False, (0,0,0)), (g.width/2-25,g.height/2+50))
pg.display.update()