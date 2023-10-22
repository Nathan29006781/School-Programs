#Ways to acquire data and also universal functions used in the code

#Imported things to set up cool code
from os import system

def acquireNum(msg, range_start, range_end):
  while True:
    try:
      val = float(input("\033[92m" + msg + "\033[0m")) #Tries to cast to float
      if val.is_integer(): val = int(val) #Tries to cast float to int
      else: raise ValueError #Raises error if float was not an integer 
      if val not in range(range_start, range_end+1): raise IndexError #Raises error if not in range
      system('clear') #Clears screen
      break #Exits loop
    except ValueError: #If input wasn't an interger, sends error message
      system('clear') #Clears screen
      print("\033[31mPlease Enter an Integer.\033[0m\n")
    except IndexError: #If input was an integer but not in range, states the acceptable range in an error message
      system('clear') #Clears screen
      print(f"\033[31mValue not in acceptable range. Must be between {range_start} and {range_end}. Try again\033[0m\n")
  return val

#Return to List Fuction
def listReturn():
  print()
  input("\033[34mPress Enter to return to the list.\033[0m")
  system('clear')