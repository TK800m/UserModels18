# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:46:09 2018

@author: Sjaak
"""

import pygame, sys, time
#variables needed. Delay, TXTsource and syllBonus most important inputs
delay = 0.4
wordCount = 0
BGcolor = (255,255,255)
W = 900
H = 600
TXTsource = "C:/Users/Sjaak/ownCloud/Master HMC/2018-2019/User Models/test.txt"
TXTsource2 = "C:/Users/Sjaak/ownCloud/Master HMC/2018-2019/User Models/T1.txt"
TXTsource3 = "C:/Users/Sjaak/ownCloud/Master HMC/2018-2019/User Models/mary.txt"
pygame.font.init()
screen = pygame.display.set_mode((W,H))
screen.fill((BGcolor))
myfont = pygame.font.Font(None, 90)
f = open(TXTsource3,"r")
syllBonus = delay/10

#functions
def showWord(word, wordCount):
    text = myfont.render(word,1,(0,0,0))
    WL = len(word)
    screen.blit(text, (W/2-(WL*16),H/2))
    wordCount += 1
    pygame.display.update()
    return wordCount

def bg(BGcolor):
    screen.fill((BGcolor))
    pygame.display.update()

def numOfSyllables(word):
    syllables = 0
    for x in range (0, len(word)-1):
        if word[x+1] in ["a","e","i","o","u"]:
            if x+1<len(word)-1 and word[x+1] in ["a","e","i","o","u"]:
                x+=1
        syllables += 1
    return syllables

#Main body for reading the txt
##read every line and every word
start_time = time.time()
for line in f:
    for word in line.split():
        #get the last letter to check if it is a special sign
        lastLetter = len(word)-1
        syllables = numOfSyllables(word)
        if word[lastLetter] == "," or word[lastLetter]==".":
            specialSign =  word[lastLetter]
            word = word[:-1]
            #show the word first and then the special sign separate
            wordCount = showWord(word, wordCount) -1

            #check how many syllables the word has for syllBonus
            if syllables >2:
                delay = delay + syllables*syllBonus
                time.sleep(delay)
                delay = delay - syllables*syllBonus
            else:
                time.sleep(delay)
            bg(BGcolor)
            #print special sign next, so put in word and delete #syllables
            word = specialSign
            syllables = 0

        #print the word on screen and add syllBonus in delay
        wordCount = showWord(word, wordCount)    
        if syllables >2:
                delay = delay + syllables*syllBonus
                time.sleep(delay)
                delay = delay - syllables*syllBonus
        else:
            time.sleep(delay)

        #check during the loops for key presses and do stuff when key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #increase/decrease speed of words 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if delay >= 0.1:
                        delay -= 0.05
                if event.key == pygame.K_DOWN:
                    delay += 0.05
                if event.key == pygame.K_SPACE:
                    time.sleep(10)
        bg(BGcolor)

#At the end print out how many words read
end = "words read = " + str(wordCount)
WL = len(end)
end = myfont.render(end,1,(0,0,0))
screen.blit(end, (200,H/4))

#Calc the time it took to reed the words and print it
totalTime = time.time()-start_time
print("%.2f" %totalTime)
timed = "this took " + str("%.2f" %totalTime)+ "sec"
WL = len(timed)
timed = myfont.render(timed,1,(0,0,0))
screen.blit(timed, (200,H/4*3))
pygame.display.update()
time.sleep(5)

pygame.display.quit()
