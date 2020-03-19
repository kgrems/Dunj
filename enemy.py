from actor import *
from enums import MovementType

class Enemy(Actor):
    def __init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp,
                 xp_give, visible, image_path, movement_type):
        Actor.__init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp,
                       visible, image_path)

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name

        self.mag = mag
        self.moves = moves
        self.max_moves = max_moves
        self.str = str
        self.hp = hp
        self.xp_give = xp_give

        self.up_img = None
        self.down_img = None
        self.left_img = None
        self.right_img = None

        self.movement_type = movement_type

    def draw(self, surf):
        if self.direction == 'd':
            self.base_image = self.down_img
        elif self.direction == 'l':
            self.base_image = self.left_img
        elif self.direction == 'r':
            self.base_image = self.right_img
        elif self.direction == 'u':
            self.base_image = self.up_img
        DisplayObject.draw(self, surf)

    '''def move(self):
        if self.movement_type == MovementType.RANDOM:'''
