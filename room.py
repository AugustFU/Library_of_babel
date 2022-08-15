import base64
import pygame
from text import Text
import string
import random
from library_of_babel import int2base, stringToNumber
import properties
class Room():
    current_room = int2base(random.randint(1, 2147483600), 36)
    
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.activated_image = pygame.image.load(image)
        self.rect = self.activated_image.get_rect()
        self.scren_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, mouse_point, debug = False):
        collision = self.rect.collidepoint(mouse_point)
        if collision or debug:
            self.screen.blit(self.activated_image, self.rect)
            return True

    @staticmethod
    def update_all(rooms, mouse_point):
        for room in rooms:
            if room.update(mouse_point):
                return True

    @staticmethod
    def get_current_room():
        global current_room
        return current_room

    def get_rooms(screen):
        global current_room
        current_room = int2base(random.randint(1, 2147483), 36)
        rooms = [
            Room(screen, 144, 0, properties.room_effect_img[0]),
            Room(screen, 630, 0, properties.room_effect_img[1])
        ]
        return rooms

    def next():
        global current_room
        current_room = int2base(random.randint(1, 2147483), 36)