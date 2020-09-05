# Text RPG Attempt 2
### Imports ###
import cmd # allows command prompt fnction
import textwrap # wraps text to command prompt screen
import os
import sys # allows system functions
import time # contains counter functions
import random # contains rnd functions

screen_width = 100
### Speech Text Function ###
def speak(x):
    for letter in x:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

### Title Screen ###
def title_screen():
    os.system('cls') # clears the commad prompt
    print('####################################')
    print('          Welcome to Ullysis        ')
    print('####################################')
    print('              - Start -             ')
    print('              - Help -              ')
    print('              - Exit -               ')
    title_choice()

### Title Screen Choice ###
def title_choice():
    choice = input('> ')
    while choice.lower() not in ['start', 'help', 'exit']:
        speak('I do not understand, please choose again.')
        choice = input('> ')
    if choice.lower() == 'start':
        start_game()
    elif choice.lower() == 'help':
        help_menu()
    elif choice.lower() == 'exit':
        sys.exit()

### Help Menu ###
def help_menu():
    print('####################################')
    print('           Help Menu           ')
    print('####################################')
    print('1. You must type all commands')
    print('2. Use UP, RIGHT, LEFT, DOWN to move character')
    print('3. INTERACT to engage, use, look at an object')
    back = input('                 - Back -                    ')
    if back.lower() == 'back':
        title_screen()

### start_game ###
def start_game():
    speak('PROSCH DISTRICT 4B: 5th rebmet')
    speak('You there .............. NUMBER FOURTY FIVE! What is your name?')
    choice = input('> ')
    if choice.lower in ['q', 'quit', 'exit', 'finish', 'end']:
            sys.exit
    # character_setup()

title_screen()
