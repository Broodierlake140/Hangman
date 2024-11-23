import random
import asyncore
from random import randint
from typing import Counter

import pygame
from gc import is_finalized
from itertools import filterfalse
from pygame.display import update
from pygame.examples.cursors import image
from pygame.locals import *
import sys
from setuptools import setup
from setuptools.glob import iglob
from time import sleep
global  bad_list, Banned, letter1, letter2, letter3, letter4, letter5
global letter6, letter7, letter8, letter9, letter10, Loops, Word, Bad, Update
global done, Correct, new, End, Dead, life, Letters, Limb, Naught, Limbs, Guess
Limbs = []
Limb = 0
Dead = False
Done = False
Correct = 0
Letters = 0
Game = True
Update = True
Banned = []
Loops = True
List = []
Counter = 0
cat = ["cat"]
Letter1 = ""
Letter2 = ""
Letter3 = ""
Letter4 = ""
Letter5 = ""
Letter6 = ""
Letter7 = ""
Letter8 = ""
Letter9 = ""
Letter10 = ""
life = 6
End = False
reset = False
pygame.init()
Screen = pygame.display.set_mode((800, 800))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Screen.fill(WHITE)
font = pygame.font.Font('freesansbold.ttf', 38)
FPS = pygame.time.Clock()
FPS.tick(60)
new = False
bad_list = ", ".join(Banned)
New = True
Naughty = ""
Guess = ""
def Checker(a):
    global Naughty
    global Update
    global Banned
    global done
    global Correct, bad_list, text, Screen
    global Limbs

    Update = True
    for i, letter in enumerate(Word):



        if a == letter and a not in Banned:
            found = True
            Banned.append(a)


        else:
            if a not in Word and a not in Banned:
                temp = []
                global life

                temp.append(a)
                Banned.append(a)
                Naughty = ", ".join(temp)
                life = life - 1


def KeyPress():
    global New
    temp = True
    while temp == True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                temp = False
            elif event.type == pygame.KEYDOWN:  # Check for key press
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                    temo = False
                elif event.key == pygame.K_BACKSPACE:
                    New = True
                    temp = False



def Clear():
    global Screen, WHITE
    Screen.fill(WHITE)

def Setup():
    global Update, new, Loops, Dead
    global Screen, font, Update, done, life, End
    Counter = 0
    new = True
    Update = False
    for i in Word:
        Counter +=1

        if Counter == 1:
            Letter1 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (400 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 2:
            Letter2 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (450 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 3:
            Letter3 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (500 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 4:
            Letter4 == i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (550 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 5:
            Letter5 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (600 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 6:
            Letter6 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (650 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 7:
            Letter7 == i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (700 , 100 )
            Screen.blit(text, textRect)
        elif Counter == 8:
            Letter8 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (400 , 200 )
            Screen.blit(text, textRect)
        elif Counter == 9:
            Letter9 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (450 , 200 )
            Screen.blit(text, textRect)
        elif Counter == 10:
            Letter10 = i
            text = font.render('_', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (500 , 200 )
            Screen.blit(text, textRect)





def Words():
    global Counter, bad_list, Banned, Word, Counter, Letters, life, Done, Dead, Limb, Naughty, Guess
    Naughty = ""
    life = 6
    bad_list = ", "
    Banned = []
    Word = ""
    Guess = ""
    Done = False
    Dead = False
    Limb = 0
    with open("Words.txt", "r") as file:
        words = [line.strip() for line in file]  # Read all words and strip whitespace/newlines
        Word = random.choice(words).lower()  # Randomly select a word and convert to lowercase
        for i in Word:
            Counter +=1
            Letters +=1





#Shown Letters
pygame.display.set_caption("Hangman")



while Loops == True:
    if New == True:
        Words()
        New = False
    if life == 0:
        Dead = True
    Clear()
    if Limb >= 1:
        pygame.draw.circle(Screen, BLACK, (80, 180), 30, width=3)
        if Limb >= 2:
            pygame.draw.line(Screen, BLACK, (80, 210), (80, 340), (3))
            if Limb >= 3:
                pygame.draw.line(Screen, BLACK, (80, 230), (40, 270), (3))
                if Limb >= 4:
                    pygame.draw.line(Screen, BLACK, (80, 230), (120, 270), (3))
                    if Limb >= 5:
                        pygame.draw.line(Screen, BLACK, (80, 340), (40, 380), (3))
                        if Limb >= 6:
                            pygame.draw.line(Screen, BLACK, (80, 340), (120, 380), (3))


    pygame.draw.line(Screen, BLACK, (80, 100), (330, 100), (3))
    pygame.draw.line(Screen, BLACK, (330, 100), (330, 500), (3))
    pygame.draw.line(Screen, BLACK, (300, 500), (360, 500), (3))
    pygame.draw.line(Screen, BLACK, (80, 100), (80, 150), (3))
    Update = True
    Setup()
    global text
    if Guess == Word.lower():
        Done = True
        Screen.fill(WHITE)
        text = font.render('You Win!, Press Backspace To Continue', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (400 , 400 )
        Screen.blit(text, textRect)
        text = font.render('Or Space To Exit.', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (400 , 500 )
        Screen.blit(text, textRect)
        pygame.display.update()
        KeyPress()


    if Dead == True:
        pressed = pygame.key.get_pressed()
        Dead = False
        Screen.fill(WHITE)
        text = font.render('You Lose, Press Backspace To Continue', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (400 , 400 )
        Screen.blit(text, textRect)
        text = font.render('Or Space To Exit.', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (400 , 500 )
        Screen.blit(text, textRect)
        pygame.display.update()
        KeyPress()




    bad_list = ", ".join(Banned)
    Correct = 0
    if life > 0 and Done == False:
        Guess_list = []
        for i, letter in enumerate(Word):
            if letter in bad_list:  # If the letter has been guessed, display it
                text = font.render(letter, True, BLACK)
                x_offset = 400 + (i % 10) * 50
                y_offset = 100
                if x_offset > 700:
                    x_offset = x_offset - 350
                    y_offset = 200
                textRect = text.get_rect()
                textRect.center = (x_offset, y_offset)
                Screen.blit(text, textRect)
                Correct +=1
                Guess_list.append(letter)
        Guess = "".join(Guess_list)

    if life > 0 and Done == False:
        if Naughty not in enumerate(Word) and Naughty != "":
            Limb +=1
            Naughty = ""
        text = font.render(bad_list, True, BLACK)
        textRect = text.get_rect()
        textRect.center = (400, 600)

        Screen.blit(text, textRect)
        pygame.display.update()





    pressed = pygame.key.get_pressed()






    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if life > 0 and Done == False:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            Key = getattr(pygame, f"K_{letter}")
            if pressed[Key] and letter not in Banned:
                Checker(letter)









