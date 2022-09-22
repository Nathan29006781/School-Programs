#Importing functions from other files
import Functions.gameFunctions as gf
import Functions.systemFunctions as sf
import Globals as v
import Objects as o

#Dictionary to convert cards to point values
values = {'K':10, 'Q':10, 'J':10, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'A':1}

#Game vars
#playable, choice, score
player = [1, 0, 0]
cpu = [1, 0, 0]
end = False

def printCard(char):
  if char != "10":
    print(f"""
 ------- 
|{char}      |
|       |
|       |
|       |
|      {char}|
 ------- 
{v.reset}""")

  else:
    print(f"""
 ------- 
|10     |
|       |
|       |
|       |
|     10|
 ------- 
{v.reset}""")

def deal(user): #Gives a random card to a user
  card = sf.randObj2(o.cards[0]) #Gets a random card
  if user == player: #Shows the player their card
    sf.print(f"\n{v.white}{card} of {sf.randObj2(o.cards[1])}")
    printCard(card)
  return values[card] #Sends the point value back

def turn(user):
  if user[0] == 0: return #If not in game (standing)
  elif user[1] == 1: #Hit
    user[2] += deal(user) #Gets another card
    if user[2] >= 21: #Excedeed 21 points
      global end
      end = True 
  elif user[1] == 2: #Stand
    user[0] = 0

def blackjack(rounds, enemy):
  print(f"{v.underline}Blackjack{v.reset}{v.blue}\nTry to get as close to 21 points without going over! 'Hit' will add a card and 'Stand' will stop you from getting any more.\n") #Description
  sf.cut()
  for i in range(rounds): #Plays set amount of rounds
    global player, cpu, end #Resets game vars
    player = [1, 0, 0]
    cpu = [1,0,0]
    end = False

    while not end:
      sf.clear()
      sf.print(f"{v.green}Blackjack - Round {i+1}\n")
      #Prints scores
      sf.print(f"\n{v.red}{enemy}: ?\n{v.green}{v.name}: {player[2]}")

      #Prompts user with 
      if player[0]: player[1] = gf.acquireNum("Press 1 to Hit\nPress 2 to Stand\n", 1, 2)

      if cpu[0]: #If CPU is still playing
        if cpu[2] < 16: cpu[1] = 1 #Hits if less than 16 points
        else: cpu[1] = 2 #Stands otherwise

      #Each player takes turns
      turn(player)
      turn(cpu)
      if player[0]==0 and cpu[0]==0: break
      sf.cut()

    #Prints scores
    sf.clear()
    sf.print(f"\n{v.red}{enemy}: {cpu[2]}\n{v.green}{v.name}: {player[2]}")

    #Evaluates game result
    result = player[2]-cpu[2] #Player's point lead
    if result == 0: gf.score(0, enemy) #Draw
    elif player[2]>21 and cpu[2]>21: gf.score(0, enemy) #Draw
    elif player[2]>21: gf.score(1,enemy) #Loss
    elif cpu[2]>21: gf.score(2,enemy) #Win
    elif result<0: gf.score(1,enemy) #Loss
    elif result>0: gf.score(2,enemy) #Draw
    sf.cut()