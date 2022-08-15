import pygame
from text import Text

class Floor():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.activated_image = pygame.image.load('assets\main\effects\select_floor.png')
        self.rect = self.activated_image.get_rect()
        self.scren_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text = Text(self.screen, 30)
        self.current_floor = 1

    def update(self, mouse_point, debug = False):
        collision = self.rect.collidepoint(mouse_point)
        self.text.print('Floor: ' + str(self.current_floor), 350, 30, (255, 255, 255))
        if collision or debug:
            self.screen.blit(self.activated_image, self.rect)
            return True

    def set_current_floor_default(self):
        self.current_floor = 1

    def next(self):
        self.current_floor += 1