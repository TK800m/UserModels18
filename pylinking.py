
# asking questions about the texts

import pygame, sys, time, math, numpy
import pygaze

pygame.init()
width = 1200
height = 600
BLACK = 0,0,0
GREY = 100,100,100
WHITE = (255,255,255)
question_font = pygame.font.Font(None, 50)
info_font = pygame.font.Font(None, 20)
answer_font = pygame.font.Font(None, 30)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Questions for reading with Eyetracker")
bg = pygame.image.load('background.png')
FPS = 100
BLACK = 0,0,0
GREY = 100,100,100
WHITE = (255,255,255)
clock = pygame.time.Clock()

info = 'press the number corresponding to the correct answer..'
question = ['Why was Nasreddin on the roof of his house?']
options = ['1: He was looking at the view.','2: He was waiting for the old man.','3: He was fixing the roof.','4: He was cleaning the gutters']
buttW = 600;
buttH = 80;

class Button:
	def __init__(self, locationX, locationY, buttW, buttH):
		self.locationX = locationX
		self.locationY = locationY
		self.buttW = buttW
		self.buttH = buttH

class Answer:
	def __init__(self, locationX, locationY,answer):
		self.locationX = locationX
		self.locationY = locationY
		self.answer = answer

B1 = Button((width/2)-(buttW/2),200,buttW,buttH)
B2 = Button(B1.locationX,B1.locationY+buttH+10,buttW,buttH)
B3 = Button(B1.locationX,B2.locationY+buttH+10,buttW,buttH)
B4 = Button(B1.locationX,B3.locationY+buttH+10,buttW,buttH)

A1 = Answer((width/2),B1.locationY+10,options[0])
A2 = Answer((width/2),B2.locationY+10,options[1])
A3 = Answer((width/2),B3.locationY+10,options[2])
A4 = Answer((width/2),B4.locationY+10,options[3]) 


def showWordQ(word,font, locationX, locationY):
    text = font.render(word,1,(0,0,0))
    size = font.size(word)
    textHeight =text.get_height()
    screen.blit(text,(locationX-(size[0]/2),locationY+(textHeight/2)))

currentText = 1



while True:
	clock.tick(FPS)
	screen.fill(GREY)
##questions and info	
	showWordQ(info,info_font,width/2,20)
	showWordQ(question[0], question_font, width/2, 80)


##show Answers in rectangles
	pygame.draw.rect(screen, WHITE,(B1.locationX,B1.locationY,B1.buttW,B1.buttH));
	showWordQ(A1.answer,answer_font, A1.locationX, A1.locationY)

	pygame.draw.rect(screen, WHITE,(B2.locationX,B2.locationY,B2.buttW,B2.buttH));
	showWordQ(A2.answer,answer_font, A2.locationX, A2.locationY)

	pygame.draw.rect(screen, WHITE,(B3.locationX,B3.locationY,B3.buttW,B3.buttH));
	showWordQ(A3.answer,answer_font, A3.locationX, A3.locationY)

	pygame.draw.rect(screen, WHITE,(B4.locationX,B4.locationY,B4.buttW,B4.buttH));
	showWordQ(A4.answer,answer_font, A4.locationX, A4.locationY)

	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_1 or event.key==pygame.K_KP1:
				print(options[0])
			if event.key==pygame.K_2 or event.key==pygame.K_KP2:
				print(options[1])
			if event.key==pygame.K_3 or event.key==pygame.K_KP3:
				print(options[2])
			if event.key==pygame.K_4 or event.key==pygame.K_KP4:
				print(options[3])



	pygame.display.update()
	pygame.display.flip()

