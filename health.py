from item import *


class Health(Item):
    def __init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb, hp_amount):
        Item.__init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb)
        
        self.hp_amount = hp_amount
        
    def use(self, player):
        player.hp += self.hp_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
