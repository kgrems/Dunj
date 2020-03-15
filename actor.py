import pygame
from display_object import *


class Actor(DisplayObject):

    def __init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp, visible, image_path):
        DisplayObject.__init__(self, name, x_pos, y_pos, size, visible, image_path)

        self.str = str
        self.defense = defense
        self.hp = hp
        self.mp = mp
        self.mag = mag
        self.gold = gold
        self.inventory = []
        self.up_img = None
        self.down_img = None
        self.left_img = None
        self.right_img = None
        self.direction = direction
        self.moves = moves
        self.max_moves = max_moves
        self.max_hp = max_hp
