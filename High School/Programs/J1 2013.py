#Nathan Menezes & Will Le
#Date: Sept 28, 2021
#Next in Line (CCC J1 2013)
#Purpose: To find the age of the oldest child given youngest and middle children's ages.
#Solve with data validation and prompts

from os import system #for clearing screen

#Function to acquire ages of the children
def acquireNum(msg, range_start, range_end):
  while True:
    try:
      val = float(input(msg)) #Tries to cast to float
      if val.is_integer(): val = int(val) #Tries to cast float to int
      else: raise ValueError #Raises error if float was not an integer 
      if val not in range(range_start, range_end+1): raise IndexError #Raises error if not in range
      system('clear') #Clears screen
      break #Exits loop
    except ValueError: #If input wasn't an integer, sends error message
      system('clear') #Clears screen
      print("\033[31mPlease Enter an Integer.\033[0m\n")
    except IndexError: #If input was an interger but not in range, states the acceptable range in an error message
      system('clear') #Clears screen
      print(f"\033[31mValue not in acceptable range. Must be between {range_start} and {range_end}. Try again\033[0m\n")
  return val

#Instructions for the Program
exit = 1 #Flag to loop program
while(exit == 1):
  print("Please enter the ages of the youngest and middle children when prompted.\nWe will give you the age of the oldest child.\n")

  #Input for youngest child's age (Y is the variable for the age of the youngest child)
  Y = acquireNum("\033[92mPlease enter the age of the youngest child: ", 0, 50)

  #Input for the middle child's age (M is the variable for the age of the middle child)
  M = acquireNum("\033[92mPlease enter the age of the middle child: ", Y, 50)

  #Calculates and prints the age of the oldest child based on the ages of the middle and youngest
  print(f"\033[92mThe age of the oldest child is: \033[0m{3*M-2*Y }")
  
  #Asks for input to exit or loop the program
  exit = acquireNum("\nPress 1 to run again\nPress 2 to end the program\n", 1, 2) #Flag to loop program is modified here

#Goodbye Message
print("\033[92mGoodbye!\n--------\033[0m")