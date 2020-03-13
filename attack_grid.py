from pygame.locals import *


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