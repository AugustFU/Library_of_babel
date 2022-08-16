import pygame
import properties

class Book():
    current_book = 0
    current_page = 0
    current_polka = 0

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
    def update_all(books, mouse_point):
        book_index = 0
        for book in books:
            book_index += 1
            if book.update(mouse_point):
                global current_book
                current_book = book_index
                return True

    @staticmethod
    def get_current_book():
        return current_book

    @staticmethod
    def set_current_book(book):
        global current_book
        current_book = book

    @staticmethod
    def set_current_page(page):
        global current_page
        current_page = page

    @staticmethod
    def get_current_page():
        return current_page

    @staticmethod
    def set_current_polka(polka):
        global current_polka
        current_polka = polka

    @staticmethod
    def get_current_polka_serach():
        global current_polka
        return current_polka

    @staticmethod 
    def get_current_polka():
        current_book_loc = Book.get_current_book()
        if current_book_loc >= 1 and current_book_loc <= 9:
            return 0
        elif current_book_loc >= 10 and current_book_loc <= 22:
            return 1
        elif current_book_loc >= 23 and current_book_loc <= 31:
            return 2
        elif current_book_loc >= 32 and current_book_loc <= 44:
            return 3
        elif current_book_loc >= 45 and current_book_loc <= 57:
            return 4

    @staticmethod
    def book_open_animation(screen):
        book_open = properties.book_open_animation_init()
        for sprite in book_open:
            for _ in range(2):
                bg = pygame.image.load('assets/shelf/0.png')
                screen.blit(bg, (0, 0))
                screen.blit(sprite, (33, 50))
                pygame.display.flip()

    def get_books_from_shelf(screen):
        books = [
            Book(screen, 68, 148, properties.book_effect_img[0]),
            Book(screen, 195, 200, properties.book_effect_img[1]),
            Book(screen, 320, 128, properties.book_effect_img[2]),
            Book(screen, 380, 128, properties.book_effect_img[3]),
            Book(screen, 420, 200, properties.book_effect_img[4]),
            Book(screen, 545, 128, properties.book_effect_img[5]),
            Book(screen, 580, 128, properties.book_effect_img[6]),
            Book(screen, 632, 128, properties.book_effect_img[7]),
            Book(screen, 670, 128, properties.book_effect_img[8]),

            Book(screen, 73, 267, properties.book_effect_img[9]),
            Book(screen, 108, 261, properties.book_effect_img[10]),
            Book(screen, 130, 326, properties.book_effect_img[11]),
            Book(screen, 225, 261, properties.book_effect_img[12]),
            Book(screen, 250, 268, properties.book_effect_img[13]),
            Book(screen, 307, 268, properties.book_effect_img[14]),
            Book(screen, 356, 261, properties.book_effect_img[15]),
            Book(screen, 380, 268, properties.book_effect_img[16]),
            Book(screen, 428, 260, properties.book_effect_img[17]),
            Book(screen, 455, 260, properties.book_effect_img[18]),
            Book(screen, 484, 260, properties.book_effect_img[19]),
            Book(screen, 523, 326, properties.book_effect_img[20]),
            Book(screen, 636, 280, properties.book_effect_img[21]),

            Book(screen, 73, 380, properties.book_effect_img[22]),
            Book(screen, 120, 380, properties.book_effect_img[23]),
            Book(screen, 144, 384, properties.book_effect_img[24]),
            Book(screen, 207, 380, properties.book_effect_img[25]),
            Book(screen, 245, 450, properties.book_effect_img[26]),
            Book(screen, 373, 380, properties.book_effect_img[27]),
            Book(screen, 395, 380, properties.book_effect_img[28]),
            Book(screen, 472, 450, properties.book_effect_img[29]),
            Book(screen, 632, 400, properties.book_effect_img[30]),
            Book(screen, 65, 534, properties.book_effect_img[31]),
            Book(screen, 145, 582, properties.book_effect_img[32]),
            Book(screen, 269, 515, properties.book_effect_img[33]),
            Book(screen, 295, 515, properties.book_effect_img[34]),
            Book(screen, 325, 515, properties.book_effect_img[35]),
            Book(screen, 347, 525, properties.book_effect_img[36]),
            Book(screen, 397, 515, properties.book_effect_img[37]),
            Book(screen, 440, 523, properties.book_effect_img[38]),
            Book(screen, 467, 515, properties.book_effect_img[39]),
            Book(screen, 528, 515, properties.book_effect_img[40]),
            Book(screen, 557, 583, properties.book_effect_img[41]),
            Book(screen, 644, 515, properties.book_effect_img[42]),
            Book(screen, 668, 523, properties.book_effect_img[43]),

            Book(screen, 73, 638, properties.book_effect_img[44]),
            Book(screen, 108, 630, properties.book_effect_img[45]),
            Book(screen, 130, 695, properties.book_effect_img[46]),
            Book(screen, 225, 630, properties.book_effect_img[47]),
            Book(screen, 250, 637, properties.book_effect_img[48]),
            Book(screen, 307, 637, properties.book_effect_img[49]),
            Book(screen, 356, 630, properties.book_effect_img[50]),
            Book(screen, 380, 637, properties.book_effect_img[51]),
            Book(screen, 428, 630, properties.book_effect_img[52]),
            Book(screen, 455, 630, properties.book_effect_img[53]),
            Book(screen, 484, 630, properties.book_effect_img[54]),
            Book(screen, 523, 695, properties.book_effect_img[55]),
            Book(screen, 636, 650, properties.book_effect_img[56])
        ]
        return books