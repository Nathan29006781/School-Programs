#Copied from https://replit.com/@prithul0218/Tic-Tac-Toe
#May have some weird errors in edge cases due to recursion (We did not choose to write it that way)

#Imports functions from other files
import Functions.gameFunctions as gf
import Functions.systemFunctions as sf
import Globals as v

# Player 1 = X
# Player 2 = O

#Array for board squares
board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #game board
MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6] #sequence for checking (created by original author, don't really get it)
opponent = "" #global var so functions know the enemy's name

#Function for displaying the Tic Tac Toe board
def printBoard():
  print(v.blue)
  print('', board[0], "|", board[1], "|", board[2])
  print("---|---|---")
  print('', board[3], "|", board[4], "|", board[5])
  print("---|---|---")
  print('', board[6], "|", board[7], "|", board[8])
  print()

#Function for the user's turn
def Turn(player):
  validTurn = False
  while not validTurn: #Acquires a number input between 1 and 9
    placing_index = gf.acquireNum("", 1,9) if player == "X" else sf.rnd(1,9) #Ternary to either get player's choice or a random option for the computer
    placing_index -= 1 #Offsets because array is from 0-8 not 1-9
    if board[placing_index] == "X" or board[placing_index] == "O": #If spot is taken
      if (player == "X"): sf.print("Box already occupied. Try another one") #Displays if a box has already been chosen
    else: break

  board[placing_index] = player #Makes the move

#Checks if the user won
def CheckWin(player):
  count = 0 #This compares against the MagicSquare to determine wins
  for x in range(9):
    for y in range(9):
      for z in range(9):
        if x != y and y != z and z != x:
          if board[x] == player and board[y] == player and board[z] == player:
            if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15: #Someone won
              if player == "X": gf.score(2, opponent) #Player Won
              else: gf.score(1, opponent) #Player Lost to computer
              return True

  for j in range(9):
    if board[j] == "X" or board[j] == "O":
      count += 1
    if count == 9:
      gf.score(0, opponent) #Tie
      print()
      return True

#Game function, takes in enemy's name and the number of rounds to be played
def tic_tac_toe(rounds, enemy):
  global opponent, board #so they can be reset
  opponent = enemy

  print(f"{v.underline}Tic Tac Toe{v.reset}{v.blue}\nChoose a square to mark as your own. Be the first to get 3 squares lined up vertically, horizontally or diagonally!")
  sf.cut()
  for i in range(rounds):
    sf.clear()
    end = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Resets board
    
    while not end:
      sf.clear()
      print(f"Tic Tac Toe - Round {i+1}")
      printBoard()
      end = CheckWin("O") #Checks if computer won
      if end == True: break
      sf.print(f"{v.green}Choose a box {v.name}") #Prompts player to move
      Turn("X") #Player Turn
      sf.clear()
      print(f"Tic Tac Toe - Round {i+1}")
      printBoard()
      end = CheckWin("X") #Checks if computer won
      if end == True: break
      Turn("O") #Computer turn
    sf.cut()