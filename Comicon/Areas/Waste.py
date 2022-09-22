#Import functions from other files
import Globals as v
import Objects as o
import ASCII as a
from Battle.Battle import battle
import Functions.systemFunctions as sf

#Second area function
def waste():
  enemy = sf.randObj(o.enemies, 1) #Randomly selects an enemy from the waste enemies array
  sf.print(f"Now entering {sf.randObj(o.places, 1)}...") #Randomly selects an area name from the wastes area array and prints it
  print(a.waste) #ASCII moon art
  sf.print(f"{v.blue}Entering the wastes, a foul stench fills the air. Rising from the pits, {enemy} unseen by elven eyes blocks your path.") #Encounter with enemy narration
  battle(enemy) #Calls the battle function
  sf.print(f"{v.blue}Cleansing the waste of {enemy}, you proceed further into the heart of the wastes, on your journey to the Tree of Life.") #Progressing the story narration
  sf.print(f"Blocking your path is {v.red}Ulamog, Scourge of the Purity{v.blue}. You must purge the tyrant to continue on your fateful journey.") #Encounter with mini-boss narration
  battle("Scourge of Purity") #Calles battle function