#J1 2019
#To calculate the winning basketball team given their different methods of scoring

#Importing the universal functions present in the code
from UniversalFuctions import acquireNum
from UniversalFuctions import listReturn

#Beginning of Problem 1 (Basketball CCC)
def Basketball():
  #Welcome/Instructions
  print("""\033[31mWelcome to 'Winning Score'.\033[0m

\033[34mYou enter how many times each team scored successfully in these 3 ways:\033[0m
\033[35m3-point shots
2-point field goals
1-point free throws\033[34m

We will then calculate how many points each team scored and who won or if they tied.
  \033[0m\n""")
  
  raptors = [0] * 4 #Initialize 4 spaces because no value for 0 points
  warriors = [0] * 4

  for points in range(3, 0, -1): #Iterate through point vals 3, 2, and 1
    raptors[points] = acquireNum(f"Please enter the number of Raptor {points}-point shots: ", 0, 50)
  for points in range(3, 0, -1):
    warriors[points] = acquireNum(f"Please enter the number of Warrior {points}-point shots: ", 0, 50)

  #Calculates the total points of both teams
  raptorPoints = 3*raptors[3] + 2*raptors[2] + raptors[1]
  warriorPoints = 3*warriors[3] + 2*warriors[2] + warriors[1]

  print("\033[34mAnd the final score is:\n")
  #Displays who wins or if they tied
  if(warriorPoints > raptorPoints): 
    print(f"\033[92mWarriors win with {warriorPoints} points. ☜(⌒▽⌒)☞")
    print(f"\033[31mRaptors only managed to score {raptorPoints} points. ┏༼ ◉╭╮◉༽┓")
  elif(warriorPoints < raptorPoints): 
    print(f"\033[92mRaptors win with {raptorPoints} points. ☜(⌒▽⌒)☞")
    print(f"\033[31mWarriors only managed to score {warriorPoints} points. ┏༼ ◉╭╮◉༽┓")
  else: 
    print(f"Raptors and Warriors tie with {raptorPoints} points. t(-_-t)")
  
  #Returning to the list of options
  listReturn()
