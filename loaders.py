import pygame
from enemy import * 
from weapon import *
from armor import *
from health import *
from resources import *

class Loaders:

    def __init__(self, resources, base_size):
        #WEAPONS
        self.sword1 = Weapon(4, 4, base_size, "Steel Long Sword", pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), True, 10, 's1', pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), 5, 0.10, 2, resources.S1_U, resources.S1_D, resources.S1_L, resources.S1_R)
        
        self.sword2 = Weapon(6, 6, base_size, "Rusty Short Sword", pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), True, 2, 's2', pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), 10, 0.20, 1, resources.S2_U, resources.S2_D, resources.S2_L, resources.S2_R)

        #ARMOR
        self.armorh1 = Armor(3, 4, base_size, "Cloth Head Armor", pygame.image.load('images/armor/h1/h1.png').convert_alpha(), True, 5, 'h1', pygame.image.load('images/armor/h1/h1.png').convert_alpha(), 5, 'h', resources.H1_U, resources.H1_D, resources.H1_L, resources.H1_R)
        
        self.armorc1 = Armor(3, 5, base_size, "Hard Chest Armor", pygame.image.load('images/armor/c1/c1.png').convert_alpha(), True, 10, 'c1', pygame.image.load('images/armor/c1/c1.png').convert_alpha(), 10, 'c', resources.C1_U, resources.C1_D, resources.C1_L, resources.C1_R)

        self.armorc2 = Armor(8, 5, base_size, "Soft Wizard Armor", pygame.image.load('images/armor/c2/c2.png').convert_alpha(), True, 7, 'c2', pygame.image.load('images/armor/c2/c2.png').convert_alpha(), 7, 'c', resources.C2_U, resources.C2_D, resources.C2_L, resources.C2_R)

        #ENEMIES
        self.skeleton1 = Enemy("Weak Skeleton", 10, 10, base_size, 100, 15, 10, 10, 13, 2, 5, 'd', 5, 10, 15, True, pygame.image.load('images/enemies/skeleton1.png').convert_alpha())
        self.skeleton1.up_img = resources.SKELETON1_U
        self.skeleton1.down_img = resources.SKELETON1_D
        self.skeleton1.left_img = resources.SKELETON1_L
        self.skeleton1.right_img = resources.SKELETON1_R
        
        self.skeleton2 = Enemy("Strong Skeleton", 10, 11, base_size, 300, 10, 12, 1, 3, 4, 4, 'u', 10, 30, 20, True, pygame.image.load('images/enemies/skeleton1.png').convert_alpha())
        self.skeleton2.up_img = resources.SKELETON1_U
        self.skeleton2.down_img = resources.SKELETON1_D
        self.skeleton2.left_img = resources.SKELETON1_L
        self.skeleton2.right_img = resources.SKELETON1_R

        
        #ITEMS
        #  HEALTH
        self.berries1 = Health(3, 3, base_size,"Berries1", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 10)
        
        self.berries2 = Health(2, 2, base_size,"Berries2", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 15)
        
        self.peach1 = Health(2, 6, base_size,"Juicy Peach", pygame.image.load('images/items/peach1.png').convert_alpha(), True, 2, 'p1', pygame.image.load('images/items/peach1_i.png').convert_alpha(), 1)
        