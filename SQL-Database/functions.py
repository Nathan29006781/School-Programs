#Imports stuff from other files as well as the system command
from os import system
import Globals as g

def clear(): #Clears the screen
  system('clear')

#Takes in a string and checks if it is pure text. Returns as bool
def containsOnlyText(string):
  return not any(char.isdigit() for char in str(string)) #Checks if any digits in the string

def acquireNum(msg, blank, range_start="", range_end=""):
  while True: #Loops until acquired info
    val = input(f"{g.green}{msg}{g.reset}")
    try:
      if val == "": #If the user doesn't input any value
        if blank:
          clear()
          return val
        else: raise ValueError

      val = float(val) #Tries to cast to float
      if val.is_integer(): val = int(val) #Tries to cast float to int
      else: raise ValueError #Raises error if float was not an integer

      if range_start != "" and range_end != "" and val not in range(range_start, range_end+1): raise IndexError #Raises error if not in range
      
      clear()
      break #Exits loop
    except ValueError: #If input wasn't an integer, sends error message
      clear()
      print(f"{g.red}Please Enter an Integer: {g.blue}")
    except IndexError: #If input was an integer but not in range, states the acceptable range in an error message
      clear()
      print(f"{g.red}Value not in acceptable range. Must be between {range_start} and {range_end}. Try again: {g.blue}")
  return val

def acquirePureText(msg): #Acquiring pure text from the input
  while True:
    text = input(f"{g.green}{msg}{g.reset}") #Prompts user for text
    clear()
    if containsOnlyText(text): return text
    print(f"{g.red}Please Enter Text: {g.blue}") #Error if it was an integer

def acquireAlphaText(msg, str_format): #Acquiring alphanumeric text from the input
  while True:
    text = input(f"{g.green}{msg}{g.reset}").replace(" ", "") #Prompts user for text
    clear()

    if str_format == "0": return text #This format means anything is acceptable
    if len(text) == len(str_format): #Makes sure it's the right length
      for text_chr, format_chr in zip(text, str_format): #Loops through the text and format strings by character
        if format_chr == "A" or format_chr == "1": #If supposed to be str or int
          if containsOnlyText(text_chr) != containsOnlyText(format_chr): #Checks if they are not the same format
            print(f"{g.red}Please follow the format '{str_format}': {g.blue}")
            break
      else: return text #Else from the for loop. Will only run if the loop didn't break
    else:print(f"{g.red}Please Enter Text {len(str_format)} long: {g.blue}") #Error if it was not the right length

#Takes in a title message, a list of prompts, and a list of functions to run based on the selcted prompt
def listRun(prompt, prompts, functions):
  prompts.append("Go Back") #Adds one more prompt for going back to previous menu
  functions.append(lambda: {}) #Does nothing for the go back option, handled within this function rather than externally
  length = len(prompts) #How many prompts
  while True: #Continues until user wishes to quit
    print(f"{g.green}{prompt}{g.beige}") #Prints the title
    result = "" #String to store the entire message of prompts, so it can be reprinted multiple times
    for i in range(length): result = "\n".join([result, f"Press {i+1} to {prompts[i]}"]) #Saves prompts

    choice = acquireNum(f"{g.beige}{result}\n", False, 1, length) - 1 #Asks user for a choice
    functions[choice]() #Runs the corresponding function
    if choice == length-1: break #If last option is picked, exit loop

def back(): #Enter to continue option
  input(f"{g.green}Press 'Enter' to continue{g.reset} ")
  clear()
  
def listReturn(prompt, prompts): #Prints a list of options such as multiple students with the same name. Returns the selected choice by index
  length = len(prompts)
  print(f"{g.green}{prompt}{g.beige}")
  result = ""
  for i in range(length): result = "\n".join([result, f"Press {i+1} to {prompts[i]}"]) #Prints the list of options with a number for each
  
  choice = acquireNum(f"{g.beige}{result}\n", False, 1, length) - 1
  return choice