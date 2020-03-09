import pygame
from weapon import *
from armor import *
from health import *
from resources import *

class Loaders:

    def __init__(self, resources):
        self.sword1 = Weapon(4, 4, "Steel Long Sword", pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), True, 10, 's1', pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), 5, 0.10, 2, resources.S1_U, resources.S1_D, resources.S1_L, resources.S1_R)
        
        self.sword2 = Weapon(6, 6, "Rusty Short Sword", pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), True, 2, 's2', pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), 10, 0.20, 1, resources.S2_U, resources.S2_D, resources.S2_L, resources.S2_R)
        
        self.armorh1 = Armor(3, 4, "Cloth Head Armor", pygame.image.load('images/armor/h1/h1.png').convert_alpha(), True, 5, 'h1', pygame.image.load('images/armor/h1/h1.png').convert_alpha(), 5, 'h', resources.H1_U, resources.H1_D, resources.H1_L, resources.H1_R)
        
        self.armorc1 = Armor(3, 5, "Hard Chest Armor", pygame.image.load('images/armor/c1/c1.png').convert_alpha(), True, 10, 'c1', pygame.image.load('images/armor/c1/c1.png').convert_alpha(), 10, 'c', resources.C1_U, resources.C1_D, resources.C1_L, resources.C1_R)
        
        self.berries1 = Health(3, 3, "Berries1", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 10)
        
        self.berries2 = Health(2, 2, "Berries2", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 15)
        
        self.peach1 = Health(2, 6, "Juicy Peach", pygame.image.load('images/items/peach1.png').convert_alpha(), True, 2, 'p1', pygame.image.load('images/items/peach1_i.png').convert_alpha(), 1)
        