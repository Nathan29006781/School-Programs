#Imports functions from other files
import Functions.gameFunctions as gf
import Functions.systemFunctions as sf
import Globals as v
import ASCII as a

def rock_paper_scissors(rounds, enemy):
  #Array for the different options
  rps = ["Rock", "Paper", "Scissors"]

  sf.print(f"{v.underline}Rock, Paper, Scissors!{v.reset}{v.blue}\nChoose a hand!\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\nDo your best to come on top!")
  sf.cut()
  for i in range(rounds): #Determines what round it is and prints it
    print(f"Rock Paper Scissors - Round {i+1}\n")
    sf.print(f"{v.green}Choose a hand {v.name}:")
    for j in range (0,3):
      print(f"\b'{j+1}' for {rps[j]}")
    #Acquires the player's choice between the 3 options
    plChoice = gf.acquireNum("", 1, 3)-1

    sf.clear()
    for j in range (0,3):
      sf.print(f"\033[92m{rps[j]}...")
    cpuChoice = sf.rnd(0,2) #Randomizes what the CPU chooses
    sf.print(f"{v.red}{enemy}: {v.blue}{rps[cpuChoice]}\n{v.name}: {rps[plChoice]}") #Prints the choices of the user and the CPU
    if plChoice == 0: print(a.rock)
    elif plChoice == 1: print(a.paper)
    else: print(a.scissors)
    gf.score((cpuChoice-plChoice)%3, enemy) #Determines who won the round
    sf.cut()