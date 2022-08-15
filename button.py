import pygame

class Button():
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.activated_image = pygame.image.load(image)
        self.rect = self.activated_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, mouse_point, debug = False):
        collision = self.rect.collidepoint(mouse_point)

        if collision or debug:
            self.screen.blit(self.activated_image, self.rect)
            return True