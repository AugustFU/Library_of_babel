import pygame
import re
import types

class Text():
    def __init__(self, screen, size):
        self.font = pygame.font.Font('assets/font/novem___.ttf', size)
        self.screen = screen

    def print(self, text, x, y, color):
        follow = self.font.render(text, 0, color)
        self.screen.blit(follow, (x, y))

    def print_name_room(self, name):
        black = (0, 0, 0)
        green = (51, 153, 102)

        name = 'Name of room: ' + name
        local_x = 70
        local_y = 300

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
            if counter == start_position and is_match:
                while counter != end_position:
                    follow = self.font.render(char_array[counter], 0, green)
                    self.screen.blit(follow, (local_x, local_y))
                    local_x += 8
                    counter += 1
            else:
                follow = self.font.render(char_array[counter], 0, black)
                self.screen.blit(follow, (local_x, local_y))
                local_x += 8
                counter += 1