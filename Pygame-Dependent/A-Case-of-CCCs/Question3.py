#J1 2017
#To determine the co-ordinate of a point and which of the four quadrants it is in. Also displays the co-ordinate in a graph

#Importing the universal functions present in the code
from UniversalFuctions import acquireNum
from UniversalFuctions import listReturn

# Importing the required module for graphing
import matplotlib.pyplot as plt

# Beginning of Problem 3 (Quadrants)
def Quadrants():
  #Welcome/Instructions
  print("""\033[31mWelcome to 'Quadrant Selection'.\033[0m

\033[34mInput your x-value and y-value of your co-ordinate below. 
Please note that the minimum value is -50 and the maximum value is 50.\033[0m\n""")
  x = acquireNum("Please enter the x-value of the co-ordinate: ", -50, 50)
  y = acquireNum("Please enter the y-value of the co-ordinate: ", -50, 50)

  #Repeat Code hard to fix D:
  print(f"The co-ordinate ({x},{y}) is in \033[36mQuadrant\033[s")
  if x==0 and y==0: print("\033[us 1 & 2 & 3 & 4.\033[0m")
  elif x==0 and y>0: print("\033[us 1 & 2.\033[0m")
  elif x==0 and y<0: print("\033[us 3 & 4.\033[0m")
  elif x<0 and y==0: print("\033[us 2 & 3.\033[0m")
  elif x>0 and y==0: print("\033[us 1 & 4.\033[0m")
  elif x>0 and y>0: print("\033[u 1.\033[0m")
  elif x<0 and y>0: print("\033[u 2.\033[0m")
  elif x<0 and y<0: print("\033[u 3.\033[0m")
  elif x>0 and y<0: print("\033[u 4.\033[0m")
  
  #GRAPH:
  #Labels
  plt.figure("Quadrants - Game 3")
  plt.title('Where is my Co-ordinate?')
  print("\n\033[34mPress the X on the top right of the graph to close it and return to the list.\033[0m")
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.text(x+1, y+1, f"({x},{y})")

  #Setting up quadrant boundaries
  plt.plot([0,0], [-50,50], linewidth=1, color='black')
  plt.plot([-50,50], [0,0], linewidth=1, color='black')
  
  # plotting the points
  plt.scatter(x, y)
  plt.show()
  listReturn()