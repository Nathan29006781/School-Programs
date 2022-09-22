#Imports functions from other files
import Globals as v
from Games.RockPaperScissors import rock_paper_scissors
from Games.TicTacToe import tic_tac_toe
from Games.Blackjack import blackjack

places = [ #Array of places that can be randomly selected
  [v.violet, "Golden Desert", "Riven Sands", "Iron Dunes"], #Deserts
  [v.violet, "Desolation of Acezzer", "Wailing Mire", "Witchlight Moor"], #Wastes
  [v.violet, "Eldritch Jungle", "Jungle of Dreaming Stones", "Fen of Lost Temples"] #Jungles
  ]

armour = [ #Array of armour that can be randomly called
  [v.brown, "Father's Robes", "Fool's Jester Hat", "Heirloom Chainmail"], #Starters
  [v.beige, "Enchanted Chestplate", "Festering Shield", "Ferrous Shadow", "Warped Protector", "Isolated Helm"], #Slightly Better
  [v.violet, "Profane Victory", "Celestial Protection", "Silent Sheath"] #Good
  ]

enemies = [ #Array of enemies that will randomly be called
  [v.yellow, "Dunecrawler", "Corrupted Genie", "Pharaoh's Old Guard"], #Desert
  [v.yellow, "Wailing Ghoul", "Those Who Lurk Below", "Phantom Dragon"], #Wastes
  [v.yellow, "GIANT ENEMY SPIDER", "Priest of the Dark Sun", "Polluted Shaman"], #Jungles
  ]

#Array of battle calls before a game
battleStart = ["Don your armour!","Prepare to fight!","En garde!", "Slay the Beast!", "Victory awaits!", "Vanquish thy foe!"]

#Cards for blackjack
cards = [
  ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A'],
  [f'{v.black}Spades', f'{v.red}Hearts', f'{v.red}Diamonds', f'{v.black}Clubs']
]

#Array that will store collected items
items = []

#Array of games to be randomly selected from
games = [rock_paper_scissors, tic_tac_toe, blackjack]