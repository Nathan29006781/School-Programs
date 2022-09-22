#Imports functions from other files
import Globals as v
import sys
from time import sleep
from os import system
from random import randint
import Functions.gameFunctions as gf

# Overloaded print for delayed writing
def print(text, delay_time=0.02): #0.02 is good
  for ch in text:      
    sys.stdout.write(ch)
    sys.stdout.flush()
    sleep(delay_time)
  sys.stdout.write("\n\n") 

#Delays for the times specified by user in the arg
def delay(time):
  sleep(time/1000)

#Clears the screen and prints health/items of the user
def clear():
  system('clear')
  gf.health()
  gf.items()

#Prompts the user to press Enter to continue, which also clears the screen
def cut():
  input(f"{v.reset}Press 'Enter' to continue{v.blue} ")
  clear()

#Removes the colour of an item when in format ({v.color}"text"{v.color}). It removes the first and last 5 chars from the text
def stripColor(text):
  return text[5:-5]

#Gives a random number from range specified in arguments
def rnd(low, high):
  return randint(low, high)

#Gets a random object from a 2D array and color formats
#User specifies a 2D array and index to get the subarray
def randObj(arr, index):
  subArr = arr[index]
  return f"{subArr[0]}{subArr[rnd(1, len(subArr)-1)]}{v.blue}"

#Simply gets a random object from the specified array with no color format
def randObj2(arr):
  return arr[rnd(0, len(arr)-1)]