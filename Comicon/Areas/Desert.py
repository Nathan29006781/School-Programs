#Importing fuctions from other files
import Globals as v
import Objects as o
import ASCII as a
from Battle.Battle import battle
import Functions.systemFunctions as sf

#Desert function
def desert():
  enemy = sf.randObj(o.enemies, 0) #Chooses random enemy from the desert enemy array
  sf.print(f"Now entering {sf.randObj(o.places, 0)}...") #Chooses random desert name from the desert name array
  print(a.desert) #ASCII desert art
  sf.print(f"{v.blue}The sizzling desert beside your hometown is your first major obstacle in your epic saga. The sun’s harsh rays burn your skin as you trudge through the shifting sands.") #Desert setting backstory
  sf.print(f"{enemy} emerges from the sands, scattering bloodied remains as it rises.") #Encountering desert enemy dialogue
  battle(enemy) #Start battle with desert enemy
  sf.print(f"{v.blue}The thumping of the {enemy}'s carcass stirs the land, prompting you to quickly traverse ahead.") #Story continuation
  sf.print(f"After miles of empty desert, you finally reach the edge, only to be stopped by {v.red}Kozilek, Horror of the Dunes{v.blue}.")#Encounter with desert mini-boss
  battle("Horror of the Dunes") #Battle with the desert mini-boss