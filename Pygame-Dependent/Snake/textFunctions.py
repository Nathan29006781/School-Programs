#Import functions and variables from other files
import pygame
import Globals as g
import gameFunctions as gf

def eraseText(msg, coord): #Function to clear the text on screen (by changing the text to the black colour of the background)
  text = g.font1.render(msg, False, g.black)
  g.dis.blit(text, coord)

def updateText(msg, coord, color):
  text = g.font1.render(msg, False, color) #Code for displaying Inverted: False or Inverted: True
  g.dis.blit(text, coord)
  pygame.display.update()

def screenSetUp():
  #Loads up the title image
  bx = g.dis_width
  by = g.dis_height
  #Getting values to resize the image
  title = pygame.image.load('title.png')
  ix,iy = title.get_size()
  scale_factor = bx/ix
  sy = scale_factor * iy
  if sy > by:
    scale_factor = by/iy
    sx = scale_factor * ix
    sy = by
  else:
    sx = bx
  sx = int(sx)
  sy = int(sy)
  #Resizing the image and moving it
  title = pygame.transform.smoothscale(title, (sx,sy))
  title_rect = title.get_rect()
  title_rect = title_rect.move((sx*800, sy*600))
  g.dis.blit(title, title_rect)

  #Displaying customizable options
  invert_text = g.font1.render("Inverted: " + gf.state(g.invert), False, g.green)
  obstacle_text = g.font1.render("Obstacles: " + gf.state(g.obstacle), False, g.green)
  auto_text = g.font1.render("Auto: " + g.autos[g.auto].__name__.upper(), False, g.green)
  speed_text = g.font1.render("Speed: " + str(g.snake_speed), False, g.green)
  size_text = g.font1.render("Size: " + str(g.snake_block), False, g.green)
  #Printing customizable options
  g.dis.blit(title, (0,70))
  g.dis.blit(g.font1.render("Press 'Enter' to Start", False, g.red), (g.dis_width / 2 -100, g.dis_height-50))
  g.dis.blit(g.font1.render("Press 'I' to Invert Controls", False, g.green), (5,5))
  g.dis.blit(g.font1.render("Press 'O' to Toggle Obstacles", False, g.green), (5,25))
  g.dis.blit(g.font1.render("Press 'A' to Select Autopilot", False, g.green), (5,45))
  g.dis.blit(g.font1.render("Use 'up' and 'down' to change Speed", False, g.green), (g.dis_width - 310, 5))
  g.dis.blit(g.font1.render("Use 'left' and 'right' to change Size", False, g.green), (g.dis_width - 310, 25))
  g.dis.blit(invert_text, (5, g.dis_height-80))
  g.dis.blit(obstacle_text, (5, g.dis_height-60))
  g.dis.blit(auto_text, (5, g.dis_height-40))
  g.dis.blit(speed_text, (g.dis_width - 85, g.dis_height - 100))
  g.dis.blit(size_text, (g.dis_width - 85, g.dis_height - 80))
  #Updating the display
  pygame.display.update()