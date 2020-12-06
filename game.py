# Text RPG Attempt 3
### Imports ###
import cmd # allows command prompt fnction
import textwrap # wraps text to command prompt screen
import os
import sys # allows system functions
import time # contains counter functions
import random # contains rnd functionsx

screen_width = 100
### Player ###
class player:
    def __init__(self):
        self.name = ''
        self.skill = ''
        self.hp = 100
        self.bag = []
        self.equip = [ None, None, None]
        self.position = 'center'
player1 = player() # Initialise the player before anything else

class setting:
    def __init__(self):
        self.speach = True
settings = setting()
#
# #### map setup ###
# location = {
# 'center': {
#     DESCRIPTION: "You find yourself standing normally on clouds, strangely\n.",
#     INFO: "Even more strange than standing on clouds is the\nbird that begins speaking to you.\n",
#     SIDE_UP: 'north',
#     SIDE_DOWN: 'south',
#     SIDE_LEFT: 'east',
#     SIDE_RIGHT: 'west',
# },
#     'north': {
#         DESCRIPTION: "You find yourself standing normally on clouds, strangely.",
#         INFO: "Even more strange than standing on clouds is the\nbird that begins speaking to you.\n",
#         SIDE_UP: 'wall',
#         SIDE_DOWN: 'center',
#         SIDE_LEFT: 'east',
#         SIDE_RIGHT: 'west',
#     },
#     'east': {
#         DESCRIPTION: "You find yourself in lush woodlands, bursting with wildlife\nand a cacaphony of chirping.",
#         INFO: "A rough-looking man sits next to a little cabin.\nHis eyes are glued to bird-watching binoculars.",
#         SIDE_UP: 'north',
#         SIDE_DOWN: 'south',
#         SIDE_LEFT: 'center',
#         SIDE_RIGHT: 'wall',
#     },
#     'south': {
#         DESCRIPTION: 'You find yourself encompassed by strong winds and sandy dunes.',
#         INFO: 'A terrified looking man is hiding among some cacti.',
#         SIDE_UP: 'center',
#         SIDE_DOWN: 'wall',
#         SIDE_LEFT: 'west',
#         SIDE_RIGHT: 'east',
#     },
#     'west': {
#         DESCRIPTION: "You find yourself next to a still, soothing pond.\nAn old man gazes at a table nearby.",
#         INFO: "You greet the old man.\nHe beckons you to look at the intricate twelve-sided table.",
#         SIDE_UP: 'north',
#         SIDE_DOWN: 'south`',
#         SIDE_LEFT: 'wall',
#         SIDE_RIGHT: 'center',
#     }
# }
#
# ### moving player ###
# def move_player(move_dest):
#     print("\nYou have moved to the " + move_dest + ".")
#     player1.position = move_dest
#     # print_location()
#
# ### move action ###
# def move():
#     move_dest = "wall"
#
#     while move_dest == "wall":
#         direction = input("Where would you like move to? ")
#         if direction.lower() == 'forward':
#             move_dest = location[player1.position][SIDE_UP] #if you are on ground, should say north
#         elif direction.lower() == 'left':
#             move_dest = location[player1.position][SIDE_LEFT]
#         elif direction.lower() == 'right':
#             move_dest = location[player1.position][SIDE_RIGHT]
#         elif direction.lower() == 'back':
#             move_dest = location[player1.position][SIDE_DOWN]
#         else:
#             print("Invalid direction command, try using forward, back, left, or right.\n")
#             move()
#     move_player(move_dest)
#     return



### Prompt ###
def prompt():
    print("What would you like to do?")
    action = input("> ")
    action = check(action)
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'inspect', 'examine', 'look', 'search']
    while action.lower() not in acceptable_actions:
        print("Unknown action command, please try again.\n")
        action = input("> ")
    if action.lower() in acceptable_actions[:5]:
        pass # move()
    elif action.lower() in acceptable_actions[5:]:
        pass #examine()

### my cheat ###
def ask_speach():
    choice = input('Do you want the game to include speach time delays? Y/N')
    if choice.lower() == 'n':
        settings.speach = False
    else:
        settings.speach = True

### death countdown ##
def death(dmg):
    if (player1.hp - dmg ) <= 0:
        while player1.hp > 0:
            print(f'{player1.hp}  \r', end="")
            time.sleep(0.02)
            player1.hp = player1.hp - 1
        print('BAMMMM!')
        speak('"Ughh... Cahunk!\n"', 0.02)
        speak('So long fair friend, may you rest in peace...\n', 0.03)
        input('> ')
        print('####################################')
        print('           ~~~You Died~~~           ')
        print('####################################')
        input('> ')
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
    while choice.lower() not in ['start', 'help', 'exit', 'e', 's', 'h']:
        speak('I do not understand, please choose again.', 0.01)
        choice = input('> ')
    if choice.lower() in ['s', 'start']:
        ask_speach()
        game()
    elif choice.lower() in ['h', 'help']:
        help_menu()
        title_choice()
    elif choice.lower() in ['exit', 'e']:
        sys.exit()


### Help Menu ###
def help_menu():
    os.system('cls') # clears the commad prompt
    print('####################################')
    print('           Help Menu           ')
    print('####################################')
    print('1. You must type all commands')
    print('2. Use UP, RIGHT, LEFT, DOWN to move character')
    print('3. INTERACT to engage, use, look at an object')
    x = input('> ')

### pause menu ###
def pause_menu():
    print(2*'\n')
    print('####################################')
    print('            Pause Menu              ')
    print('####################################')
    print('       - Character Profile -        ')
    print('             - Map -                ')
    print('             - Help -               ')
    print('             - Back -               ')
    print('             - Exit -               ')
    pause_choice = input('>')
    if pause_choice.lower() in ['c', 'character profile']:
        view_profile()
        pause_menu()
    elif pause_choice.lower() in ['m', 'map']:
        view_map()
        pause_menu()
    elif pause_choice.lower() in ['h', 'help']:
        help_menu()
        pause_menu()
    elif pause_choice.lower() in ['exit', 'e']:
        sys.exit()
    elif pause_choice.lower() in ['back', 'b']:
        pass
    print(2*'\n')

### Character Profile ###
def view_profile():
    os.system('cls')
    print('####################################')
    print('         Character Profile          ')
    print('####################################')
    print(f'Name: {player1.name}')
    print(f'Skill: {player1.skill}')
    print(f'hp: {player1.hp}')
    choice = input('> ')

### View Map ###
def view_map():
    print('####################################')
    print('               Map                  ')
    print('####################################')
    if 'map' in player1.bag:
        pass
    else:
        print('It seems you do not have a map yet.')
    choice = input('> ')


### input check ###
def check(x):
    if x.lower() in ['s', 'p', 'pause', 'start', 'end', 'q', 'exit']:
        pause_menu()
        return input('> ')
    return x


### start_game ###
def game():
    while player1.hp in range(0,101):
        speak('PROSCH DISTRICT 4B: 5th rebmet \n')
        speak('You there .............. NUMBER FOURTY FIVE!\nIve forgotten, What is your name again?\n')
        choice = input('> ')
        choice = check(choice)
        player1.name = choice
        speak('(You have a gun in your back pocket... kill your self?)')
        choice = input('> ')
        choice = check(choice)
        if choice.lower() in ['ok', 'yes', 'i will', 'alright', "i'll do it"]:
            death(100)

title_screen()
