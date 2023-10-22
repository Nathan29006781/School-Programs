#J1 2016
#To place a team in a group (Blue, Yellow, Red or Eliminated) based on their winnings

#Importing the universal functions present in the code
from os import system #to clear screen
from UniversalFuctions import listReturn

#Beginning of Problem 2 (Tournaments)
def Tournaments():
  #Welcome/Instructions
  print("""\033[31mWelcome to 'Tournament Selection'.\033[0m 

  \033[34mPlease input the amount of wins and loses below. 
  Indicate each win with a W and each lose with a L, include spaces between. 
  Please only input a maximum of 6 characters.\033[0m\n""")
  while True:
    wins = input("\033[92mPlease write a string of 'W' and 'L' that represents the games won and lost:\033[0m\n") #Input for storing the number of wins
    wins = wins.replace(" ", "") #Removes spaces
    system('clear') #Clears screen
    wCount = wins.count('W') + wins.count('w') #Counts wins and losses
    lCount = wins.count('L') + wins.count('l')

    if len(wins) > wCount + lCount: #If chars other than w and l
      print("\033[31mPlease only print 'W' and 'L'.\033[0m\n")
    elif len(wins) != 6: #If text is not 6 chars
      print("\033[31mPlease only print 6 characters.\033[0m\n")
    else:
      break

  #Printing results
  print(f"\033[0mThe player won {wCount} times and is placed in the \033[s")
#Conditions for each group and also elimination
  if 5<=wCount and wCount<=6: #Blue
    print ("\033[u\033[34mBlue Group.")
  elif 3<=wCount and wCount<=4: #Yellow
    print(f"\033[u\033[33mYellow Group.")
  elif 1<=wCount and wCount<=2: #Red
    print(f"\033[u\033[31mRed Group.")
  else: #Elimination
    print("\033[30m\033[47mThe player is Eliminated.\033[0m\n")
  
  #Returning to the list of options
  listReturn() 