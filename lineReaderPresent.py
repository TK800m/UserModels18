##printing lines

import pygame, sys, time, math, numpy

pygame.init()
width = 1200
height = 600
myfont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fastreading with Eyetracker")
bg = pygame.image.load('background2.png')
## initialize texts
texts = ["TEXTS/mary.txt", "TEXTS/test.txt", "TEXTS/T1.txt", "TEXTS/nassradin.txt", "TEXTS/T2.txt"]
data = open (texts[3], "r")
ntexts = len(texts)

##add questions for texts
FPS = 90
BLACK = 0,0,0
GREY = 128,128,128
clock = pygame.time.Clock()

def showWord(word, location):
    text = myfont.render(word,1,(0,0,0))
    textHeight =text.get_height()
    screen.blit(text,(location ,(height/2)-(textHeight/2)))

##array of all the words in the text works!!
Arr =[]
for lines in data:
	for words in lines.split():
		Arr.append(words)

##setting starting position works!!
objectTrackers = [0,1,2,3,4,5,6,7]
#objectDistance = [0,0,0,0,0,0,0]
objectTrackers = numpy.array(objectTrackers)
for i in range (0,len(objectTrackers)):
	if i == 0:
		objectTrackers[i] = 800
	else:
		getSize = myfont.size(Arr[i-1])
		objectTrackers[i] = objectTrackers[i-1]+ getSize[0] + 10
print(objectTrackers)

i = 0
count = 0
box_dir = -2
while True:
	clock.tick(FPS)

	for event in pygame.event.get():
	  if event.type == pygame.QUIT:
	    sys.exit()
	  if event.type == pygame.KEYDOWN:
	              if event.key == pygame.K_UP:
	              	box_dir -=1
	              if event.key == pygame.K_DOWN:
	              	box_dir +=1
	              	if box_dir >-2:
	              		box_dir = -1
	                  		
	              if event.key == pygame.K_SPACE:
	                  time.sleep(10)
	screen.blit(bg,(0,0))

	objectTrackers += box_dir
	#if objectTrackers[0] == width/2:
		#speech = gTTs(Arr[i],'en')
		#speech.say()

	if objectTrackers[0] <= 0:
		storage = abs(objectTrackers[0])
		for y in range (0,len(objectTrackers)):
			if y < len(objectTrackers)-1:
				objectTrackers[y] = objectTrackers[y+1]
			elif y == len(objectTrackers)-1:
				getSize = myfont.size(Arr[i+y])
				objectTrackers[y] = objectTrackers[y-1] + getSize[0] + storage +10
	#object tracker 1 becomes 0 etc. new entry in objectTrackers[5] is i+1
		i += 1

	for x in range(0,len(objectTrackers)):
		showWord(Arr[i+x], objectTrackers[x])
	pygame.display.update()
	pygame.display.flip()


