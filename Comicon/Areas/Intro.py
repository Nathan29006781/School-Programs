#Import functions from other files
import Globals as v
import Objects as o
import ASCII as a
import Functions.gameFunctions as gf
import Functions.systemFunctions as sf

#Introduction to the game/worldbuilding fuction
def intro():
  print(a.town) #ASCII town art
  sf.print(f"{v.blue}The {v.green}Tree of Life{v.blue} is dying, {v.name}, its power is waning and you must be the one to save it.") #Opening narration
  sf.print(f"{v.green}The Tree{v.blue} is the source of all our magical power, you mustn’t let the {v.red}HOOOOMANS{v.blue} murder it and take it for their own greed.") #Quest narration
  sf.print(f"Make haste young {v.name}, become the {v.violet}legend{v.blue} you were always destined to be.")
  sf.cut()
  armour = sf.randObj(o.armour, 0) #Randomly selects an armour from the starter armour array
  sf.print(f"You obtained '{armour}{v.green}'") #Prints what armour was selected
  gf.items(armour) #Addes this armour to the user's items
  print(a.hat) #ASCII art
  sf.print(f"{v.blue}Remember to keep an eye on your health. If it gets to {v.red}0 you will die. {v.blue}Fortunately, if you succesfully knock back or beat an enemy, you will {v.green}regain 10 health.")
  sf.print(f"{v.blue}Your armours will be able to protect you from receiving too much damage.\nHowever be wary of getting hurt, your armour will be lost if it used to shield you!")
  sf.cut()
  sf.print(f"There are 3 rarities of armour:\n{v.brown}Starter armour{v.blue} that reduces damage by {v.green}10{v.blue}, which you were most recently given.\n{v.beige}Regular armour{v.blue} that reduces damage by {v.green}20{v.blue}, and can be acquired from fighting enemies and bosses, and finally,\n{v.violet}Magical armour{v.blue} that reduces damage by {v.green}30{v.blue}, which can be obtained very rarely after battles.\nIf you have no armour however, you're going to take {v.red}35 damage{v.blue} each hit.")#Explains armour and how they work
  sf.cut(); #Prompts the user to enter the next scene