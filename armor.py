from item import *


class Armor(Item):
    def __init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb, defense,
                 armor_type, u_img, d_img, l_img, r_img):
        Item.__init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb)

        self.defense = defense
        # valid types are 'h' 'c' 'l'
        self.armor_type = armor_type

        self.u_img = u_img
        self.d_img = d_img
        self.l_img = l_img
        self.r_img = r_img
