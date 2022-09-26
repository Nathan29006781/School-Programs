#Snake Game but Improved
#Nathan Menezes and Will Le
#October 29th 2021
#Original code from: https://www.edureka.co/blog/snake-game-with-pygame/
#Functions in camelCase, Variables in under_score

#If on smart autopilot, if the program tries to look at a side of the screen, it will crash as it can't look beyond the screen boundaries

#Imports functions and variables from other files
import pygame
import gameFunctions as gf
import Globals as g
import obstacles as o
import creation as c

# You may use an autpilot, however they are not guaranteed wins, just aids

g.playing = True

while g.playing:
  #Resets game settings, not customization
  c.opening()
  g.resetVars()

  #Loops to check if you have lost the game
  while not g.game_over:

    #Makes a turn (auto or human)
    g.autos[g.auto]()
    
    #Draws screen
    g.dis.fill(g.blue)
    pygame.draw.rect(g.dis, gf.col(g.green), [g.foodx, g.foody, g.snake_block, g.snake_block])
    o.drawObstacle()
    #Creates new snake head
    snake_Head = []
    snake_Head.append(g.x1)
    snake_Head.append(g.y1)
    g.snake_list.append(snake_Head)
    
    gf.drawSnake()  
    
    #Increases the size of the snake by 1 for each food eaten
    if g.x1 == g.foodx and g.y1 == g.foody:
      #Creates new food and obstacle
      g.foodx = gf.rand('x')
      g.foody = gf.rand('y')
      o.createObstacle()

      #Gives the snake an extra head if it got food
      g.x1 += g.x_change
      g.y1 += g.y_change
      snake_Head = []
      snake_Head.append(g.x1)
      snake_Head.append(g.y1)
      g.snake_list.append(snake_Head)

    #Determines if you've lost by hitting the sides
    if g.x1 >= g.dis_width or g.x1 < 0 or g.y1 >= g.dis_height or g.y1 < 0: g.game_over = True
    #Checks if collided with self
    for x in g.snake_list[:-1]:
      if x == snake_Head:
        print("HIT MYSELF")
        g.game_over = True
    o.checkObstacle()

    #Deletes the snake's butt
    del g.snake_list[0]
    gf.printScore()
    print(g.x_change, "     ", g.y_change)

    #Updates the screen
    pygame.display.update()
    gf.clock.tick(g.snake_speed)
  c.close()

#Quiting the game
pygame.quit()
quit() 