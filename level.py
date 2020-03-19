import pygame


class Level:

    def __init__(self, file_name, map_width, map_height, tile_size):
        self.DIRT = 0
        self.GRASS = 1
        self.WATER = 2
        self.COAL = 3
        self.ROCK = 4
        self.LAVA = 5
    
        self.file_name = file_name
        self.tilemap = [[None for w in range(map_width)] for h in range(map_height)]
        self.map_width = map_width
        self.map_height = map_height
        self.tile_size = tile_size
        
        self.items = []
        self.enemies = []

        self.textures = {
                0: (pygame.image.load('images/ground/dirt.png'), 1),
                1: (pygame.image.load('images/ground/grass.png'), 1),
                2: (pygame.image.load('images/ground/water.png'), 0),
                3: (pygame.image.load('images/ground/coal.png'), 0),
                4: (pygame.image.load('images/ground/rock.png'), 0),
                5: (pygame.image.load('images/ground/lava.png'), 0)
        } 
        
        self.resources = [self.DIRT, self.GRASS, self.WATER, self.COAL, self.ROCK, self.LAVA]
        
        i = 0
        j = 0
        f = open("levels/" + file_name, "r")    
        for l in f:
            for c in l:
                if c != '\n':
                    self.tilemap[i][j] = self.resources[int(c)]
                    j += 1
            i += 1
            j = 0
        
    def draw(self, surf):
        for row in range(self.map_height):
            for column in range(self.map_width):
                surf.blit(self.textures[self.tilemap[row][column]][0], (column*self.tile_size, row*self.tile_size, self.tile_size, self.tile_size))

    def is_tile_passable_tl(self, player):
        return self.textures[self.tilemap[player.y_pos-1][player.x_pos - 1]][1] == 1

    def is_tile_passable_tm(self, player):
        return self.textures[self.tilemap[player.y_pos-1][player.x_pos]][1] == 1

    def is_tile_passable_tr(self, player):
        return self.textures[self.tilemap[player.y_pos-1][player.x_pos + 1]][1] == 1

    def is_tile_passable_ml(self, player):
        return self.textures[self.tilemap[player.y_pos][player.x_pos - 1]][1] == 1

    def is_tile_passable_mm(self, player): #redundant
        return self.textures[self.tilemap[player.y_pos][player.x_pos]][1] == 1

    def is_tile_passable_mr(self, player):
        return self.textures[self.tilemap[player.y_pos][player.x_pos + 1]][1] == 1

    def is_tile_passable_bl(self, player):
        return self.textures[self.tilemap[player.y_pos + 1][player.x_pos-1]][1] == 1

    def is_tile_passable_bm(self, player):
        return self.textures[self.tilemap[player.y_pos+1][player.x_pos]][1] == 1

    def is_tile_passable_br(self, player):
        return self.textures[self.tilemap[player.y_pos + 1][player.x_pos+1]][1] == 1
