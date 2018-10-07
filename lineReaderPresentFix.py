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
FPS = 60
BLACK = 0,0,0
GREY = 128,128,128
clock = pygame.time.Clock()

word_speed = -2000 # pixels 
basis_frame_time = 1.0 / FPS


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
objectTrackers = [0,1]
objectTrackers = numpy.array(objectTrackers)
for i in range (0,len(objectTrackers)):
	if i == 0:
		objectTrackers[i] = 1200
	else:
		getSize = myfont.size(Arr[i-1])
		objectTrackers[i] = objectTrackers[i-1]+ getSize[0] + 10
print(objectTrackers)

i = 0
count = 0
countdown = 10
start_time = time.time()
while True:
	frame_duration = clock.tick(FPS)
	sinceFPS = clock.get_time()
	count += sinceFPS

	for event in pygame.event.get():
	  if event.type == pygame.QUIT:
	    sys.exit()
	  if event.type == pygame.KEYDOWN:
	      if event.key == pygame.K_UP:
	      	word_speed -=1
	      if event.key == pygame.K_DOWN:
	      	word_speed +=1
	      	if word_speed >-2:
	      		word_speed = -1
	      if event.key == pygame.K_SPACE:
	          time.sleep(10)
	      print("Current speed is: "+ str(word_speed))
	

	

	# want to move the word over 600 pixels in 1 sec: 
	# 600pix/sec and 60frame/sec ->
	if (count > 20):
		objectTrackers += word_speed
		count = 0

	if objectTrackers[0] <= 0:
		storage = abs(objectTrackers[0])
		objectTrackers[0] = objectTrackers[1]
		if i+1 < len(Arr):
			getSize = myfont.size(Arr[i+1])
			objectTrackers[1] = objectTrackers[0] + getSize[0] + storage
	#object tracker 1 becomes 0 etc. new entry in objectTrackers[5] is i+1
		i += 1

	
	sentence = ""
	if i+10 < len(Arr):
		for x in range(0,10):
			sentence += " "+ Arr[i+x] 
			
	elif countdown > 0:
		for z in range(0,countdown):
			sentence += " "+ Arr[i+z]
		countdown -=1
		print(sentence)
		if countdown == 0:		
			#At the end print out how many words read
			end = "words read = " + str(i+10)
			WL = len(end)
			getSize = myfont.size(end)
			end = myfont.render(end,1,(0,0,0))
			screen.blit(end, (width/2 -getSize[0]/2,100))

			#Calc the time it took to reed the words and print it
			totalTime = time.time()-start_time
			print("%.2f" %totalTime)
			timed = "this took " + str("%.2f" %totalTime)+ "sec"
			WL = len(timed)
			getSize = myfont.size(timed)
			timed = myfont.render(timed,1,(0,0,0))
			screen.blit(timed, (width/2 - getSize[0]/2,450))
			pygame.display.update()
			time.sleep(5)
			sys.exit()



	screen.blit(bg,(0,0))	
	showWord(sentence, objectTrackers[0])

	pygame.display.update()
	pygame.display.flip()


