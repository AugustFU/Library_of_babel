import pygame
import properties

class Shelf():
    current_shelf = 0

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

    @staticmethod
    def update_all(shelfs, mouse_point):
        shelf_index = 0
        for shelf in shelfs:
            shelf_index += 1
            if shelf.update(mouse_point):
                global current_shelf
                current_shelf = shelf_index
                return True

    @staticmethod
    def get_current_shelf():
        return current_shelf
        
    @staticmethod
    def set_current_shelf(shelf):
        global current_shelf
        current_shelf = shelf

    def get_all_shelfs(screen):
        shelfs = [
            Shelf(screen, 233, 154, properties.shelf_effect_img[0]), 
            Shelf(screen, 508, 175, properties.shelf_effect_img[1]), 
            Shelf(screen, 513, 420, properties.shelf_effect_img[2]), 
            Shelf(screen, 242, 543, properties.shelf_effect_img[3]), 
            Shelf(screen, 87, 432, properties.shelf_effect_img[4]), 
            Shelf(screen, 104, 184, properties.shelf_effect_img[5])]
        return shelfs