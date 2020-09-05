# Text RPG Attempt 2
### Imports ###
import cmd # allows command prompt fnction
import textwrap # wraps text to command prompt screen
import os
import sys # allows system functions
import time # contains counter functions
import random # contains rnd functions

screen_width = 100

### Title Screen ###
def title_screen():
    os.system('cls') # clears the commad prompt
    print('####################################')
    print('           Welcome to Ullysis           ')
    print('####################################')
    print('              - Start -             ')
    print('              - Help -              ')
    print('              -Exit -               ')
    title_choice()

### Title Screen Choice ###
def title_choice():
    choice = input('> ')
    while choice.lower() not in ['start', 'help', 'exit']:
        print('I do not understand, please choose again.')
        choice = input('> ')
    if choice.lower() == 'start':
        pass #start_game()
    elif choice.lower() == 'help':
        pass #help_menu()
    elif choice.lower() == 'exit':
        sys.exit()





title_screen()
