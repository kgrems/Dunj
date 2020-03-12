from actor import *


class Player(Actor):
    def __init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, xp, moves, direction, max_moves, max_hp, lvl, visible):
        Actor.__init__(self, name, x_pos, y_pos, size, hp, mp, str, defense, mag, gold, moves, direction, max_moves, max_hp, visible)

        self.lvl = lvl

        self.xp = xp

        self.weapon = None
        self.armor_head = None
        self.armor_chest = None
        self.armor_legs = None
        
        self.spell1 = None
        self.spell2 = None
        
        # did player drop an item on the tile that they're standing on?
        self.item_dropped = False

        self.current_attack_move_distance = 0
        self.max_attack_move_distance = 2
        # setting to decimal helps smooth the animation since its * by tilesize in the draw function
        self.attack_move_speed = 0.5
        self.attacking_forward = True
        self.attacking = False

        self.tile_attack_direction = ''

    def draw_self(self, surf, tilesize):
        pos = (self.x_pos*tilesize, self.y_pos*tilesize)
        if self.direction == 'd':
            surf.blit(self.down_img, pos)
            if self.armor_head is not None:
                surf.blit(self.armor_head.d_img, pos)
            if self.armor_chest is not None:
                surf.blit(self.armor_chest.d_img, pos)
            if self.armor_legs is not None:
                surf.blit(self.armor_legs.d_img, pos)
            if self.weapon is not None:
                surf.blit(self.weapon.d_img,pos)
        elif self.direction == 'l':
            surf.blit(self.left_img,pos)
            if self.armor_head is not None:
                surf.blit(self.armor_head.l_img,pos)
            if self.armor_chest is not None:
                surf.blit(self.armor_chest.l_img, pos)
            if self.armor_legs is not None:
                surf.blit(self.armor_legs.l_img, pos)
            if self.weapon is not None:
                surf.blit(self.weapon.l_img,pos)
        elif self.direction == 'r':
            surf.blit(self.right_img,pos)
            if self.armor_head is not None:
                surf.blit(self.armor_head.r_img,pos)
            if self.armor_chest is not None:
                surf.blit(self.armor_chest.r_img, pos)
            if self.armor_legs is not None:
                surf.blit(self.armor_legs.r_img, pos)
            if self.weapon is not None:
                surf.blit(self.weapon.r_img,pos)
        elif self.direction == 'u':
            surf.blit(self.up_img,pos)
            if self.armor_head is not None:
                surf.blit(self.armor_head.u_img,pos)
            if self.armor_chest is not None:
                surf.blit(self.armor_chest.u_img, pos)
            if self.armor_legs is not None:
                surf.blit(self.armor_legs.u_img, pos)
            if self.weapon is not None:
                surf.blit(self.weapon.u_img,pos)

    def get_defense(self):
        result = 0
        if self.armor_legs is not None:
            result += self.armor_legs.defense
        if self.armor_head is not None:
            result += self.armor_head.defense
        if self.armor_chest is not None:
            result += self.armor_chest.defense

        return result

    def drop_weapon(self):
        if self.direction == 'u':
            self.weapon.x_pos = self.x_pos
            self.weapon.y_pos = self.y_pos + 1
        elif self.direction == 'd':
            self.weapon.x_pos = self.x_pos
            self.weapon.y_pos = self.y_pos - 1
        elif self.direction == 'l':
            self.weapon.x_pos = self.x_pos + 1
            self.weapon.y_pos = self.y_pos
        elif self.direction == 'r':
            self.weapon.x_pos = self.x_pos - 1
            self.weapon.y_pos = self.y_pos

    '''def attack(event):
        if event.key == K_RIGHT and tile_highlight_active_x + 1 < player.x_pos + 2:
            tile_highlight_active_x += 1
        elif event.key == K_LEFT and tile_highlight_active_x - 1 > player.x_pos - 2:
            tile_highlight_active_x -= 1
        elif event.key == K_UP and tile_highlight_active_y - 1 > player.y_pos - 2:
            tile_highlight_active_y -= 1
        elif event.key == K_DOWN and tile_highlight_active_y + 1 < player.y_pos + 2:
            tile_highlight_active_y += 1
        elif event.key == K_SPACE:
            if tile_highlight_active_x == player.x_pos - 1 and tile_highlight_active_y == player.y_pos - 1:
                tile_attack_direction = 'ul'
            if tile_highlight_active_x == player.x_pos and tile_highlight_active_y == player.y_pos - 1:
                tile_attack_direction = 'um'
            if tile_highlight_active_x == player.x_pos + 1 and tile_highlight_active_y == player.y_pos - 1:
                tile_attack_direction = 'ur'
            if tile_highlight_active_x == player.x_pos - 1 and tile_highlight_active_y == player.y_pos:
                tile_attack_direction = 'ml'
            if tile_highlight_active_x == player.x_pos and tile_highlight_active_y == player.y_pos:
                tile_attack_direction = 'mm'
            if tile_highlight_active_x == player.x_pos + 1 and tile_highlight_active_y == player.y_pos:
                tile_attack_direction = 'mr'
            if tile_highlight_active_x == player.x_pos - 1 and tile_highlight_active_y == player.y_pos + 1:
                tile_attack_direction = 'bl'
            if tile_highlight_active_x == player.x_pos and tile_highlight_active_y == player.y_pos + 1:
                tile_attack_direction = 'bm'
            if tile_highlight_active_x == player.x_pos + 1 and tile_highlight_active_y == player.y_pos + 1:
                tile_attack_direction = 'br'
    '''
    # need to rework this.  perhaps pass in a tuple (x,y) with the destination coords to make it more flexible for
    #   longer/shorter attacks?
    def attack_animation(self, tile_attack_direction):
        if self.attacking:
            if self.attacking_forward:
                if tile_attack_direction == 'ul':
                    self.x_pos -= self.attack_move_speed
                    self.y_pos -= self.attack_move_speed
                elif tile_attack_direction == 'um':
                    self.direction = 'u'
                    self.y_pos -= self.attack_move_speed
                elif tile_attack_direction == 'ur':
                    self.x_pos += self.attack_move_speed
                    self.y_pos -= self.attack_move_speed
                elif tile_attack_direction == 'ml':
                    self.direction = 'l'
                    self.x_pos -= self.attack_move_speed
                elif tile_attack_direction == 'mm':
                    print('dunno what to do here')
                elif tile_attack_direction == 'mr':
                    self.direction = 'r'
                    self.x_pos += self.attack_move_speed
                elif tile_attack_direction == 'bl':
                    self.x_pos -= self.attack_move_speed
                    self.y_pos += self.attack_move_speed
                elif tile_attack_direction == 'bm':
                    self.direction = 'd'
                    self.y_pos += self.attack_move_speed
                elif tile_attack_direction == 'br':
                    self.x_pos += self.attack_move_speed
                    self.y_pos += self.attack_move_speed

                self.current_attack_move_distance += 1

                if self.current_attack_move_distance == self.max_attack_move_distance:
                    self.attacking_forward = False
            else:
                if tile_attack_direction == 'ul':
                    self.x_pos += self.attack_move_speed
                    self.y_pos += self.attack_move_speed
                elif tile_attack_direction == 'um':
                    self.direction = 'u'
                    self.y_pos += self.attack_move_speed
                elif tile_attack_direction == 'ur':
                    self.x_pos -= self.attack_move_speed
                    self.y_pos += self.attack_move_speed
                elif tile_attack_direction == 'ml':
                    self.direction = 'l'
                    self.x_pos += self.attack_move_speed
                elif tile_attack_direction == 'mm':
                    print('dunno what to do here')
                elif tile_attack_direction == 'mr':
                    self.direction = 'r'
                    self.x_pos -= self.attack_move_speed
                elif tile_attack_direction == 'bl':
                    self.x_pos += self.attack_move_speed
                    self.y_pos -= self.attack_move_speed
                elif tile_attack_direction == 'bm':
                    self.direction = 'd'
                    self.y_pos -= self.attack_move_speed
                elif tile_attack_direction == 'br':
                    self.x_pos -= self.attack_move_speed
                    self.y_pos -= self.attack_move_speed

                self.current_attack_move_distance -= 1

                if self.current_attack_move_distance == 0:
                    self.attacking = False
                    self.attacking_forward = True

