from pygame.locals import *
import pygame


class AttackGrid:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.tile_highlight_active_x = 0
        self.tile_highlight_active_y = 0
        self.tile_attack_direction = ''

        self.tl = (0, 0)
        self.tm = (0, 0)
        self.tr = (0, 0)
        self.ml = (0, 0)
        self.mm = (0, 0)
        self.mr = (0, 0)
        self.bl = (0, 0)
        self.bm = (0, 0)
        self.br = (0, 0)

        self.tile_highlight = pygame.image.load('images/ground/highlight.png').convert_alpha()
        self.tile_highlight_active = pygame.image.load('images/ground/highlight_active.png').convert_alpha()

    def update(self, event, player, game_controller):
        if event.key == K_RIGHT and self.tile_highlight_active_x + 1 < player.x_pos + 2:
            self.tile_highlight_active_x += 1
        elif event.key == K_LEFT and self.tile_highlight_active_x - 1 > player.x_pos - 2:
            self.tile_highlight_active_x -= 1
        elif event.key == K_UP and self.tile_highlight_active_y - 1 > player.y_pos - 2:
            self.tile_highlight_active_y -= 1
        elif event.key == K_DOWN and self.tile_highlight_active_y + 1 < player.y_pos + 2:
            self.tile_highlight_active_y += 1
        elif event.key == K_SPACE:
            if self.tile_highlight_active_x == player.x_pos - 1 and self.tile_highlight_active_y == player.y_pos - 1:
                self.tile_attack_direction = 'ul'
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos - 1:
                self.tile_attack_direction = 'um'
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos - 1:
                self.tile_attack_direction = 'ur'
            if self.tile_highlight_active_x == player.x_pos - 1 and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = 'ml'
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = 'mm'
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = 'mr'
            if self.tile_highlight_active_x == player.x_pos - 1 and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = 'bl'
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = 'bm'
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = 'br'

            game_controller.action_key_pressed = True
            player.attacking = True
            game_controller.deal_damage = True

    def place(self, player, tile_size):
        self.tl = ((player.x_pos - 1) * tile_size, (player.y_pos - 1) * tile_size)
        self.tm = (player.x_pos * tile_size, (player.y_pos - 1) * tile_size)
        self.tr = ((player.x_pos + 1) * tile_size, (player.y_pos - 1) * tile_size)
        self.ml = ((player.x_pos - 1) * tile_size, player.y_pos * tile_size)
        self.mm = (player.x_pos * tile_size, player.y_pos * tile_size)
        self.mr = ((player.x_pos + 1) * tile_size, player.y_pos * tile_size)
        self.bl = ((player.x_pos - 1) * tile_size, (player.y_pos + 1) * tile_size)
        self.bm = (player.x_pos * tile_size, (player.y_pos + 1) * tile_size)
        self.br = ((player.x_pos + 1) * tile_size, (player.y_pos + 1) * tile_size)
        
    def draw(self, surf, tile_size):
        surf.blit(self.tile_highlight, self.tl)
        surf.blit(self.tile_highlight, self.tm)
        surf.blit(self.tile_highlight, self.tr)
        surf.blit(self.tile_highlight, self.ml)
        surf.blit(self.tile_highlight, self.mm)
        surf.blit(self.tile_highlight, self.mr)
        surf.blit(self.tile_highlight, self.bl)
        surf.blit(self.tile_highlight, self.bm)
        surf.blit(self.tile_highlight, self.br)
        surf.blit(self.tile_highlight_active, (self.tile_highlight_active_x * tile_size, self.tile_highlight_active_y * tile_size))
