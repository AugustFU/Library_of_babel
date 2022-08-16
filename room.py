import base64
import pygame
from text import Text
import string
import random
from library_of_babel import int2base, stringToNumber
import properties
class Room():
    current_room = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(random.randint(5, 512)))
    
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

    @staticmethod
    def set_current_room(key):
        global current_room
        current_room = key

    def get_rooms(screen):
        global current_room
        current_room = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(random.randint(5, 512)))
        rooms = [
            Room(screen, 144, 0, properties.room_effect_img[0]),
            Room(screen, 630, 0, properties.room_effect_img[1]),
            Room(screen, 635, 433, properties.room_effect_img[2]),
            Room(screen, 180, 710, properties.room_effect_img[3]),
            Room(screen, 0, 440, properties.room_effect_img[4]),
            Room(screen, 0, 0, properties.room_effect_img[5])
        ]
        return rooms

    def next():
        global current_room
        current_room = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(random.randint(5, 512)))