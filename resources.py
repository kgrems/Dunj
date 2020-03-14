import pygame

class Resources:
    def __init__(self):
        #WEAPONS
        self.S1_U = pygame.image.load('images/weapons/s1/u.png').convert_alpha()
        self.S1_D = pygame.image.load('images/weapons/s1/d.png').convert_alpha()
        self.S1_L = pygame.image.load('images/weapons/s1/l.png').convert_alpha()
        self.S1_R = pygame.image.load('images/weapons/s1/r.png').convert_alpha()
        
        self.S2_U = pygame.image.load('images/weapons/s2/s2_u.png').convert_alpha()
        self.S2_D = pygame.image.load('images/weapons/s2/s2_d.png').convert_alpha()
        self.S2_L = pygame.image.load('images/weapons/s2/s2_l.png').convert_alpha()
        self.S2_R = pygame.image.load('images/weapons/s2/s2_r.png').convert_alpha()
        
        #ARMOR
        self.H1_U = pygame.image.load('images/armor/h1/h1_u.png').convert_alpha()
        self.H1_D = pygame.image.load('images/armor/h1/h1_d.png').convert_alpha()
        self.H1_L = pygame.image.load('images/armor/h1/h1_l.png').convert_alpha()
        self.H1_R = pygame.image.load('images/armor/h1/h1_r.png').convert_alpha()
        
        self.C1_U = pygame.image.load('images/armor/c1/c1_u.png').convert_alpha()
        self.C1_D = pygame.image.load('images/armor/c1/c1_d.png').convert_alpha()
        self.C1_L = pygame.image.load('images/armor/c1/c1_l.png').convert_alpha()
        self.C1_R = pygame.image.load('images/armor/c1/c1_r.png').convert_alpha()

        self.C2_U = pygame.image.load('images/armor/c2/c2_u.png').convert_alpha()
        self.C2_D = pygame.image.load('images/armor/c2/c2_d.png').convert_alpha()
        self.C2_L = pygame.image.load('images/armor/c2/c2_l.png').convert_alpha()
        self.C2_R = pygame.image.load('images/armor/c2/c2_r.png').convert_alpha()

        #PLAYER
        self.PLAYER_B_U = pygame.image.load('images/player/base/player_u.png').convert_alpha()
        self.PLAYER_B_D = pygame.image.load('images/player/base/player_d.png').convert_alpha()
        self.PLAYER_B_L = pygame.image.load('images/player/base/player_l.png').convert_alpha()
        self.PLAYER_B_R = pygame.image.load('images/player/base/player_r.png').convert_alpha()
        
        #ENEMIES
        self.SKELETON1_U = pygame.image.load('images/enemies/skeleton1_u.png').convert_alpha()
        self.SKELETON1_D = pygame.image.load('images/enemies/skeleton1_d.png').convert_alpha()
        self.SKELETON1_L = pygame.image.load('images/enemies/skeleton1_l.png').convert_alpha()
        self.SKELETON1_R = pygame.image.load('images/enemies/skeleton1_r.png').convert_alpha()

        #MISC
        TILE_HIGHLIGHT = pygame.image.load('images/ground/highlight.png').convert_alpha()
        TILE_HIGHLIGHT_ACTIVE = pygame.image.load('images/ground/highlight_active.png').convert_alpha()