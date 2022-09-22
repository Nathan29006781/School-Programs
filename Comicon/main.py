#Nathan Menezes & Will Le
#October 17th 2021
#An interactive RPG that features minigames, armour, and health

#Must be viewed on a monitor. Bottom of screen may not be visible on laptop
#May need to press enter more times on some sections(mostly seen in blackjack as the CPU draws more cards)
#Music can only be turned off when you die

#Import functions and multi-use vars
import Functions.systemFunctions as sf
import Globals as v
import ASCII as a
import Objects as o

#Get minigames
from Areas.Intro import intro
from Areas.Desert import desert
from Areas.Waste import waste
from Areas.Jungle import jungle
from Areas.TreeOfLife import treeOfLife

#Opening Sequence
print(a.title)
print("By: Nathan Menezes and Will Le\n")
print("Press Ctrl+C to exit at any time")
print("See your status at the bottom-left\n")
name = input(f"{v.red}Name THY HERO(INE): {v.green}")
if name != "": v.name = name
v.name = v.green + v.name + v.blue
sf.print(f"{v.green}Thank you {v.name}. Now go save the World!")
sf.cut()

# #All area functions are called
intro()
desert()
waste()
jungle()
treeOfLife()

# #Ending Sequence
sf.clear()
sf.print(f"{v.green}GOODBYE {v.name}, my young mage! You were able to obtain {len(o.items)} armours and {v.health} health.\n You have rekindled the {v.yellow}Fading Light!\n")
print(a.win)
sf.delay(5000)
sf.clear()