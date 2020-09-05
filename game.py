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
    print('           Welcome to Uya           ')
    print('####################################')
    print('              - Start -             ')
    print('              - Help -              ')
    print('              -Exit -               ')

title_screen()
