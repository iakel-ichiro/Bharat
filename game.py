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
        self.position = 'b2'
player = player() # Initialise the player before anything else

class setting:
    def __init__(self):
        self.speach = True
settings = setting()

# #### map setup ###
PLACENAME = 'placename'
DESCRIPTION = 'description'
INFO = 'info'
UP = 'north', 'up'
DOWN = 'south', 'down'
LEFT = 'left',  'east'
RIGHT = 'right','west'

# Nested Dictionary

locations = {
'b2': {
    PLACENAME: 'Proscht District',
    DESCRIPTION: "You find yourself standing normally on clouds, strangely\n.",
    INFO: "Even more strange than standing on clouds is the\nbird that begins speaking to you.\n",
    UP: 'b1',
    DOWN: 'b3',
    LEFT: 'a2',
    RIGHT: 'c2',
},
    'b1': {
        PLACENAME: 'Skyland',
        DESCRIPTION: "You find yourself standing normally on clouds, strangely.",
        INFO: "Even more strange than standing on clouds is the\nbird that begins speaking to you.\n",
        UP: 'b3',
        DOWN: 'b2',
        LEFT: 'x',
        RIGHT: 'x',
    },
    'b3': {
        PLACENAME: 'Woodland',
        DESCRIPTION: "You find yourself in lush woodlands, bursting with wildlife\nand a cacaphony of chirping.",
        INFO: "A rough-looking man sits next to a little cabin.\nHis eyes are glued to bird-watching binoculars.",
        UP: 'b2',
        DOWN: 'b1',
        LEFT: 'x',
        RIGHT: 'x',
    },
    'a2': {
        PLACENAME: 'Duneland',
        DESCRIPTION: 'You find yourself encompassed by strong winds and sandy dunes.',
        INFO: 'A terrified looking man is hiding among some cacti.',
        UP: 'x',
        DOWN: 'x',
        LEFT: 'c2',
        RIGHT: 'b2',
    },
    'c2': {
        PLACENAME: 'Pondland',
        DESCRIPTION: "You find yourself next to a still, soothing pond.\nAn old man gazes at a table nearby.",
        INFO: "You greet the old man.\nHe beckons you to look at the intricate twelve-sided table.",
        UP: 'x',
        DOWN: 'x',
        LEFT: 'b2',
        RIGHT: 'a2',
    }
}

#### Visual Map######
def print_map_locations():
    print('\n' + ('#' * (4 + len(locations[player.position][PLACENAME]))))
    print('# ' + locations[player.position][PLACENAME].upper() + ' #')
    print('# ' + locations[player.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(locations[player.position][PLACENAME]))))

# ### moving player ###
def move_player(move_dest):
    player.position = move_dest
    print(move_dest)
    print("\nYou have moved to the " + locations[move_dest][PLACENAME] + ".")

    print_map_locations()

# ### move action ###
def move():
    direction = input("Where would you like move to? (up,down, left, right) ")
    if direction.lower() == 'up':
        move_dest = locations[player.position][UP]
    elif direction.lower() == 'left':
        move_dest = locations[player.position][LEFT]
    elif direction.lower() == 'right':
        move_dest = locations[player.position][RIGHT]
    elif direction.lower() == 'down':
        move_dest = locations[player.position][DOWN]
    elif direction.lower() not in ['up', 'left', 'down', 'right']:
        print("Invalid direction command, try using forward, back, left, or right.\n")
        move()
    if move_dest == 'x':
        print("There is nothing to the " + direction.upper() + "of this place")
        move()



    move_player(move_dest)
    return



### Prompt ###
def prompt():
    print("What would you like to do?")
    action = input("> ")
    action = check(action)
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'inspect', 'examine', 'look', 'search']
    while action.lower() not in acceptable_actions:
        print("Unknown action command, please try again.\n")
        action = input("> ")
    if action.lower() in acceptable_actions[:3]:
        move()
    elif action.lower() in acceptable_actions[4:]:
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
    if (player.hp - dmg ) <= 0:
        while player.hp > 0:
            print(f'{player.hp}  \r', end="")
            time.sleep(0.02)
            player.hp = player.hp - 1
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
        start_game()
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
    print(f'Name: {player.name}')
    print(f'Skill: {player.skill}')
    print(f'hp: {player.hp}')
    choice = input('> ')

### View Map ###
def view_map():
    print('####################################')
    print('               Map                  ')
    print('####################################')
    if 'map' in player.bag:
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

def game_loop():
    while (player.hp > 0):
        prompt()

def start_game():
    os.system('cls')
    speak('You there, prisnor 47.... Whats your name')
    player.name = input('> ')
    speak("Eh... Oh, I've heard of you, the boys say you were a skillsman. What type where ya?")
    skill_class = input('Tell the gaurdsman your skill: (Resistant, Breeder, Strongback, Origin) \n> ')
    if skill_class.lower() in ['resistant','breeder', 'strongback', 'origin']:
        player.skill = skill_class

    # set skill class attributes


    ## Game begins##
    game_loop()
title_screen()
