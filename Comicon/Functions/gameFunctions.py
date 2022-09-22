#Imports functions from other files
import Globals as v
import ASCII as a
import Objects as o
from os import system
import Functions.systemFunctions as sf
import Functions.rollFunction as rf

#Modifies the player's health given a 'modifier' value
def health(modifier=0):
  v.health += modifier
  if v.health >= 100: print(v.green) #Green for good health status
  elif v.health < 100 and 50 < v.health: print(v.yellow) #Yellow for moderate
  elif v.health <= 50 and 0 < v.health: print(v.red) #Red for low health
  else: #If dead (health<0)
    sf.delay(1000)
    system('clear')#Cannot use sf.clear() since that calls this function (infinite recursion)
    print(f"OH NO {v.name}! You let your health get to {v.red}0...{v.blue} You're dead now and the Light will keep Fading... {a.sad}\n")
    #Death Message
    print(a.death) #Prints tombstone
    sf.delay(3000) #Ends the game
    v.source.paused = True
    quit()
  print(f"\033[s\033[35;0fHealth: {v.health}     \033[u\033[2A") #Prints health at the bottom of the screen


#Takes in an item to add to the inventory
#If no item is added it will simply re-print
def items(item=""):
  if item != "": o.items.append(sf.stripColor(item)) #New items have the color format removed and then they are added to the items list
  print(f"\033[s\033[36;0f{v.green}Items: {o.items}     \033[u") #Prints the list at the bottom of the screen

#Gets the game result and correspondingly modifies the health
#Gets enemy's name for custom message
def score(val, enemy):
  if (val == 0): print(f"{v.yellow}You drawed with the {enemy}{v.yellow}!!") #Draw
  elif (val == 1): #Loss
    sf.print(f"{v.red}You Lost! The {enemy} {v.red}struck you! {a.sad}") #Hurt narration
    bestStrength = -1 #Loops to find the armour with the highest protection
    bestArmour = ""
    for armour in o.items:
      armour = f"{v.blue}{armour}{v.blue}" #Adds color format because roll will re-strip it
      armourStrength = rf.roll(armour, o.armour) #Gets armours strength
      if (armourStrength > bestStrength): #If this armour is better than the highest so far
        bestStrength = armourStrength #Saves this armour
        bestArmour = f"{o.armour[armourStrength][0]}{sf.stripColor(armour)}{v.blue}"
    lostHealth = bestStrength*10-25
    health(lostHealth) #Removes 25, 15, or 5 health based on best armour, 35 if no armour
    if bestArmour != "": 
      sf.print(f"{v.blue}Your {bestArmour} was able to protect you from grave harm, however you still lost {v.red}{-lostHealth} health{v.blue} and your {bestArmour}!")
      o.items.remove(sf.stripColor(bestArmour))
    #If they have armour it will be used to absorb damage
    else: sf.print(f"You lost {lostHealth} health!")
  elif (val == 2): #Win
    sf.print(f"{v.green}You Won! The {enemy} {v.green}has been knocked back!")
    health(10) #Gains 10 health
    print(a.winner)
    sf.cut()
    rf.chance(enemy) #Possibility of getting new armour

#Takes in a prompt and range.
#Runs until the user gives an integer in the range
#Returns the value
def acquireNum(msg, range_start, range_end):
  while True:
    try:
      val = float(input(f"{v.green}{msg}{v.reset}")) #Tries to cast to float
      if val.is_integer(): val = int(val) #Tries to cast float to int
      else: raise ValueError #Raises error if float was not an integer 
      if val not in range(range_start, range_end+1): raise IndexError #Raises error if not in range
      break #Exits loop
    except ValueError: #If input wasn't an integer, sends error message
      sf.print(f"{v.red}Please Enter an Integer: {v.blue}")
    except IndexError: #If input was an integer but not in range, states the acceptable range in an error message
      sf.print(f"{v.red}Value not in acceptable range. Must be between {range_start} and {range_end}. Try again: {v.blue}")
  return val