from pygame.locals import *
import pygame
from enums.direction_types import DirectionTypes


class AttackGrid:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.tile_highlight_active_x = 0
        self.tile_highlight_active_y = 0
        self.tile_attack_direction = DirectionTypes.MID_MID

        self.tl_pos = (0, 0)
        self.tm_pos = (0, 0)
        self.tr_pos = (0, 0)
        self.ml_pos = (0, 0)
        self.mm_pos = (0, 0)
        self.mr_pos = (0, 0)
        self.bl_pos = (0, 0)
        self.bm_pos = (0, 0)
        self.br_pos = (0, 0)

        self.tl_active = False
        self.tm_active = False
        self.tr_active = False
        self.ml_active = False
        self.mm_active = False
        self.mr_active = False
        self.bl_active = False
        self.bm_active = False
        self.br_active = False

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
                self.tile_attack_direction = DirectionTypes.TOP_LEFT
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos - 1:
                self.tile_attack_direction = DirectionTypes.TOP_MID
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos - 1:
                self.tile_attack_direction = DirectionTypes.TOP_RIGHT
            if self.tile_highlight_active_x == player.x_pos - 1 and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = DirectionTypes.MID_LEFT
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = DirectionTypes.MID_MID
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos:
                self.tile_attack_direction = DirectionTypes.MID_RIGHT
            if self.tile_highlight_active_x == player.x_pos - 1 and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = DirectionTypes.BOT_LEFT
            if self.tile_highlight_active_x == player.x_pos and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = DirectionTypes.BOT_MID
            if self.tile_highlight_active_x == player.x_pos + 1 and self.tile_highlight_active_y == player.y_pos + 1:
                self.tile_attack_direction = DirectionTypes.BOT_RIGHT

            game_controller.action_key_pressed = True
            player.attacking = True
            game_controller.deal_damage = True

    def place(self, player, tile_size, level):
        self.tl_pos = ((player.x_pos - 1) * tile_size, (player.y_pos - 1) * tile_size)
        self.tm_pos = (player.x_pos * tile_size, (player.y_pos - 1) * tile_size)
        self.tr_pos = ((player.x_pos + 1) * tile_size, (player.y_pos - 1) * tile_size)
        self.ml_pos = ((player.x_pos - 1) * tile_size, player.y_pos * tile_size)
        self.mm_pos = (player.x_pos * tile_size, player.y_pos * tile_size)
        self.mr_pos = ((player.x_pos + 1) * tile_size, player.y_pos * tile_size)
        self.bl_pos = ((player.x_pos - 1) * tile_size, (player.y_pos + 1) * tile_size)
        self.bm_pos = (player.x_pos * tile_size, (player.y_pos + 1) * tile_size)
        self.br_pos = ((player.x_pos + 1) * tile_size, (player.y_pos + 1) * tile_size)
        self.check_tiles_active(level, player)

    def draw(self, surf, tile_size):
        if self.tl_active:
            surf.blit(self.tile_highlight, self.tl_pos)
        if self.tm_active:
            surf.blit(self.tile_highlight, self.tm_pos)
        if self.tr_active:
            surf.blit(self.tile_highlight, self.tr_pos)
        if self.ml_active:
            surf.blit(self.tile_highlight, self.ml_pos)
        if self.mm_active:
            surf.blit(self.tile_highlight, self.mm_pos)
        if self.mr_active:
            surf.blit(self.tile_highlight, self.mr_pos)
        if self.bl_active:
            surf.blit(self.tile_highlight, self.bl_pos)
        if self.bm_active:
            surf.blit(self.tile_highlight, self.bm_pos)
        if self.br_active:
            surf.blit(self.tile_highlight, self.br_pos)
        surf.blit(self.tile_highlight_active,
                  (self.tile_highlight_active_x * tile_size, self.tile_highlight_active_y * tile_size))

    def check_tiles_active(self, level, player):
        if level.is_tile_passable_tl(player):
            self.tl_active = True
        if level.is_tile_passable_tm(player):
            self.tm_active = True
        if level.is_tile_passable_tr(player):
            self.tr_active = True
        if level.is_tile_passable_ml(player):
            self.ml_active = True
        if level.is_tile_passable_mm(player):
            self.mm_active = True
        if level.is_tile_passable_mr(player):
            self.mr_active = True
        if level.is_tile_passable_bl(player):
            self.bl_active = True
        if level.is_tile_passable_bm(player):
            self.bm_active = True
        if level.is_tile_passable_br(player):
            self.br_active = True
