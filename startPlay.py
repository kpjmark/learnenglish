# Python3.0+

import pygame, sys, time, random, re, readFile
from pygame.locals  import *

pygame.init()  

# open file
openWordNote = open('wordlist.md','r')

# write lists
def mainSeeWordList():
    wordList = re.findall(r'[(](.*?)[)]', openWordNote.read())

    typein = int(input('Enter the number of loops:'))
    for i in range(typein):

# Start play
        wordNumber = random.randint(0, len(wordList))
        typeCorrectList = ['amazing', 'wonderful', 'great']
        typeSoundnumber = random.randint(0, 2)
        typeCorrectSound = pygame.mixer.Sound('soundFile/allDone/' + typeCorrectList[typeSoundnumber] + '.wav')
        pygame.mixer.music.load('soundFile/' + wordList[wordNumber] + '.wav')
        pygame.mixer.music.play(3, 0.0)
        musicPlaying = True

        print('Please enter the words you hear the most')
        typeWord = input()
        if typeWord == wordList[wordNumber]:
            pygame.mixer.music.stop()
            time.sleep(0.2)
            typeCorrectSound.play()
            if musicPlaying:
                time.sleep(2.5)
                print('ok')
        else:
            pygame.mixer.music.stop()
            time.sleep(0.2)
            print('+******************************************+')
            print('+' + readFile.wordClearList[wordNumber] + '+')
            print('+                                          +')
            print('+******************************************+')


mainSeeWordList()
openWordNote.close()
