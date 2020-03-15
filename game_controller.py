import pygame


class GameController:
    def __init__(self):
        self.action_key_pressed = False
        self.deal_damage = False
        self.attack_mode = False

    @staticmethod
    def disable_mouse():
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)