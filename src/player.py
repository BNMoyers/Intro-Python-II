# Write a class to hold player information, e.g. what room they are in
# currently.

# imports

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("You run headfirst into a blank wall. Looks like you can't go that way.")

      
            