import pygame


class Level:

    def __init__(self, file_name, MAPWIDTH, MAPHEIGHT, TILESIZE):
        self.DIRT = 0
        self.GRASS = 1
        self.WATER = 2
        self.COAL = 3
        self.ROCK = 4
        self.LAVA = 5
    
        self.file_name = file_name
        self.tilemap = [[None for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
        self.map_width = MAPWIDTH
        self.map_height = MAPHEIGHT
        self.tile_size = TILESIZE
        
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
        
    def draw_self(self, DISPLAYSURF):
        for row in range(self.map_height):
            for column in range(self.map_width):
                DISPLAYSURF.blit(self.textures[self.tilemap[row][column]][0], (column*self.tile_size, row*self.tile_size, self.tile_size, self.tile_size))

    def is_tile_passable_left(self, player):
        return self.textures[self.tilemap[player.y_pos][player.x_pos - 1]][1] == 1
    def is_tile_passable_right(self, player):
        return self.textures[self.tilemap[player.y_pos][player.x_pos + 1]][1] == 1
    def is_tile_passable_up(self, player):
        return self.textures[self.tilemap[player.y_pos - 1][player.x_pos]][1] == 1
    def is_tile_passable_down(self, player):
        return self.textures[self.tilemap[player.y_pos + 1][player.x_pos]][1] == 1