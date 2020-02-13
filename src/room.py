import textwrap

class Room:
    def __init__(self, room_name, room_description, room_items):
        self.room_name = room_name
        self.room_description = room_description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.room_items = []
    def __str__(self):
        return f"{'~' * 80}\n\n{self.room_name}\n{'=' * len(self.room_name)}\n\n{self.room_description}\n"


    
    
