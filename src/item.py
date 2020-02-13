# * Create a file called `item.py` and add an `Item` class in there.

#   * This will be the _base class_ for specialized item types to be declared
#     later.

class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
