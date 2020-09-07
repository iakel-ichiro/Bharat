move_dest = "wall"
while move_dest == "wall":
    direction = input('>:')
    if direction.lower() == 'forward':
        move_dest = 'wall' #if you are on ground, should say north
    elif direction == 'left':
        move_dest = 'north'
    elif direction == 'right':
        move_dest = 'center'
    elif direction == 'back':
        move_dest = 'south'
    else:
        print("Invalid direction command, try using forward, back, left, or right.\n")
        move_dest = 'wall'
print(move_dest)
