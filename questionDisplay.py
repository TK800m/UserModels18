
# asking questions about the texts

import pygame, sys, time, math, numpy

pygame.init()
width = 800
height = 600
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
buttonW = 600;
buttonH = 80;
Button1 = [(width/2)-(buttonW/2),200]
Button2 = [(width/2)-(buttonW/2),Button1[1]+buttonH+10]
Button3 = [(width/2)-(buttonW/2),Button2[1]+buttonH+10]
Button4 = [(width/2)-(buttonW/2),Button3[1]+buttonH+10]
Answer1 = [(width/2),Button1[1]+10]
Answer2 = [(width/2),Button2[1]+10]
Answer3 = [(width/2),Button3[1]+10]
Answer4 = [(width/2),Button4[1]+10]


def showWord(word,font, locationX, locationY):
    text = font.render(word,1,(0,0,0))
    size = font.size(word)
    textHeight =text.get_height()
    screen.blit(text,(locationX-(size[0]/2),locationY+(textHeight/2)))

currentText = 1



while True:
	clock.tick(FPS)
	screen.fill(GREY)
##questions and info	
	showWord(info,info_font,width/2,20)
	showWord(question[0], question_font, width/2, 80)


##show Answers in rectangles
	pygame.draw.rect(screen, WHITE,(Button1[0],Button1[1],buttonW,buttonH));
	showWord(options[0],answer_font, Answer1[0], Answer1[1])

	pygame.draw.rect(screen, WHITE,(Button2[0],Button2[1],buttonW,buttonH));
	showWord(options[1],answer_font, Answer2[0], Answer2[1])

	pygame.draw.rect(screen, WHITE,(Button3[0],Button3[1],buttonW,buttonH));
	showWord(options[2],answer_font, Answer3[0], Answer3[1])

	pygame.draw.rect(screen, WHITE,(Button4[0],Button4[1],buttonW,buttonH));
	showWord(options[3],answer_font, Answer4[0], Answer4[1])

	
	
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
=======
# asking questions about the texts

import pygame, sys, time, math, numpy

pygame.init()
width = 800
height = 600
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
question = ['What is the answer to this question?']
options = ['1: Answer to QUESTION number one and it is long','2: 2 this is the anwer nubmer 2','3: 3 this is another answer three','4: This is number Four (4)']
buttonW = 600;
buttonH = 80;
Button1 = [(width/2)-(buttonW/2),200]
Button2 = [(width/2)-(buttonW/2),Button1[1]+buttonH+10]
Button3 = [(width/2)-(buttonW/2),Button2[1]+buttonH+10]
Button4 = [(width/2)-(buttonW/2),Button3[1]+buttonH+10]
Answer1 = [(width/2),Button1[1]+10]
Answer2 = [(width/2),Button2[1]+10]
Answer3 = [(width/2),Button3[1]+10]
Answer4 = [(width/2),Button4[1]+10]


def showWord(word,font, locationX, locationY):
    text = font.render(word,1,(0,0,0))
    size = font.size(word)
    textHeight =text.get_height()
    screen.blit(text,(locationX-(size[0]/2),locationY+(textHeight/2)))

currentText = 1



while True:
	clock.tick(FPS)
	screen.fill(GREY)
##questions and info	
	showWord(info,info_font,width/2,20)
	showWord(question[0], question_font, width/2, 80)


##Answers
	pygame.draw.rect(screen, WHITE,(Button1[0],Button1[1],buttonW,buttonH));
	showWord(options[0],answer_font, Answer1[0], Answer1[1])

	pygame.draw.rect(screen, WHITE,(Button2[0],Button2[1],buttonW,buttonH));
	showWord(options[1],answer_font, Answer2[0], Answer2[1])

	pygame.draw.rect(screen, WHITE,(Button3[0],Button3[1],buttonW,buttonH));
	showWord(options[2],answer_font, Answer3[0], Answer3[1])

	pygame.draw.rect(screen, WHITE,(Button4[0],Button4[1],buttonW,buttonH));
	showWord(options[3],answer_font, Answer4[0], Answer4[1])

	
	
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
