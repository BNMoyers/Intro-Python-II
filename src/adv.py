# Imports
import textwrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Welcome

print()
print('~' * 80)
print()
print("Welcome to the Caverns.")
# Make a new player object that is currently in the 'outside' room.
player = Player('outside')
valid_input = ['n', 'e', 's', 'w']
# Write a loop that:
#
while True:
    print()
    print('~' * 80) 
    print()
    print("You find yourself at the:")
    print()
    print(room[player.current_room].room_name)
    print('=' * len(room[player.current_room].room_name))
    print()
    print('\n' .join(textwrap.wrap(room[player.current_room].room_description, 75)))
    print()
    print('~' * 80) 
    print()
    print("To continue your adventure, please make a selection...")
    print()

    move = (str(input("[n] North [e] East [s] South [w] West [q] Quit ")))

    if move == "q":
        break
    elif move == "n":
        pass
    elif move == "e":
        pass
    elif move == "s":
        pass
    elif move == "w":
        pass
    else: 
        print('\n'.join(textwrap.wrap("You try to move, but find yourself glitching back to the same spot. An angry programmer goblin pokes her head out from behind the bushes and shouts 'hey, you, idiot! Read the sign!' while gesturing wildly at a wooden board with the valid inputs on it. You better do what she says.")))

    

    
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
