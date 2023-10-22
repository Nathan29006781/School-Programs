#Importing functions from other files
import Functions.systemFunctions as sf
import Globals as v
import Objects as o

#Setting up a battle, requires the name of the enemy
def battle(enemy):
  sf.cut()
  game = sf.randObj2(o.games) #Gets a random game to play
  game_name = (game.__name__).replace("_", " ").title() #Gets the name of the game from its function name
  sf.print(f"{v.blue}The {v.red}{enemy}{v.blue} challenges you to a game of {v.green}{game_name}")
  sf.print(v.violet + sf.randObj2(o.battleStart)) #Battle Call
  sf.cut()
  game(3, enemy) #Runs 3 rounds of the game and tells it the enemy's name