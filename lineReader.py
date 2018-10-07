##printing lines

import pygame, sys, time, math

pygame.init()
width = 800
height = 600
myfont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fastreading with Eyetracker")
## initialize texts
texts = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"]
ntexts = len(texts)
##add questions for texts
FPS = 100
BLACK = 0,0,0
WHITE = 255,255,255
clock = pygame.time.Clock()

def showWord(word, locX):
    text = myfont.render(word,1,(0,0,0))
    screen.blit(text,(locX ,height/2))
    pygame.display.update()
    return locX


locX = 300
box_dir = 3
 
while 1:
  clock.tick(FPS)
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    FPS += 5
                if event.key == pygame.K_DOWN:
                    if FPS >= 10:
                    	FPS -= 5
                if event.key == pygame.K_SPACE:
                    time.sleep(10)
 
  screen.fill(WHITE)
 #box stuff

  locX += box_dir
  if locX >= 620:
    locX = 620
    box_dir = -3
  elif locX <= 0:
    locX = 0
    box_dir = 3

  showWord("Here is a very long text that is longer than a full screen so I will have to work out how this works with a text", locX)
  pygame.display.flip()


