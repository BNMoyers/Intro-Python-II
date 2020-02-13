# Write a class to hold player information, e.g. what room they are in
# currently.

# imports
from item import Item

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("\n\nYou run headfirst into a blank wall. Looks like you can't go that way.\n\n")
    
    def view_inventory(self):
        print("You are carrying: \n\n")
        for item in self.inventory:
            print(f"\n\n{item.item_name}\n\n{item.item_description}\n\n")
    
    def investigate(self):
        print("Looking around the room, you find: \n\n")
        for item in self.current_room.room_inventory:
            print(f"{item.item_name}\n\n{item.item_description}\n\n")
        item_prompt = (str(input("to pick up an item, type 'take' followed by the item name.\n\nTo continue, press [c]\n\n")))
        split_input = item_prompt.split(1)
        if item_prompt == "c":
            pass
        elif len(split_input) > 1:
            if split_input[1] in 
        else:
            pass


      
            