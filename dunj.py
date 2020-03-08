#http://usingpython.com/events/
import pygame, sys, random, time, types, math
from enum import Enum

from health import *
from weapon import *
from player import *
from level import *
from armor import *
from enemy import *

from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

sound_enabled = False
ai_delay = False
input_lock = False
attack_mode = False
attack_variance_increase = False
proj_x = 0
proj_y = 0

BLACK = (0,   0,   0)
BROWN = (153, 76,  0)
GREEN = (0,   255, 0)
BLUE = (0,   0,   255)
GREY = (100, 100, 100)
RED = (255, 0,   0)


class GameState(Enum):
    MOVE = 1
    ATTACK = 2
    HELP = 3


TILESIZE = 40
MAPWIDTH = 40
MAPHEIGHT = 18

HUD_HEIGHT = 4

HELP_X = 120
HELP_Y = 84

FPS = 30
fpsClock = pygame.time.Clock()

VEL = 1

show_help = False
player_turn = True
collect_sound = pygame.mixer.Sound("sounds/collect_coin_01.wav")
actionKeyPressed = False

level1 = Level("1.lvl", MAPWIDTH, MAPHEIGHT, TILESIZE)

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + HUD_HEIGHT*TILESIZE))
FAVICON = pygame.image.load('images/misc/favicon.png').convert_alpha()

pygame.display.set_icon(FAVICON)

pygame.display.set_caption('Dunj')

PLEASE_WAIT = pygame.image.load('images/misc/please_wait.png').convert_alpha()
MOVE_INDICATOR = pygame.image.load('images/misc/move_indicator.png').convert_alpha()
HELP_SCREEN = pygame.image.load('images/misc/help.png').convert_alpha()
TILE_HIGHLIGHT = pygame.image.load('images/ground/highlight.png').convert_alpha()
TILE_HIGHLIGHT_ACTIVE = pygame.image.load('images/ground/highlight_active.png').convert_alpha()

tile_highlight_active_x = 0
tile_highlight_active_y = 0
tile_attack_direction = ''

attack_grid_tl = (0, 0)
attack_grid_tm = (0, 0)
attack_grid_tr = (0, 0)
attack_grid_ml = (0, 0)
attack_grid_mm = (0, 0)
attack_grid_mr = (0, 0)
attack_grid_bl = (0, 0)
attack_grid_bm = (0, 0)
attack_grid_br = (0, 0)

HUD_LOWER = pygame.image.load('images/misc/hud_lower.png').convert_alpha()
HUD_LEFT_PADDING = 25
HUD_SYSTEM_PADDING = 1186
HUD_MOVES_PADDING = 938
HUD_TITLE_HEIGHT = 40
HUD_STAT_C1_PADDING = HUD_LEFT_PADDING + 60
HUD_STAT_C2_PADDING = HUD_STAT_C1_PADDING + 180
HUD_STAT_GAP = 18

HUD_INV_PADDING = 329
HUD_INV_SPACING = 60

HUD_WEAPON = HUD_LEFT_PADDING + 160
HUD_HEAD = HUD_WEAPON + 220
HUD_CHEST = HUD_HEAD + 280
HUD_LEGS = HUD_CHEST + 250
HUD_SPELL1 = HUD_LEGS + 300
HUD_SPELL2 = HUD_SPELL1 + 265

PLAYER_B_U = pygame.image.load('images/player/base/player_u.png').convert_alpha()
PLAYER_B_D = pygame.image.load('images/player/base/player_d.png').convert_alpha()
PLAYER_B_L = pygame.image.load('images/player/base/player_l.png').convert_alpha()
PLAYER_B_R = pygame.image.load('images/player/base/player_r.png').convert_alpha()

SKELETON1_U = pygame.image.load('images/enemies/skeleton1_u.png').convert_alpha()
SKELETON1_D = pygame.image.load('images/enemies/skeleton1_d.png').convert_alpha()
SKELETON1_L = pygame.image.load('images/enemies/skeleton1_l.png').convert_alpha()
SKELETON1_R = pygame.image.load('images/enemies/skeleton1_r.png').convert_alpha()

S1_U = pygame.image.load('images/weapons/s1/u.png').convert_alpha()
S1_D = pygame.image.load('images/weapons/s1/d.png').convert_alpha()
S1_L = pygame.image.load('images/weapons/s1/l.png').convert_alpha()
S1_R = pygame.image.load('images/weapons/s1/r.png').convert_alpha()

S2_U = pygame.image.load('images/weapons/s2/s2_u.png').convert_alpha()
S2_D = pygame.image.load('images/weapons/s2/s2_d.png').convert_alpha()
S2_L = pygame.image.load('images/weapons/s2/s2_l.png').convert_alpha()
S2_R = pygame.image.load('images/weapons/s2/s2_r.png').convert_alpha()

H1_U = pygame.image.load('images/armor/h1/h1_u.png').convert_alpha()
H1_D = pygame.image.load('images/armor/h1/h1_d.png').convert_alpha()
H1_L = pygame.image.load('images/armor/h1/h1_l.png').convert_alpha()
H1_R = pygame.image.load('images/armor/h1/h1_r.png').convert_alpha()

C1_U = pygame.image.load('images/armor/c1/c1_u.png').convert_alpha()
C1_D = pygame.image.load('images/armor/c1/c1_d.png').convert_alpha()
C1_L = pygame.image.load('images/armor/c1/c1_l.png').convert_alpha()
C1_R = pygame.image.load('images/armor/c1/c1_r.png').convert_alpha()

skeleton1 = Enemy("Weak Skeleton", 10, 10, 100, 15, 10, 10, 13, 2, 5, 'd', 5, 10, 15, True)
skeleton1.up_img = SKELETON1_U
skeleton1.down_img = SKELETON1_D
skeleton1.left_img = SKELETON1_L
skeleton1.right_img = SKELETON1_R

skeleton2 = Enemy("Strong Skeleton", 10, 11, 300, 10, 12, 1, 3, 4, 4, 'u', 10, 30, 20, True)
skeleton2.up_img = SKELETON1_U
skeleton2.down_img = SKELETON1_D
skeleton2.left_img = SKELETON1_L
skeleton2.right_img = SKELETON1_R


player = Player("Kevin", 1, 1, 78, 34, 20, 22, 5, 10, 0, 7, 'd', 7, 100, 1, True)
player.up_img = PLAYER_B_U
player.down_img = PLAYER_B_D
player.left_img = PLAYER_B_L
player.right_img = PLAYER_B_R

PLAYER_U = PLAYER_B_U       
PLAYER_D = PLAYER_B_D
PLAYER_L = PLAYER_B_L
PLAYER_R = PLAYER_B_R

sword1 = Weapon(4, 4, "Steel Long Sword", pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), True, 10,
                's1', pygame.image.load('images/weapons/s1/s1.png').convert_alpha(), 5, 0.10, 2, S1_U, S1_D, S1_L, S1_R)
sword2 = Weapon(6, 6, "Rusty Short Sword", pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), True, 2,
                's2', pygame.image.load('images/weapons/s2/s2.png').convert_alpha(), 10, 0.20, 1, S2_U, S2_D, S2_L, S2_R)
berries1 = Health(3, 3, "Berries1", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@',
                  pygame.image.load('images/items/berries1_i.png').convert_alpha(), 10)
berries2 = Health(2, 2, "Berries2", pygame.image.load('images/items/berries1.png').convert_alpha(), True, 2, '@',
                  pygame.image.load('images/items/berries1_i.png').convert_alpha(), 15)
peach1 = Health(2, 6, "Juicy Peach", pygame.image.load('images/items/peach1.png').convert_alpha(), True, 2, 'p1',
                pygame.image.load('images/items/peach1_i.png').convert_alpha(), 1)
armorh1 = Armor(3, 4, "Cloth Head Armor", pygame.image.load('images/armor/h1/h1.png').convert_alpha(), True, 5, 'h1',
                pygame.image.load('images/armor/h1/h1.png').convert_alpha(), 5, 'h', H1_U, H1_D, H1_L, H1_R)
armorc1 = Armor(3, 5, "Hard Chest Armor", pygame.image.load('images/armor/c1/c1.png').convert_alpha(), True, 10, 'c1',
                pygame.image.load('images/armor/c1/c1.png').convert_alpha(), 10, 'c', C1_U, C1_D, C1_L, C1_R)

level1.items.append(sword1)
level1.items.append(sword2)
level1.items.append(berries1)
level1.items.append(berries2)
level1.items.append(peach1)
level1.items.append(armorh1)
level1.items.append(armorc1)

level1.enemies.append(skeleton1)
level1.enemies.append(skeleton2)

hud_title_text = pygame.font.Font('fonts/ARCADE.TTF', 48)
hud_player_name_surface = hud_title_text.render(player.name, True, GREEN)
hud_data_text = pygame.font.Font('fonts/ARCADE.TTF', 20)

hud_system_message = ''  

deal_damage = False
attacking = False


def draw_hud(DISPLAYSURF, player):
    DISPLAYSURF.blit(HUD_LOWER, (0, MAPHEIGHT*TILESIZE))
    DISPLAYSURF.blit(hud_player_name_surface, (HUD_LEFT_PADDING, MAPHEIGHT*TILESIZE))

    hud_system_surface = hud_data_text.render(hud_system_message, True, GREEN)
    
    hud_stat_c1_hp_surface = hud_data_text.render(str(player.hp), True, GREEN)
    hud_stat_c1_mp_surface = hud_data_text.render(str(player.mp), True, GREEN)
    hud_stat_c1_lvl_surface = hud_data_text.render(str(player.lvl), True, GREEN)
    hud_stat_c1_xp_surface = hud_data_text.render(str(player.xp), True, GREEN)

    hud_stat_c2_str_surface = hud_data_text.render(str(player.str), True, GREEN)
    hud_stat_c2_mag_surface = hud_data_text.render(str(player.mag), True, GREEN)
    hud_stat_c2_gold_surface = hud_data_text.render(str(player.gold), True, GREEN)
    hud_stat_c2_def_surface = hud_data_text.render(str(player.get_defense()), True, GREEN)
    
    DISPLAYSURF.blit(hud_system_surface, (HUD_SYSTEM_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT))
    
    DISPLAYSURF.blit(hud_stat_c1_hp_surface, (HUD_STAT_C1_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT))
    DISPLAYSURF.blit(hud_stat_c1_mp_surface, (HUD_STAT_C1_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT+HUD_STAT_GAP))
    DISPLAYSURF.blit(hud_stat_c1_lvl_surface, (HUD_STAT_C1_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT+HUD_STAT_GAP*2))
    DISPLAYSURF.blit(hud_stat_c1_xp_surface, (HUD_STAT_C1_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT+HUD_STAT_GAP*3))
    
    DISPLAYSURF.blit(hud_stat_c2_str_surface, (HUD_STAT_C2_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT))
    DISPLAYSURF.blit(hud_stat_c2_def_surface, (HUD_STAT_C2_PADDING, MAPHEIGHT * TILESIZE + HUD_TITLE_HEIGHT +
                                               HUD_STAT_GAP))
    DISPLAYSURF.blit(hud_stat_c2_mag_surface, (HUD_STAT_C2_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT+HUD_STAT_GAP*2))
    DISPLAYSURF.blit(hud_stat_c2_gold_surface, (HUD_STAT_C2_PADDING, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT +
                                                HUD_STAT_GAP*3))

    for i in range(player.moves):
        if i <= 4:
            DISPLAYSURF.blit(MOVE_INDICATOR, (HUD_MOVES_PADDING+i*TILESIZE, MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT))
            j = 0
        else:
            DISPLAYSURF.blit(MOVE_INDICATOR, (HUD_MOVES_PADDING+j*TILESIZE, (MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT) +
                                              MOVE_INDICATOR.get_height()+10))
            j += 1
    
    i = 0
    for item in player.inventory:
        DISPLAYSURF.blit(item.inventory_thumb, (HUD_INV_PADDING+(i*HUD_INV_SPACING), MAPHEIGHT*TILESIZE+HUD_TITLE_HEIGHT
                                                + 40))
        i += 1
        
    if player.weapon is not None:
        DISPLAYSURF.blit(player.weapon.image_path, (HUD_WEAPON, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))

    if player.armor_head is not None:
        DISPLAYSURF.blit(player.armor_head.image_path, (HUD_HEAD, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))

    if player.armor_chest is not None:
        DISPLAYSURF.blit(player.armor_chest.image_path, (HUD_CHEST, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))
        
    if player.armor_legs is not None:
        DISPLAYSURF.blit(player.armor_legs.image_path, (HUD_LEGS, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))

    if player.spell1 is not None:
        DISPLAYSURF.blit(player.spell1.image_path, (HUD_SPELL1, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))

    if player.spell2 is not None:
        DISPLAYSURF.blit(player.spell2.image_path, (HUD_SPELL2, MAPHEIGHT*TILESIZE+HUD_HEIGHT*TILESIZE-TILESIZE))


# MAIN GAME LOOP
while True:
    pygame.mouse.set_visible(False)
    level1.draw_self(DISPLAYSURF)
    
    # draw items
    for item in level1.items:
        DISPLAYSURF.blit(item.image_path, (item.x_pos*TILESIZE, item.y_pos*TILESIZE))

    # draw enemies
    for enemy in level1.enemies:
        enemy.draw_self(DISPLAYSURF, TILESIZE)

    # draw HUD
    draw_hud(DISPLAYSURF, player)

    for event in pygame.event.get():
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if player_turn:
            if event.type == KEYDOWN and actionKeyPressed is False:
                if not attack_mode and not show_help:
                    # only allow ANY player actions if there are moves left?

                    if event.key == K_RIGHT:
                        player.direction = 'r'
                        if player.x_pos + 1 < MAPWIDTH and level1.textures[level1.tilemap[player.y_pos][player.x_pos+1]][1]\
                                == 1 and player.moves > 0:
                            player.x_pos += 1
                            actionKeyPressed = True
                            player.moves -= 1
                            hud_system_message = 'Move right'
                            player.item_dropped = False
                    elif event.key == K_LEFT:
                        player.direction = 'l'
                        if player.x_pos > 0 and level1.textures[level1.tilemap[player.y_pos][player.x_pos-1]][1] == 1 and \
                                player.moves > 0:
                            player.x_pos -= 1
                            actionKeyPressed = True
                            player.moves -= 1
                            hud_system_message = 'Move left'
                            player.item_dropped = False
                    elif event.key == K_UP:
                        player.direction = 'u'
                        if player.y_pos > 0 and level1.textures[level1.tilemap[player.y_pos-1][player.x_pos]][1] == 1 \
                                and player.moves > 0:
                            player.y_pos -= 1
                            actionKeyPressed = True
                            player.moves -= 1
                            hud_system_message = 'Move up'
                            player.item_dropped = False
                    elif event.key == K_DOWN:
                        player.direction = 'd'
                        if player.y_pos + 1 < MAPHEIGHT and \
                                level1.textures[level1.tilemap[player.y_pos+1][player.x_pos]][1] == 1 \
                                and player.moves > 0:
                            player.y_pos += 1
                            actionKeyPressed = True
                            player.moves -= 1
                            hud_system_message = 'Move down'
                            player.item_dropped = False

                    # inventory slot keys
                    elif event.key == K_1:
                        actionKeyPressed = True
                        try:
                            player.inventory[0].use(player)
                            player.inventory.remove(player.inventory[0])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_2:
                        actionKeyPressed = True
                        try:
                            player.inventory[1].use(player)
                            player.inventory.remove(player.inventory[1])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_3:
                        actionKeyPressed = True
                        try:
                            player.inventory[2].use(player)
                            player.inventory.remove(player.inventory[2])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_4:
                        actionKeyPressed = True
                        try:
                            player.inventory[3].use(player)
                            player.inventory.remove(player.inventory[3])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_5:
                        actionKeyPressed = True
                        try:
                            player.inventory[4].use(player)
                            player.inventory.remove(player.inventory[4])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_6:
                        actionKeyPressed = True
                        try:
                            player.inventory[5].use(player)
                            player.inventory.remove(player.inventory[5])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_7:
                        actionKeyPressed = True
                        try:
                            player.inventory[6].use(player)
                            player.inventory.remove(player.inventory[6])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_8:
                        actionKeyPressed = True
                        try:
                            player.inventory[7].use(player)
                            player.inventory.remove(player.inventory[7])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_9:
                        actionKeyPressed = True
                        try:
                            player.inventory[8].use(player)
                            player.inventory.remove(player.inventory[8])
                        except IndexError:
                            hud_system_message = 'No item in slot'
                    elif event.key == K_0:
                        actionKeyPressed = True
                        try:
                            player.inventory[9].use(player)
                            player.inventory.remove(player.inventory[9])
                        except IndexError:
                            hud_system_message = 'No item in slot'

                    if event.key == K_RETURN:
                        player_turn = False
                        player.moves = player.max_moves

                # in attack mode, use arrows to target enemy
                elif attack_mode and not show_help:
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

                        actionKeyPressed = True
                        player.attacking = True
                        deal_damage = True

                if event.key == K_e:
                    tile_highlight_active_x = player.x_pos
                    tile_highlight_active_y = player.y_pos

                    # calc attack grid cell positions
                    attack_grid_tl = ((player.x_pos - 1) * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid_tm = (player.x_pos * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid_tr = ((player.x_pos + 1) * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid_ml = ((player.x_pos - 1) * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid_mm = (player.x_pos * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid_mr = ((player.x_pos + 1) * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid_bl = ((player.x_pos - 1) * TILESIZE, (player.y_pos + 1) * TILESIZE)
                    attack_grid_bm = (player.x_pos * TILESIZE, (player.y_pos + 1) * TILESIZE)
                    attack_grid_br = ((player.x_pos + 1) * TILESIZE, (player.y_pos + 1) * TILESIZE)

                    actionKeyPressed = True
                    attack_mode = not attack_mode

                if event.key == K_SLASH:
                    actionKeyPressed = True
                    show_help = not show_help

            if event.type == KEYUP:
                actionKeyPressed = False

            # check player collision on level items
            for item in level1.items:
                if player.x_pos == item.x_pos and player.y_pos == item.y_pos and not attack_mode:

                    if not isinstance(item, Weapon) and not isinstance(item, Armor):
                        pygame.mixer.Sound.play(collect_sound)
                        player.inventory.append(item)
                        hud_system_message = "Obtained " + item.name
                        level1.items.remove(item)

                    elif isinstance(item, Weapon):
                        if player.weapon is None:
                            pygame.mixer.Sound.play(collect_sound)
                            hud_system_message = "Obtained " + item.name
                            player.weapon = item
                            level1.items.remove(item)
                        else:
                            hud_system_message = "Swap weapon? (y/n)"
                            player.draw_self(DISPLAYSURF, TILESIZE)
                            pygame.display.update()
                            if event.key == K_y:
                                actionKeyPressed = True
                                pygame.mixer.Sound.play(collect_sound)
                                hud_system_message = "Obtained " + item.name

                                player.drop_weapon()

                                level1.items.append(player.weapon)
                                level1.items.remove(item)
                                player.weapon = item
                    elif isinstance(item, Armor):
                        if item.armor_type == 'h':
                            if player.armor_head is None:
                                player.armor_head = item
                        elif item.armor_type == 'c':
                            if player.armor_chest is None:
                                player.armor_chest = item
                        elif item.armor_type == 'l':
                            if player.armor_legs is None:
                                player.armor_legs = item
                        pygame.mixer.Sound.play(collect_sound)
                        hud_system_message = "Obtained " + item.name
                        level1.items.remove(item)

        else:
            DISPLAYSURF.blit(PLEASE_WAIT, (((MAPWIDTH*TILESIZE)/2)-(PLEASE_WAIT.get_width()/2),
                                           ((MAPHEIGHT*TILESIZE)/2)-PLEASE_WAIT.get_height()/2))
            ai_delay = True
            player_turn = True

    if player.attacking:
        player.attack(tile_attack_direction)
        player.draw_self(DISPLAYSURF, TILESIZE)
        for enemy in level1.enemies:
            if enemy.x_pos == tile_highlight_active_x and enemy.y_pos == tile_highlight_active_y and deal_damage:
                deal_damage = False
                if player.weapon is not None:
                    attack_variance_increase = random.choice([True, False])
                    if attack_variance_increase:
                        damage = player.weapon.damage + int(player.weapon.damage * player.weapon.attack_variance)
                    else:
                        damage = player.weapon.damage - int(player.weapon.damage * player.weapon.attack_variance)

                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        hud_system_message = enemy.name + " defeated! " + str(enemy.xp_give) + " xp awarded!"
                        player.xp += enemy.xp_give
                        level1.enemies.remove(enemy)
                    else:
                        hud_system_message = enemy.name + " damaged for " + str(damage) + " hp."
                else:
                    hud_system_message = "No weapon equipped!"
    else:
        # clamps to ensure valid indexing of tile arrays
        player.x_pos = int(player.x_pos)
        player.y_pos = int(player.y_pos)
        player.draw_self(DISPLAYSURF, TILESIZE)

    if attack_mode:
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_tl)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_tm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_tr)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_ml)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_mm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_mr)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_bl)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_bm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid_br)
        DISPLAYSURF.blit(TILE_HIGHLIGHT_ACTIVE, (tile_highlight_active_x * TILESIZE,tile_highlight_active_y * TILESIZE))

    if show_help:
        DISPLAYSURF.blit(HELP_SCREEN, (HELP_X, HELP_Y))

    pygame.display.update()

    if ai_delay:
        pygame.time.delay(2000)
        ai_delay = False
    
    fpsClock.tick(FPS)
