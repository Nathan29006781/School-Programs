#Importing functions and variables from other files
import pygame
import gameFunctions as gf
import Globals as g
import textFunctions as tf

def opening():
  tf.screenSetUp()
  #Prompts the user to presss Enter to start the game
  start = False
  while not start:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN: #Starts the program if the user inputs an answer
          start = True
        if event.key == pygame.K_i: #Invert text if "i" is pressed
          tf.eraseText("Inverted: " + gf.state(g.invert), (5, g.dis_height-80))
          g.invert = -g.invert #Toggles between 0 and 1
          tf.updateText("Inverted: " + gf.state(g.invert), (5, g.dis_height-80), g.green)

        if event.key == pygame.K_o: #Toggle obstacles if "o" is pressed
          tf.eraseText("Obstacles: " + gf.state(g.obstacle), (5, g.dis_height-60))
          g.obstacle = -g.obstacle #Toggles between 0 and 1
          tf.updateText("Obstacles: " + gf.state(g.obstacle), (5, g.dis_height-60), g.green)

        if event.key == pygame.K_a: #Change autopilot if "a" is pressed
          tf.eraseText("Auto: " + g.autos[g.auto].__name__.upper(), (5, g.dis_height-40))
          g.auto += 1
          g.auto %= 5 #rollover to start of array
          tf.updateText("Auto: " + g.autos[g.auto].__name__.upper(), (5, g.dis_height-40), g.green)

        if event.key == pygame.K_UP: #Increase speed when 'up' is pressed
          tf.eraseText("Speed: " + str(g.snake_speed), (g.dis_width - 85, g.dis_height - 100))
          if g.snake_speed != 30: g.snake_speed += 1
          tf.updateText("Speed: " + str(g.snake_speed), (g.dis_width - 85, g.dis_height - 100), g.green)
            
        if event.key == pygame.K_DOWN: #Increase speed when 'up' is pressed
          tf.eraseText("Speed: " + str(g.snake_speed), (g.dis_width - 85, g.dis_height - 100))
          if g.snake_speed != 1: g.snake_speed -= 1
          tf.updateText("Speed: " + str(g.snake_speed), (g.dis_width - 85, g.dis_height - 100), g.green)

        if event.key == pygame.K_RIGHT: #Increase size when 'up' is pressed
          tf.eraseText("Size: " + str(g.snake_block), (g.dis_width - 85, g.dis_height - 80))
          if g.snake_block != 30: g.snake_block += 1
          tf.updateText("Size: " + str(g.snake_block), (g.dis_width - 85, g.dis_height - 80), g.green)

        if event.key == pygame.K_LEFT: #Increase size when 'up' is pressed
          tf.eraseText("Size: " + str(g.snake_block), (g.dis_width - 85, g.dis_height - 80))
          if g.snake_block != 1: g.snake_block -= 1
          tf.updateText("Size: " + str(g.snake_block), (g.dis_width - 85, g.dis_height - 80), g.green)

def close(): #Function for game loss
  g.dis.fill(g.black)
  g.dis.blit(g.font1.render("You Lost! Press P to Play Again or Q to Quit", False, g.red), (g.dis_width / 2 -200, g.dis_height-250))
  gf.printScore()
  pygame.display.update()

  #If you pressed Q, quits the game, if you pressed P, plays the game again
  endSequence = True
  while endSequence:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          g.playing = False
          endSequence = False
        if event.key == pygame.K_p: 
          endSequence = False