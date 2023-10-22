#Import functions from other files
import Globals as v
import Objects as o
import ASCII as a
import Functions.systemFunctions as sf

#Final area function
def treeOfLife():
  enemy = f"{v.red}Lady of Death{v.blue}"
  sf.print(f"Now approaching {v.violet}The Tree of Life...") #Narratively setting the scene
  sf.print(f"{v.blue}After a long and arduous journey, you’ve arrived at the site of the {v.green}Tree of Life{v.blue}. It’s light is fading however, and fast. Rushing forward, you encounter your final obstacle…") #Story narration
  sf.print(f"Arising from the roots of the once majestic tree, {v.red}Nelaser, the {enemy} confronts your advance.") #Final boss narration
  sf.print(f"{v.red}The final confrontation is imminent!")
  sf.cut()
  sf.print(f"{v.red}OH NO! In a showcase of her strength, the '{enemy}{v.red}' has challenged you to a round of all 3 games...")
  sf.cut()

  #Special Case of the battle function
  for i in range (0,3):
    game = o.games[i]
    game_name = (game.__name__).replace("_", " ").title() #Gets the name of the game from its function name
    sf.print(f"{v.blue}For Round {i+1}, the {v.red}{enemy}{v.blue} challenges you to a game of {v.green}{game_name}")
    sf.print(v.violet + sf.randObj2(o.battleStart)) #Battle Call
    sf.cut()
    game(1, enemy)