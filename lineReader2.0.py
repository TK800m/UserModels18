##printing lines

import pygame, sys, time, math, numpy

pygame.init()
width = 800
height = 600
myfont = pygame.font.Font(None, 90)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fastreading with Eyetracker")
## initialize texts
TXT1 = "C:/Users/Sjaak/ownCloud/Master HMC/2018-2019/User Models/mary.txt"
texts = [TXT1, "text2.txt", "text3.txt", "text4.txt"]
data = open (texts[0], "r")


print(data)
ntexts = len(texts)


##add questions for texts
FPS = 150
BLACK = 0,0,0
GREY = 128,128,128
clock = pygame.time.Clock()

def showWord(word, location):
    text = myfont.render(word,1,(0,0,0))
    screen.blit(text,(location ,height/2))
    pygame.display.update()

##array of all the words in the text works!!
Arr =[]
for lines in data:
	for words in lines.split():
		Arr.append(words)

##setting starting position works!!
objectTrackers = [0,1,2,3,4,5]
objectDistance = [0,0,0,0,0]
objectTrackers = numpy.array(objectTrackers)
for i in range (0,6):
	if i == 0:
		objectTrackers[i] = 800
	else:
		getSize = myfont.size(Arr[i-1])
		objectTrackers[i] = objectTrackers[i-1]+ getSize[0] + 10
print(objectTrackers)
objectDistance[4]=abs(objectTrackers[5]- objectTrackers[4])
objectDistance[3]=abs(objectTrackers[4]- objectTrackers[3])
objectDistance[2]=abs(objectTrackers[3]- objectTrackers[2])
objectDistance[1]=abs(objectTrackers[2]- objectTrackers[1])
objectDistance[0]=abs(objectTrackers[1]- objectTrackers[0])
print(objectDistance)

##

i = 0
count = 0
box_dir = -5
while True:
	clock.tick(FPS)
	#for x in range(0,5):
	#	xToGo[x] = myfont.size(Arr[i+x])
	#	if x == 0:
	#		objectTrackers[x] = objectTrackers[x]
	#	else:
	#		objectTrackers[x] = objectTrackers[x] + xToGo[x-1]
	
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
	screen.fill(GREY)
	 #box stuff

	objectTrackers += box_dir
	
	if objectTrackers[0] <= 0:
		storage = abs(objectTrackers[0])
		for y in range (0,6):
			if y < 5:
				objectTrackers[y] = objectTrackers[y+1]
			if y == 5:
				getSize = myfont.size(Arr[i+y-1])
				objectTrackers[y] = objectTrackers[y-1] + getSize[0] + storage +10
				#print(objectTrackers[y-1])
				#print(objectTrackers[y]
		objectDistance[4]=abs(objectTrackers[5]- objectTrackers[4])
		objectDistance[3]=abs(objectTrackers[4]- objectTrackers[3])
		objectDistance[2]=abs(objectTrackers[3]- objectTrackers[2])
		objectDistance[1]=abs(objectTrackers[2]- objectTrackers[1])
		objectDistance[0]=abs(objectTrackers[1]- objectTrackers[0])
		print(objectDistance)
			

	#object tracker 1 becomes 0 etc. new entry in objectTrackers[5] is i+1
		i += 1

	## check if xToGo is smaller than 800 - some margin
	#nextWord = (locX+xToGo+10)
	#if nextWord <= 800:
		##display another word and take care of the location
	#	showWord(Arr[i+1],locX2)
	for x in range(0,6):
		showWord(Arr[i+x], objectTrackers[x])
	pygame.display.flip()


