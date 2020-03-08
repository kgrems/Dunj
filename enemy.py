from actor import *


class Enemy(Actor):
    def __init__(self, name, x_pos, y_pos, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp,
                 xp_give, visible):
        Actor.__init__(self, name, x_pos, y_pos, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp,
                       visible)

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

    def draw_self(self, surf, tilesize):
        if self.direction == 'd':
            surf.blit(self.down_img, (self.x_pos*tilesize, self.y_pos*tilesize))
        elif self.direction == 'l':
            surf.blit(self.left_img, (self.x_pos*tilesize, self.y_pos*tilesize))
        elif self.direction == 'r':
            surf.blit(self.right_img, (self.x_pos*tilesize, self.y_pos*tilesize))
        elif self.direction == 'u':
            surf.blit(self.up_img, (self.x_pos*tilesize, self.y_pos*tilesize))
