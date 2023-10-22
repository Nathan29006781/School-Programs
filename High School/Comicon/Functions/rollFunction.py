#Import functions from other files
import Globals as v
import Objects as o
import ASCII as a
import Functions.gameFunctions as gf
import Functions.systemFunctions as sf

#Checks if item is in a given array
def roll(item, arr):
  for i in range (0, len(arr)): #Goes through all subcategories of the array
    if sf.stripColor(item) in arr[i]: return i #Found, returns strength of item
  return -1 #Not Found

#Function to determine if an armour is dropped and what rarity
def chance(enemy):
  armourRoll = sf.rnd(0, 10)
  if roll(enemy, o.enemies) != -1: #Weak Enemy
    if armourRoll < 8: armourStrength = 0 #0-7, no armour is dropped
    elif armourRoll < 10: armourStrength = 1 #8-9, decent armour is dropped
    else: armourStrength = 2 #9-10, cool armour is dropped
  else: #Strong enemy
    if armourRoll < 6: armourStrength = 0 #0-5, no armour is dropped
    elif armourRoll < 9: armourStrength = 1 #6-8, decent armour is dropped
    else: armourStrength = 2 #8-10 get cool WEAPON

  if armourStrength == 0: #Armor fail
    sf.print(f"{v.red}Sadly the {enemy} {v.red}did not drop anything useful.")
  else: #Obtained armour successfully
    armour = sf.randObj(o.armour, armourStrength) #Randomizes what armour is dropped and determines the armour strength
    sf.print(f"{v.green}The {enemy} {v.green}dropped something.") #Armour dropped narration
    sf.print(f"{v.green}You obtained {armour}")
    gf.items(armour) #Puts the obtained armour in the user's items
    if armourStrength == 1: print(a.shield) #Prints different ASCII art based on the strength of the armour
    elif armourStrength == 2: print(a.crown)
    