#Importing functions from other files
import Globals as v
import Objects as o
import ASCII as a
from Battle.Battle import battle
import Functions.systemFunctions as sf

#3rd Area Function
def jungle():
  enemy = sf.randObj(o.enemies, 2) #Randomly selects an enemy from the jungle enemy array
  area = sf.randObj(o.places, 2) #Randomly selects a jungle name from the jungle names array
  sf.print(f"Now entering {area}...") #Narratively sets the scene
  print(a.jungle) #ASCII tree art
  sf.print(f"You enter the far woods, on your quest to save the Tree of Life. Stumbling into the bush, you encounter a {enemy}.") #Encountering the jungle enemy narration
  battle(enemy) #Calls the battle function with the jungle enemy
  sf.print(f"{v.blue}After slaying the {enemy}{v.blue}, you come face to face with the guardian of the \"{area}\" {v.red}Emrakul, Voice of the Woods{v.blue}.") #Encountering the Jungle mini-boss narration
  battle("Voice of the Woods") #Calls the battle function with the Jungle mini-boss