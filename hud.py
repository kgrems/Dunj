import pygame
from colors import *


class Hud:
    def __init__(self, player):
        self.player = player
        self.lower = pygame.image.load('images/misc/hud_lower.png').convert_alpha()
        self.move_indicator = pygame.image.load('images/misc/move_indicator.png').convert_alpha()
        self.height = 4
        self.left_padding = 25
        self.system_padding = 1186
        self.moves_padding = 938
        self.title_height = 40
        self.stat_c1_padding = self.left_padding + 60
        self.stat_c2_padding = self.stat_c1_padding + 180
        self.stat_gap = 18
             
        self.inv_padding = 329
        self.inv_spacing = 60
             
        self.weapon = self.left_padding + 160
        self.head = self.weapon + 220
        self.chest = self.head + 280
        self.legs = self.chest + 250
        self.spell1 = self.legs + 300
        self.spell2 = self.spell1 + 265
        
        self.title_text = pygame.font.Font('fonts/ARCADE.TTF', 48)
        self.player_name_surface = self.title_text.render(player.name, True, Colors.GREEN)
        self.data_text = pygame.font.Font('fonts/ARCADE.TTF', 20)
    
        self.system_message = '' 
        
    def draw(self, displaysurf, tilesize, mapheight):
        displaysurf.blit(self.lower, (0, mapheight * tilesize))
        displaysurf.blit(self.player_name_surface, (self.left_padding, mapheight*tilesize))
    
        self.system_surface = self.data_text.render(self.system_message, True, Colors.GREEN)
        
        self.stat_c1_hp_surface = self.data_text.render(str(self.player.hp), True, Colors.GREEN)
        self.stat_c1_mp_surface = self.data_text.render(str(self.player.mp), True, Colors.GREEN)
        self.stat_c1_lvl_surface = self.data_text.render(str(self.player.lvl), True, Colors.GREEN)
        self.stat_c1_xp_surface = self.data_text.render(str(self.player.xp), True, Colors.GREEN)
    
        self.stat_c2_str_surface = self.data_text.render(str(self.player.str), True, Colors.GREEN)
        self.stat_c2_mag_surface = self.data_text.render(str(self.player.mag), True, Colors.GREEN)
        self.stat_c2_gold_surface = self.data_text.render(str(self.player.gold), True, Colors.GREEN)
        self.stat_c2_def_surface = self.data_text.render(str(self.player.get_defense()), True, Colors.GREEN)
        
        displaysurf.blit(self.system_surface, (self.system_padding, mapheight*tilesize+self.title_height))
        
        displaysurf.blit(self.stat_c1_hp_surface, (self.stat_c1_padding, mapheight*tilesize+self.title_height))
        displaysurf.blit(self.stat_c1_mp_surface, (self.stat_c1_padding, mapheight*tilesize+self.title_height+self.stat_gap))
        displaysurf.blit(self.stat_c1_lvl_surface, (self.stat_c1_padding, mapheight*tilesize+self.title_height+self.stat_gap*2))
        displaysurf.blit(self.stat_c1_xp_surface, (self.stat_c1_padding, mapheight*tilesize+self.title_height+self.stat_gap*3))
        
        displaysurf.blit(self.stat_c2_str_surface, (self.stat_c2_padding, mapheight*tilesize+self.title_height))
        displaysurf.blit(self.stat_c2_def_surface, (self.stat_c2_padding, mapheight * tilesize + self.title_height + self.stat_gap))
        displaysurf.blit(self.stat_c2_mag_surface, (self.stat_c2_padding, mapheight*tilesize+self.title_height+self.stat_gap*2))
        displaysurf.blit(self.stat_c2_gold_surface, (self.stat_c2_padding, mapheight*tilesize+self.title_height + self.stat_gap*3))
    
        for i in range(self.player.moves):
            if i <= 4:
                displaysurf.blit(self.move_indicator, (self.moves_padding+i*tilesize, mapheight*tilesize+self.title_height))
                j = 0
            else:
                displaysurf.blit(self.move_indicator, (self.moves_padding+j*tilesize, (mapheight*tilesize+self.title_height) + self.move_indicator.get_height()+10))
                j += 1
        
        i = 0
        for item in self.player.inventory:
            displaysurf.blit(item.inventory_thumb, (self.inv_padding+(i*self.inv_spacing), mapheight*tilesize+self.title_height + 40))
            i += 1
            
        if self.player.weapon is not None:
            displaysurf.blit(self.player.weapon.base_image, (self.weapon, mapheight*tilesize+self.height*tilesize-tilesize))
    
        if self.player.armor_head is not None:
            displaysurf.blit(self.player.armor_head.base_image, (self.head, mapheight*tilesize+self.height*tilesize-tilesize))
    
        if self.player.armor_chest is not None:
            displaysurf.blit(self.player.armor_chest.base_image, (self.chest, mapheight*tilesize+self.height*tilesize-tilesize))
            
        if self.player.armor_legs is not None:
            displaysurf.blit(self.player.armor_legs.base_image, (self.legs, mapheight*tilesize+self.height*tilesize-tilesize))
    
        if self.player.spell1 is not None:
            displaysurf.blit(self.player.spell1.base_image, (self.spell1, mapheight*tilesize+self.height*tilesize-tilesize))
    
        if self.player.spell2 is not None:
            displaysurf.blit(self.player.spell2.base_image, (self.spell2, mapheight*tilesize+self.height*tilesize-tilesize))

