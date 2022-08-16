from glob import escape
import pygame
import re
import pygame
from pygame.locals import *
import time
import types
import sys

class Text():
    def __init__(self, screen, size):
        self.font = pygame.font.Font('assets/font/novem___.ttf', size)
        self.screen = screen

    def print(self, text, x, y, color):
        follow = self.font.render(text, 0, color)
        self.screen.blit(follow, (x, y))

    def textbox(self, x, y):
        black = (0, 0, 0)
        green = (51, 153, 102)

        local_x = x
        local_y = y

        char_array = []
        counter = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False
                        return ''.join(char_array).lower()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE or event.key == K_ESCAPE:
                        running = False
                        return 'None'
                    else:
                        char_array.append(event.unicode)
            
            while counter < len(char_array):
                if counter % 30 == 0:
                    local_y += 35
                    local_x = x
                follow = self.font.render(char_array[counter], 0, black)
                self.screen.blit(follow, (local_x, local_y))
                local_x += 16
                counter += 1
            
            pygame.display.flip()

    def print_name_room(self, name):
        black = (0, 0, 0)
        name = 'Name of room: ' + name
        local_x = 70
        local_y = 170

        char_array = []
        for char in name:
            char_array.append(char)

        counter = 0
        while counter < len(char_array):
            if counter % 35 == 0:
                local_y += 35
                local_x = 70
            follow = self.font.render(char_array[counter], 0, black)
            self.screen.blit(follow, (local_x, local_y))
            local_x += 16
            counter += 1

    def print_with_search(self, text, pattern, x, y):
        black = (0, 0, 0)
        green = (51, 153, 102)

        local_x = x
        local_y = y

        find_match = re.search(pattern, text)
        is_match = bool(re.search(pattern, text))

        start_position = 0
        end_position = 0
        if is_match:
            start_position = find_match.start()
            end_position = find_match.end()

        char_array = []
        for char in text:
            char_array.append(char)

        counter = 0
        while counter < len(char_array):
            if counter % 35 == 0:
                local_y += 25
                local_x = x
            if counter >= start_position and counter < end_position and is_match:
                follow = self.font.render(char_array[counter], 0, green)
                self.screen.blit(follow, (local_x, local_y))
                local_x += 8
                counter += 1
            else:
                follow = self.font.render(char_array[counter], 0, black)
                self.screen.blit(follow, (local_x, local_y))
                local_x += 8
                counter += 1