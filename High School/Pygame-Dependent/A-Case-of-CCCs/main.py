#Will Le and Nathan Menezes 
#Make and let users choose between 3 CCC problems
#Sep 29th to Oct 1st 2021
# CCC J1: 2019 (Question 1), 2016 (Question 2), 2017 (Question 3)

#This is what's in the config folder
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/" #A hack i found online to fix the matplotlib directory error for game 3

from UniversalFuctions import acquireNum #Gets the functions from other files (readability)
from Question1 import Basketball
from Question2 import Tournaments
from Question3 import Quadrants
  
while(True): #Continues until user wishes to quit
  program = acquireNum("""\033[32mPlease select which CCC you want to try:\033[0m\n
\033[36mPress 1 for Basketball
Press 2 for Tournaments
Press 3 for Quadrants
Press 4 to Exit
\033[0m\n""", 1, 4)
  #Selects the corresponding program based on user selection
  if (program == 1): Basketball()
  elif (program == 2): Tournaments()
  elif (program == 3): Quadrants()
  elif (program == 4): #Exit option
    print("\033[35mThanks for playing! Goodbye.\033[0m")
    break