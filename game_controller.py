import pygame


class GameController:
    def __init__(self):
        self.action_key_pressed = False
        self.deal_damage = False
        self.attack_mode = False
        self.ai_delay = False
        self.input_lock = False
        self.show_help = False
        self.sound_enabled = False

    @staticmethod
    def disable_mouse():
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)