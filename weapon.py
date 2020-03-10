from item import *


class Weapon(Item):
    def __init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb, damage,
                 attack_variance, weapon_range, u_img, d_img, l_img, r_img):
        Item.__init__(self, x_pos, y_pos, size, name, image_path, visible, cost, data_symbol, inventory_thumb)
        
        self.damage = damage
        self.weapon_range = weapon_range

        # damage modifier (as decimal) + or - based on damage property
        self.attack_variance = attack_variance

        self.u_img = u_img
        self.d_img = d_img
        self.l_img = l_img
        self.r_img = r_img

    def use(self, player):
        print('attack!')
