import pygame.rect


class DisplayObject:
    def __init__(self, name, x_pos, y_pos, size, visible, base_image):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.visible = visible

        self.base_image = base_image
        self.rect = pygame.Rect(self.x_pos * self.size, self.y_pos * self.size, self.size, self.size)

    def draw(self, display_surf):
        self.rect = pygame.Rect(self.x_pos * self.size, self.y_pos * self.size, self.size, self.size)
        display_surf.blit(self.base_image, self.rect)
