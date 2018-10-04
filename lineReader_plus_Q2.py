##printing lines
#from pylink import *
import pygame, sys, time, math, numpy
from pylink import *

pygame.init()
width = 1200
height = 600
FPS = 60
clock = pygame.time.Clock()
BLACK = 0,0,0
GREY = 100,100,100
WHITE = (255,255,255)
myfont = pygame.font.Font(None, 90)
question_font = pygame.font.Font(None, 30)
answer_font = pygame.font.Font(None, 30)
info_font = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fastreading with Eyetracker")
bg = pygame.image.load('background2.png')
testbg = pygame.image.load('testBG.png')
##---------------------------------------------------------------------------------------------------------------------------------------------------------##
#Initialize the EyeLink system, and open a link connection to the EyeLink tracker.
#eyelinktracker = EyeLink()
#pylink.openGraphics()
# Check the display mode, create a full-screen window, and initialize the calibration system.

#· Send any configuration commands to the EyeLink tracker to prepare it for the experiment
#· Get an EDF file name, and open an EDF data file (stored on the eye tracker)
#· Record one or more blocks of trials. Each block typically begins with tracker setup (camera setup
#and calibration), and then several trials are run.
#· Close the EDF data file. If desired, copy it via the link to the local computer.
#· Close the window, and the link connection to the eye tracker.
##---------------------------------------------------------------------------------------------------------------------------------------------------------##





## initialize texts
class Texts:
	def __init__(self, text, question,options, answer):
		self.text = text
		self.question = question
		self.options = options
		self.answer = answer
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

T1 = Texts(1,2,3,4)
T1.text = "TEXTS/TEST1.txt"
T1.question = 'The claim that listening to Mozart makes you more intelligent led to... '
T1.options = ['1: conclusions that turned out to be scientifically invalid.','2: a new appreciation of the benefits of classical music.','3:  over-excited reactions among people concerned with children.',"4: I do not know"]
T1.answer = 3
print(T1.options[2])

T2 = Texts(1,2,3,4)
T2.text = "TEXTS/TEST2.txt"
T2.question = "In his research Dr Alfred Tomatis looked upon music as..."
T2.options = ["1: a means of diagnosing mental disorders.", "2: a non-verbal way of communication.", "3: a sequence of sounds affecting the brain","4: I do not know"]
T2.answer = 3

T3 = Texts(1,2,3,4)
T3.text = "TEXTS/TEST3.txt"
T3.question = "What is the idea behind filtering out sounds of a certain frequency from Mozart's music?"
T3.options = ["1: Some frequencies are more easily processed by the brain than others.", "2: Reducing the music's complexity makes it easier to appreciate.", "3:  Offering a limited sound spectrum makes it easier to concentrate.","4: I do not know"]
T3.answer = 3

T4 = Texts(1,2,3,4)
T4.text = "TEXTS/TEST4.txt"
T4.question = "The positive effect of Mozart's music on special needs children..."
T4.options = ["1: only became apparent after some time.", "2: was discovered quite accidentally.", "3: confirmed earlier research findings.","4: I do not know"]
T4.answer = 2

T5 = Texts(1,2,3,4)
T5.text = "TEXTS/TEST5.txt"
T5.question = "Research carried out by the University of Reading led to the conclusion that..."
T5.options = ["1: exposure to music causes significant physiological changes.", "2: appreciation of music is related to physiological characteristics.", "3: listening to music increases the capacity to absorb new information."]
T5.answer = 1

T6 = Texts(1,2,3,4)
T6.text = "TEXTS/TEST6.txt"
T6.question = "In Oliver Sack's experience music can help Parkinson patients to..."
T6.options = ["1:recover their ability to speak.", "2: overcome their difficulty in moving.", "3: restore their sense of balance."]
T6.answer = 2

T7 = Texts(1,2,3,4)
T7.text = "TEXTS/TEST7.txt"
T7.question = "What does Oliver Sacks say here about music?"
T7.options = ["1: It may stimulate the recovery from brain damage.", "2: It may provide a framework of time and space.", "3: It may support deficient parts of the brain."]
T7.answer = 3

T8 = Texts(1,2,3,4)
T8.text = "TEXTS/TEST8.txt"
T8.question = "What is said here about Mozart as a child?"
T8.options = ["1: His exceptional talents went hand in hand with a problematic childhood.", "2: He compensated for his physical weakness by developing his mind.", "3: He had to overcome serious problems before his talents were recognized."]
T8.answer = 1

#-----------------------------------------------------------------------------------#
txtObj = [T1, T2, T3, T4]
currText = txtObj[0]
#-----------------------------------------------------------------------------------#

buttW = 800;
buttH = 80;
B1 = Button((width/2)-(buttW/2),200,buttW,buttH)
B2 = Button(B1.locationX,B1.locationY+buttH+10,buttW,buttH)
B3 = Button(B1.locationX,B2.locationY+buttH+10,buttW,buttH)
B4 = Button(B1.locationX,B3.locationY+buttH+10,buttW,buttH)

A1 = Answer((width/2),B1.locationY+10,currText.options[0])
A2 = Answer((width/2),B2.locationY+10,currText.options[1])
A3 = Answer((width/2),B3.locationY+10,currText.options[2])
A4 = Answer((width/2),B4.locationY+10,currText.options[3])

info = 'press the number corresponding to the correct answer..'

data = open (T1.text, "r")
##add questions for texts

word_speed = -25 # pixels 
basis_frame_time = 1.0 / FPS

#showwords of linereader- and for questionscreen
def showWord(word, location):
    text = myfont.render(word,1,(0,0,0))
    textHeight =text.get_height()
    screen.blit(text,(location ,(height/2)-(textHeight/2)))
def showWordQ(word,font, locationX, locationY):
    text = font.render(word,1,(0,0,0))
    size = font.size(word)
    textHeight =text.get_height()
    screen.blit(text,(locationX-(size[0]/2),locationY+(textHeight/2)))
def makeTXTarray(Textfile):
	data = open(Textfile, "r")
	Arr =[]
	for lines in data:
		for words in lines.split():		
			Arr.append(words)

	for dot in range(0,10):
		Arr.append(".")
	return(Arr)
def calcObjectTracker(Arr):
	objectTrackers = [0,1]
	objectTrackers = numpy.array(objectTrackers)
	for i in range (0,len(objectTrackers)):
		if i == 0:
			objectTrackers[i] = 1200
		else:
			getSize = myfont.size(Arr[i-1])
			objectTrackers[i] = objectTrackers[i-1]+ getSize[0] + 10
	return(objectTrackers)

#calculate LiveAVG
def calcWIV(baseline, threshold):
	pupilsize  = getEventDataFlags(currentTime())
	pcps = (pupilsize-baseline)/baseline + 1000
	average = 0
	liveCount = 0

	while currentTime < 10000:
		average = average + pcps
		liveCount += 1

	LiveAVG= average/liveCount
	threshold = 0.997
	WIV = LiveAVG * threshold
	return(WIV)
##array of all the words in the text works!!


#-------------------------------------------------------------------------START-OF-GAMELOOP---------------------------------------------------------------------------------#
def setToStart(object):
	Arr = makeTXTarray(object.text)
	objectTrackers = calcObjectTracker(Arr)
	i = 0
	count = 0
	countdown = 10
	start_time = time.time()
	question_screen = False
	given_answer = 0
	return(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer)


(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
textCounter = 0
while True:
	#if this == startscreen:
	#
	## first show a start screen and calculate the baseline
	# baseline = getEventDataFlags(currentTime(1000))


	frame_duration = clock.tick(FPS)
	sinceFPS = clock.get_time()
	count += sinceFPS

	#if answer == incorrect:
	#because people were able to read, but just were wrong
	#	word_speed = 3
	#if answer == i dont know:
	#because people weren't able to read it is worse than being wrong
	#	wordspeed += 5
	#else:
	#	word_speed -= 1


	#calculate PCPS





	#calculate WIV

	### check WIV if it is too high decrease speed
	### if WIV is too low increas speed


	for event in pygame.event.get():
	  if event.type == pygame.QUIT:
	    sys.exit()
	  if event.type == pygame.KEYDOWN:
	  	
	      if event.key == pygame.K_UP:
	      	word_speed -=1
	      	print("Current speed is: "+ str(word_speed))
	      if event.key == pygame.K_DOWN:
	      	word_speed +=1
	      	print("Current speed is: "+ str(word_speed))
	      if word_speed >-2:
	      		word_speed = -1
	      
	      if event.key == pygame.K_SPACE:
	          time.sleep(10)
	      if event.key==pygame.K_q:
	      		sys.exit()
	      if question_screen ==True:
	      	if event.key==pygame.K_1 or event.key==pygame.K_KP1:
	      		given_answer = 1
	      		if given_answer == currText.answer:
	      			print("This is the correct answer: " + currText.options[0])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	      	if event.key==pygame.K_2 or event.key==pygame.K_KP2:
	      		given_answer = 2
	      		if given_answer == currText.answer:
	      			#---------------------------------------------------WORK IN PROGRESS--------------------------------------------------------------###
	      			print("This is the correct answer: " + currText.options[1])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	      			#---------------------------------------------------WORK IN PROGRESS--------------------------------------------------------------###
	      	if event.key==pygame.K_3 or event.key==pygame.K_KP3:
	      		given_answer = 3
	      		if given_answer == currText.answer:
	      			print("This is the correct answer: " + currText.options[2])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	      	if event.key==pygame.K_4 or event.key==pygame.K_KP4:
	      		given_answer = 4
	      		if given_answer == currText.answer:
	      			print("This is the correct answer: " + currText.options[3])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	if question_screen == False:
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
				objectTrackers[1] = objectTrackers[0] + getSize[0] + storage + 13
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
			screen.blit(bg,(0,0))
			showWord(sentence, objectTrackers[0])
			#print(sentence)
		if countdown == 0:		
			#At the end print out how many words read
			end = "words read = " + str(i)
			print(i)
			WL = len(end)
			getSize = myfont.size(end)
			end = myfont.render(end,1,(0,0,0))
			screen.blit(end, (width/2 -getSize[0]/2,100))

			#Calc the time it took to reed the words and print it
			totalTime = time.time()-start_time
			print("%.2f" %totalTime)
			print("WPM = "+ str((len(Arr)-10)/(totalTime/60)))
			timed = "this took " + str("%.2f" %totalTime)+ "sec"
			WL = len(timed)
			getSize = myfont.size(timed)
			timed = myfont.render(timed,1,(0,0,0))
			screen.blit(timed, (width/2 - getSize[0]/2,450))
			pygame.display.update()
			question_screen = True
			time.sleep(1)
		screen.blit(bg,(0,0))	
		showWord(sentence, objectTrackers[0])
	elif question_screen == True:
		screen.blit(testbg,(0,0))
				##questions and info	
		showWordQ(info,info_font,width/2,20)
		showWordQ(currText.question, question_font, width/2, 80)


		##show Answers in rectangles
		pygame.draw.rect(screen, WHITE,(B1.locationX,B1.locationY,B1.buttW,B1.buttH));
		showWordQ(A1.answer,answer_font, A1.locationX, A1.locationY)

		pygame.draw.rect(screen, WHITE,(B2.locationX,B2.locationY,B2.buttW,B2.buttH));
		showWordQ(A2.answer,answer_font, A2.locationX, A2.locationY)

		pygame.draw.rect(screen, WHITE,(B3.locationX,B3.locationY,B3.buttW,B3.buttH));
		showWordQ(A3.answer,answer_font, A3.locationX, A3.locationY)

		pygame.draw.rect(screen, WHITE,(B4.locationX,B4.locationY,B4.buttW,B4.buttH));
		showWordQ(A4.answer,answer_font, A4.locationX, A4.locationY)

		
	pygame.display.update()
	pygame.display.flip()
<<<<<<< HEAD
=======


=======
##printing lines

import pygame, sys, time, math, numpy

pygame.init()
width = 1200
height = 600
FPS = 60
clock = pygame.time.Clock()
BLACK = 0,0,0
GREY = 100,100,100
WHITE = (255,255,255)
myfont = pygame.font.Font(None, 90)
question_font = pygame.font.Font(None, 50)
answer_font = pygame.font.Font(None, 30)
info_font = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fastreading with Eyetracker")
bg = pygame.image.load('background2.png')
testbg = pygame.image.load('testBG.png')
## initialize texts
class Texts:
	def __init__(self, text, question,options, answer):
		self.text = text
		self.question = question
		self.options = options
		self.answer = answer
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

T1 = Texts(1,2,3,4)
T1.text = "TEXTS/TEST1.txt"
T1.question = 'The claim that listening to Mozart makes you more intelligent led to... '
T1.options = ['1: conclusions that turned out to be scientifically invalid.','2: a new appreciation of the benefits of classical music.','3:  over-excited reactions among people concerned with children.']
T1.answer = 3
print(T1.options[2])

T2 = Texts(1,2,3,4)
T2.text = "TEXTS/TEST2.txt"
T2.question = "In his research Dr Alfred Tomatis looked upon music as..."
T2.options = ["1: a means of diagnosing mental disorders.", "2: a non-verbal way of communication.", "3: a sequence of sounds affecting the brain"]
T2.answer = 3

T3 = Texts(1,2,3,4)
T3.text = "TEXTS/TEST3.txt"
T3.question = "What is the idea behind filtering out sounds of a certain frequency from Mozart's music?"
T3.options = ["1: Some frequencies are more easily processed by the brain than others.", "2: Reducing the music's complexity makes it easier to appreciate.", "3:  Offering a limited sound spectrum makes it easier to concentrate."]
T3.answer = 3

T4 = Texts(1,2,3,4)
T4.text = "TEXTS/TEST4.txt"
T4.question = "The positive effect of Mozart's music on special needs children..."
T4.options = ["1: only became apparent after some time.", "2: was discovered quite accidentally.", "3: confirmed earlier research findings."]
T4.answer = 2

T5 = Texts(1,2,3,4)
T5.text = "TEXTS/TEST5.txt"
T5.question = "Research carried out by the University of Reading led to the conclusion that..."
T5.options = ["1: exposure to music causes significant physiological changes.", "2: appreciation of music is related to physiological characteristics.", "3: listening to music increases the capacity to absorb new information."]
T5.answer = 1

T6 = Texts(1,2,3,4)
T6.text = "TEXTS/TEST6.txt"
T6.question = "In Oliver Sack's experience music can help Parkinson patients to..."
T6.options = ["1:recover their ability to speak.", "2: overcome their difficulty in moving.", "3: restore their sense of balance."]
T6.answer = 2

T7 = Texts(1,2,3,4)
T7.text = "TEXTS/TEST7.txt"
T7.question = "What does Oliver Sacks say here about music?"
T7.options = ["1: It may stimulate the recovery from brain damage.", "2: It may provide a framework of time and space.", "3: It may support deficient parts of the brain."]
T7.answer = 3

T8 = Texts(1,2,3,4)
T8.text = "TEXTS/TEST8.txt"
T8.question = "What is said here about Mozart as a child?"
T8.options = ["1: His exceptional talents went hand in hand with a problematic childhood.", "2: He compensated for his physical weakness by developing his mind.", "3: He had to overcome serious problems before his talents were recognized."]
T8.answer = 1

#-----------------------------------------------------------------------------------#
txtObj = [T1, T2, T3, T4]
currText = txtObj[0]
#-----------------------------------------------------------------------------------#

buttW = 800;
buttH = 80;
B1 = Button((width/2)-(buttW/2),200,buttW,buttH)
B2 = Button(B1.locationX,B1.locationY+buttH+10,buttW,buttH)
B3 = Button(B1.locationX,B2.locationY+buttH+10,buttW,buttH)

A1 = Answer((width/2),B1.locationY+10,currText.options[0])
A2 = Answer((width/2),B2.locationY+10,currText.options[1])
A3 = Answer((width/2),B3.locationY+10,currText.options[2])

info = 'press the number corresponding to the correct answer..'

data = open (T1.text, "r")
##add questions for texts

word_speed = -20 # pixels 
basis_frame_time = 1.0 / FPS

#showwords of linereader- and for questionscreen
def showWord(word, location):
    text = myfont.render(word,1,(0,0,0))
    textHeight =text.get_height()
    screen.blit(text,(location ,(height/2)-(textHeight/2)))
def showWordQ(word,font, locationX, locationY):
    text = font.render(word,1,(0,0,0))
    size = font.size(word)
    textHeight =text.get_height()
    screen.blit(text,(locationX-(size[0]/2),locationY+(textHeight/2)))
def makeTXTarray(Textfile):
	data = open(Textfile, "r")
	Arr =[]
	for lines in data:
		for words in lines.split():		
			Arr.append(words)

	for dot in range(0,10):
		Arr.append(".")
	return(Arr)
def calcObjectTracker(Arr):
	objectTrackers = [0,1]
	objectTrackers = numpy.array(objectTrackers)
	for i in range (0,len(objectTrackers)):
		if i == 0:
			objectTrackers[i] = 1200
		else:
			getSize = myfont.size(Arr[i-1])
			objectTrackers[i] = objectTrackers[i-1]+ getSize[0] + 10
	return(objectTrackers)
##array of all the words in the text works!!


#-------------------------------------------------------------------------START-OF-GAMELOOP---------------------------------------------------------------------------------#
def setToStart(object):
	Arr = makeTXTarray(object.text)
	objectTrackers = calcObjectTracker(Arr)
	i = 0
	count = 0
	countdown = 10
	start_time = time.time()
	question_screen = False
	given_answer = 0
	return(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer)


(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
textCounter = 0
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
	      	print("Current speed is: "+ str(word_speed))
	      if event.key == pygame.K_DOWN:
	      	word_speed +=1
	      	print("Current speed is: "+ str(word_speed))
	      if word_speed >-2:
	      		word_speed = -1
	      
	      if event.key == pygame.K_SPACE:
	          time.sleep(10)
	      if event.key==pygame.K_q:
	      		sys.exit()
	      if question_screen ==True:
	      	if event.key==pygame.K_1 or event.key==pygame.K_KP1:
	      		given_answer = 1
	      		if given_answer == currText.answer:
	      			print("This is the correct answer: " + currText.options[0])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	      	if event.key==pygame.K_2 or event.key==pygame.K_KP2:
	      		given_answer = 2
	      		if given_answer == currText.answer:
	      			#---------------------------------------------------WORK IN PROGRESS--------------------------------------------------------------###
	      			print("This is the correct answer: " + currText.options[1])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	      			#---------------------------------------------------WORK IN PROGRESS--------------------------------------------------------------###
	      	if event.key==pygame.K_3 or event.key==pygame.K_KP3:
	      		given_answer = 3
	      		if given_answer == currText.answer:
	      			print("This is the correct answer: " + currText.options[2])
	      			textCounter += 1
	      			if textCounter < len(txtObj):
	      				currText = txtObj[textCounter]
	      				(Arr, objectTrackers, i, count, countdown, start_time, question_screen, given_answer) = setToStart(currText)
	      			else:
	      				sys.exit()
	if question_screen == False:
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
				objectTrackers[1] = objectTrackers[0] + getSize[0] + storage + 13
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
			screen.blit(bg,(0,0))
			showWord(sentence, objectTrackers[0])
			#print(sentence)
		if countdown == 0:		
			#At the end print out how many words read
			end = "words read = " + str(i)
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
			question_screen = True
			time.sleep(1)
		screen.blit(bg,(0,0))	
		showWord(sentence, objectTrackers[0])
	elif question_screen == True:
		screen.blit(testbg,(0,0))
				##questions and info	
		showWordQ(info,info_font,width/2,20)
		showWordQ(currText.question, question_font, width/2, 80)


		##show Answers in rectangles
		pygame.draw.rect(screen, WHITE,(B1.locationX,B1.locationY,B1.buttW,B1.buttH));
		showWordQ(A1.answer,answer_font, A1.locationX, A1.locationY)

		pygame.draw.rect(screen, WHITE,(B2.locationX,B2.locationY,B2.buttW,B2.buttH));
		showWordQ(A2.answer,answer_font, A2.locationX, A2.locationY)

		pygame.draw.rect(screen, WHITE,(B3.locationX,B3.locationY,B3.buttW,B3.buttH));
		showWordQ(A3.answer,answer_font, A3.locationX, A3.locationY)

		
	pygame.display.update()
	pygame.display.flip()
>>>>>>> ceabfd6f73bfcc6ab7445a719113d42f8fc69923
