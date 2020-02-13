# Imports
import textwrap

from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    """North of you, the cave mouth beckons""",[]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[]),
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

# Declare all Items
item = {
    "symbol": Item("Holy Symbol", """A tiny dwarven anvil hanging from a bronze chain"""),
    "mouse": Item("Mousey", """A mouse's skull which whispers strange names to you at night"""),
    "stick": Item("Walking Stick", """A wooden walking stick with six jingling rings"""),
    "keyring": Item("Ancient Key", """An iron key engraved with the symbol of a fell vampire"""),
    "decoy": Item("Pouch", """A small leather pouch of flat stones"""),
    "gauntlet": Item("Guantlet", """A bronze gauntlet, recently given to you by an old soldier """),
    "rose": Item("Rose", """A petrified rose"""),
    "figurine": Item("Magic Figurine", """An iron figurine of a warrior which stabs you with a tiny spear when anyone approaches"""),
}

# Main
#

# Welcome

print()
print('~' * 80)
print()
print("Welcome to the Caverns.")
# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name, adventurer?"),room['outside'])

print(f'Hello {player.name}.\n\n You are {player.current_room.room_name}')
# def change_room(current_room, direction):

# Write a loop that:
#
while True:
    print()
    print('~' * 80) 
    print()
    print("You are:")
    print()
    print(f"{player.current_room.room_name}")
    print('=' * len(player.current_room.room_name))
    print()
    print(player.current_room)
    print()
    print('~' * 80) 
    print()
    print("To continue your adventure, please make a selection...")
    print()

    player_choice = (str(input("[n] North [e] East [s] South [w] West [v] View Inventory [i]Investigate Room [q] Quit ")))
    if player_choice == "q":
        break
    elif player_choice in ["n", "e", "s", "w"]:
        player.move(player_choice)
    elif player_choice == "v":
        player.view_inventory()
    elif player_choice == "i":
        pass
    else: 
        print(f"\n\nYou try to move, but find yourself glitching back to the same spot. An angry programmer goblin pokes her head out from behind the bushes and shouts 'hey, you, idiot! Read the sign!' while gesturing wildly at a wooden board with the valid inputs on it. You better do what she says.")

    

    
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
