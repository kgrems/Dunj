from display_object import *


class Item(DisplayObject):
    def __init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb):
        DisplayObject.__init__(self, name, x_pos, y_pos, size, visible, image_path)

        self.cost = cost
        self.data_symbol = data_symbol
        self.inventory_thumb = inventory_thumb
    
    def use(self, player):
        print(player.name + ' used and item!')
