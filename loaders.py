'''import pygame
from weapon import *

class Loaders:
    pygame.init()
    
    sword1 = Weapon(4, 4, "Steel Long Sword", pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), True, 10, 's1', pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), 5, 0.10, 2, S1_U, S1_D, S1_L, S1_R)
    
    sword2 = Weapon(6, 6, "Rusty Short Sword", pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), True, 2, 's2', pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), 10, 0.20, 1, S2_U, S2_D, S2_L, S2_R)
    

    armorh1 = Armor(3, 4, "Cloth Head Armor", pygame.image.load('images/armor/h1/h1.png').convert_alpha(), True, 5, 'h1', pygame.image.load('images/armor/h1/h1.png').convert_alpha(), 5, 'h', H1_U, H1_D, H1_L, H1_R)
    
    armorc1 = Armor(3, 5, "Hard Chest Armor", pygame.image.load('images/armor/c1/c1.png').convert_alpha(), True, 10, 'c1', pygame.image.load('images/armor/c1/c1.png').convert_alpha(), 10, 'c', C1_U, C1_D, C1_L, C1_R)
      
    berries1 = Health(3, 3, "Berries1", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 10)
    
    berries2 = Health(2, 2, "Berries2", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@', pygame.image.load('images/items/berries1_i.png').convert_alpha(), 15)
    
    peach1 = Health(2, 6, "Juicy Peach", pygame.image.load('images/items/peach1.png').convert_alpha(), True, 2, 'p1', pygame.image.load('images/items/peach1_i.png').convert_alpha(), 1)
    