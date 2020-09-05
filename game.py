# Text RPG Attempt 2
### Imports ###
import cmd # allows command prompt fnction
import textwrap # wraps text to command prompt screen
import os
import sys # allows system functions
import time # contains counter functions
import random # contains rnd functions

screen_width = 100
### Player ###
class player:
    def __init__(self):
        self.name = ''
        self.skill = ''
        self.hp = 100
player1 = player() # Initialise the player before anything else

class setting:
    def __init__(self):
        self.speach = True
settings = setting()

def ask_speach():
    choice = input('Do you want the game to include speach time delays? Y/N')
    if choice.lower() == 'n':
        settings.speach = False

### death countdown ##
def death(dmg):
    if (player1.hp - dmg ) <= 0:
        while player1.hp > 0:
            print(f'{player1.hp}  \r', end="")
            time.sleep(0.02)
            player1.hp = player1.hp - 1
        speak('"Ughh... Cahunk!\n"', 0.05)
        speak('So long fair friend, may you rest in peace...\n', 0.03)
        print('####################################')
        print('           ~~~You Died~~~           ')
        print('####################################')
        title_screen()


### Speech Text Function ###
def speak(x,spd = 0.03):
    if settings.speach:
        for letter in x:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(spd)
    else:
        print(x)

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
        speak('I do not understand, please choose again.', 0.01)
        choice = input('> ')
    if choice.lower() == 'start':
        ask_speach()
        game()
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

### pause menu ###
def pause_menu():
    print('####################################')
    print('            Pause Menu              ')
    print('####################################')
    print('       - Character Profile -        ')
    print('             - Map -                ')
    print('             - Help -               ')
    print('             - Back -               ')
    print('             - Exit -               ')
    pause_choice = input('                 - Back -                    ')
    if pause_choice.lower() == 'character profile':
        pass # view_profile()
    elif pause_choice.lower() == 'map':
        pass # view_map()
    elif pause_choice.lower() == 'help':
        help_menu()
    elif choice.lower() == 'exit':
        sys.exit()
    elif pause_choice.lower() == 'back':
        pass
### input check ###
def check(x):
    if x.lower() in ['s', 'p', 'pause', 'start', 'end', 'q', 'exit']:
        pause_menu()

### start_game ###
def game():
    while player1.hp in range(0,101):
        speak('PROSCH DISTRICT 4B: 5th rebmet \n')
        speak('You there .............. NUMBER FOURTY FIVE!\nIve forgotten, What is your name again?\n')
        choice = input('> ')
        check(choice)
        player1.name = choice
        speak('(You have a gun in your back pocket... kill your self?)')
        choice = input('> ')
        check(choice)
        if choice.lower() in ['ok', 'yes', 'i will', 'alright', "i'll do it"]:
            death(100)

title_screen()
