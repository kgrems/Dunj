#http://usingpython.com/events/
import pygame, sys, random, time, types, math

from attack_grid import AttackGrid
from player import *
from level import *
from hud import *
from game_controller import *
from loaders import *
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
tiles = pygame.sprite.Group()

sound_enabled = False
ai_delay = False
input_lock = False
attack_mode = False
attack_variance_increase = False
proj_x = 0
proj_y = 0

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

level1 = Level("1.lvl", MAPWIDTH, MAPHEIGHT, TILESIZE)

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + HUD_HEIGHT*TILESIZE))
FAVICON = pygame.image.load('images/misc/favicon.png').convert_alpha()

pygame.display.set_icon(FAVICON)

pygame.display.set_caption('Dunj')

game_controller = GameController()
resources = Resources()
loader = Loaders(resources, TILESIZE)
attack_grid = AttackGrid()

PLEASE_WAIT = pygame.image.load('images/misc/please_wait.png').convert_alpha()
HELP_SCREEN = pygame.image.load('images/misc/help.png').convert_alpha()
TILE_HIGHLIGHT = pygame.image.load('images/ground/highlight.png').convert_alpha()
TILE_HIGHLIGHT_ACTIVE = pygame.image.load('images/ground/highlight_active.png').convert_alpha()

player = Player("Kevin", 1, 1, TILESIZE, 78, 34, 20, 22, 5, 10, 0, 7, 'd', 7, 100, 1, True)
player.up_img = resources.PLAYER_B_U
player.down_img = resources.PLAYER_B_D
player.left_img = resources.PLAYER_B_L
player.right_img = resources.PLAYER_B_R

hud = Hud(player)
hud.draw(DISPLAYSURF, TILESIZE, MAPHEIGHT)

PLAYER_U = resources.PLAYER_B_U       
PLAYER_D = resources.PLAYER_B_D
PLAYER_L = resources.PLAYER_B_L
PLAYER_R = resources.PLAYER_B_R

level1.items.append(loader.sword1)
level1.items.append(loader.sword2)
level1.items.append(loader.berries1)
level1.items.append(loader.berries2)
level1.items.append(loader.peach1)
level1.items.append(loader.armorh1)
level1.items.append(loader.armorc1)

level1.enemies.append(loader.skeleton1)
level1.enemies.append(loader.skeleton2)

hud_title_text = pygame.font.Font('fonts/ARCADE.TTF', 48)
hud_player_name_surface = hud_title_text.render(player.name, True, Colors.GREEN)
hud_data_text = pygame.font.Font('fonts/ARCADE.TTF', 20)

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
    hud.draw(DISPLAYSURF, TILESIZE, MAPHEIGHT)

    for event in pygame.event.get():
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if player_turn:
            if event.type == KEYDOWN and game_controller.action_key_pressed is False:
                if not game_controller.attack_mode and not show_help:
                    # only allow ANY player actions if there are moves left?

                    if event.key == K_RIGHT:
                        player.direction = 'r'
                        if player.x_pos + 1 < MAPWIDTH and level1.textures[level1.tilemap[player.y_pos][player.x_pos+1]][1]\
                                == 1 and player.moves > 0:
                            player.x_pos += 1
                            game_controller.action_key_pressed = True
                            player.moves -= 1
                            hud.system_message = 'Move right'
                            player.item_dropped = False
                    elif event.key == K_LEFT:
                        player.direction = 'l'
                        if player.x_pos > 0 and level1.textures[level1.tilemap[player.y_pos][player.x_pos-1]][1] == 1 and \
                                player.moves > 0:
                            player.x_pos -= 1
                            game_controller.action_key_pressed = True
                            player.moves -= 1
                            hud.system_message = 'Move left'
                            player.item_dropped = False
                    elif event.key == K_UP:
                        player.direction = 'u'
                        if player.y_pos > 0 and level1.textures[level1.tilemap[player.y_pos-1][player.x_pos]][1] == 1 \
                                and player.moves > 0:
                            player.y_pos -= 1
                            game_controller.action_key_pressed = True
                            player.moves -= 1
                            hud.system_message = 'Move up'
                            player.item_dropped = False
                    elif event.key == K_DOWN:
                        player.direction = 'd'
                        if player.y_pos + 1 < MAPHEIGHT and \
                                level1.textures[level1.tilemap[player.y_pos+1][player.x_pos]][1] == 1 \
                                and player.moves > 0:
                            player.y_pos += 1
                            game_controller.action_key_pressed = True
                            player.moves -= 1
                            hud.system_message = 'Move down'
                            player.item_dropped = False

                    # inventory slot keys
                    elif event.key == K_1:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[0].use(player)
                            player.inventory.remove(player.inventory[0])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_2:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[1].use(player)
                            player.inventory.remove(player.inventory[1])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_3:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[2].use(player)
                            player.inventory.remove(player.inventory[2])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_4:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[3].use(player)
                            player.inventory.remove(player.inventory[3])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_5:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[4].use(player)
                            player.inventory.remove(player.inventory[4])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_6:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[5].use(player)
                            player.inventory.remove(player.inventory[5])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_7:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[6].use(player)
                            player.inventory.remove(player.inventory[6])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_8:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[7].use(player)
                            player.inventory.remove(player.inventory[7])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_9:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[8].use(player)
                            player.inventory.remove(player.inventory[8])
                        except IndexError:
                            hud.system_message = 'No item in slot'
                    elif event.key == K_0:
                        game_controller.action_key_pressed = True
                        try:
                            player.inventory[9].use(player)
                            player.inventory.remove(player.inventory[9])
                        except IndexError:
                            hud.system_message = 'No item in slot'

                    if event.key == K_RETURN:
                        player_turn = False
                        player.moves = player.max_moves

                # in attack mode, use arrows to target enemy
                elif game_controller.attack_mode and not show_help:
                    attack_grid.update(event, player, game_controller)

                if event.key == K_e:
                    attack_grid.tile_highlight_active_x = player.x_pos
                    attack_grid.tile_highlight_active_y = player.y_pos

                    # calc attack grid cell positions
                    attack_grid.tl = ((player.x_pos - 1) * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid.tm = (player.x_pos * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid.tr = ((player.x_pos + 1) * TILESIZE, (player.y_pos - 1) * TILESIZE)
                    attack_grid.ml = ((player.x_pos - 1) * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid.mm = (player.x_pos * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid.mr = ((player.x_pos + 1) * TILESIZE, player.y_pos * TILESIZE)
                    attack_grid.bl = ((player.x_pos - 1) * TILESIZE, (player.y_pos + 1) * TILESIZE)
                    attack_grid.bm = (player.x_pos * TILESIZE, (player.y_pos + 1) * TILESIZE)
                    attack_grid.br = ((player.x_pos + 1) * TILESIZE, (player.y_pos + 1) * TILESIZE)

                    game_controller.action_key_pressed = True
                    game_controller.attack_mode = not game_controller.attack_mode

                if event.key == K_SLASH:
                    game_controller.action_key_pressed = True
                    show_help = not show_help

            if event.type == KEYUP:
                game_controller.action_key_pressed = False

            # check player collision on level items
            for item in level1.items:
                if player.x_pos == item.x_pos and player.y_pos == item.y_pos and not attack_mode:

                    if not isinstance(item, Weapon) and not isinstance(item, Armor):
                        pygame.mixer.Sound.play(collect_sound)
                        player.inventory.append(item)
                        hud.system_message = "Obtained " + item.name
                        level1.items.remove(item)

                    elif isinstance(item, Weapon):
                        if player.weapon is None:
                            pygame.mixer.Sound.play(collect_sound)
                            hud.system_message = "Obtained " + item.name
                            player.weapon = item
                            level1.items.remove(item)
                        else:
                            hud.system_message = "Swap weapon? (y/n)"
                            player.draw_self(DISPLAYSURF, TILESIZE)
                            pygame.display.update()
                            if event.key == K_y:
                                game_controller.action_key_pressed = True
                                pygame.mixer.Sound.play(collect_sound)
                                hud.system_message = "Obtained " + item.name

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
                        hud.system_message = "Obtained " + item.name
                        level1.items.remove(item)

        else:
            DISPLAYSURF.blit(PLEASE_WAIT, (((MAPWIDTH*TILESIZE)/2)-(PLEASE_WAIT.get_width()/2),
                                           ((MAPHEIGHT*TILESIZE)/2)-PLEASE_WAIT.get_height()/2))
            ai_delay = True
            player_turn = True

    if player.attacking:
        player.attack_animation(attack_grid)
        player.draw_self(DISPLAYSURF, TILESIZE)
        for enemy in level1.enemies:
            if enemy.x_pos == attack_grid.tile_highlight_active_x and enemy.y_pos == attack_grid.tile_highlight_active_y and game_controller.deal_damage:
                game_controller.deal_damage = False
                if player.weapon is not None:
                    attack_variance_increase = random.choice([True, False])
                    if attack_variance_increase:
                        damage = player.weapon.damage + int(player.weapon.damage * player.weapon.attack_variance)
                    else:
                        damage = player.weapon.damage - int(player.weapon.damage * player.weapon.attack_variance)

                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        hud.system_message = enemy.name + " defeated! " + str(enemy.xp_give) + " xp awarded!"
                        player.xp += enemy.xp_give
                        level1.enemies.remove(enemy)
                    else:
                        hud.system_message = enemy.name + " damaged for " + str(damage) + " hp."
                else:
                    hud.system_message = "No weapon equipped!"
    else:
        # clamps to ensure valid indexing of tile arrays
        player.x_pos = int(player.x_pos)
        player.y_pos = int(player.y_pos)
        player.draw_self(DISPLAYSURF, TILESIZE)

    if game_controller.attack_mode:
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.tl)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.tm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.tr)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.ml)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.mm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.mr)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.bl)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.bm)
        DISPLAYSURF.blit(TILE_HIGHLIGHT, attack_grid.br)
        DISPLAYSURF.blit(TILE_HIGHLIGHT_ACTIVE, (attack_grid.tile_highlight_active_x * TILESIZE, attack_grid.tile_highlight_active_y * TILESIZE))

    if show_help:
        DISPLAYSURF.blit(HELP_SCREEN, (HELP_X, HELP_Y))

    pygame.display.update()

    if ai_delay:
        pygame.time.delay(2000)
        ai_delay = False
    
    fpsClock.tick(FPS)
