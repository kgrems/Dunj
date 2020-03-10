import pygame
from colors import *


class Actor(pygame.sprite.Sprite):

    def __init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp, visible):
    
        #not using Sprite yet, but could be useful later
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([size,size])
        self.image.fill(Colors.RED)
        
        self.rect = self.image.get_rect()
        
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
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
        self.visible = visible