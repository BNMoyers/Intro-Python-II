# Write a class to hold player information, e.g. what room they are in
# currently.

# imports
from room import Room

class Player(Room): 
    def __init__(self,room_name):
        super().__init__(room_name)
            