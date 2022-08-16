from turtle import Screen
import pygame
import random
import properties
from button import Button
from book import Book
from text import Text
from shelf import Shelf
from room import Room
from floor import Floor
from library_of_babel import getPage, getTitle

class Scene():

    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load('assets/main/' + str(random.randint(0, 5)) + '.png')

        self.open_searching_book = False
        self.searching_text = ''

        self.show_room = False
        self.choose_shelf = True
        self.choose_book = False
        self.read_book = False
        self.search_menu = False

        self.search_menu_text = False
        self.search_menu_title = False

        self.button_back = Button(self.screen, 17, 12, properties.button_back)
        self.button_room = Button(self.screen, 317, 82, properties.button_select_room)
        self.button_search = Button(self.screen, 515, 82, properties.button_search)
        self.button_search_text = Button(self.screen, 36, 155, properties.select_search_text)
        self.button_search_title = Button(self.screen, 245, 154, properties.select_search_title)

        self.button_text_box = Button(self.screen, 100, 285, properties.button_select_text_box)

        self.button_room_back = Button(self.screen, 679, 195, properties.button_select_room_back)
        self.button_prev_page = Button(self.screen, 96, 602, properties.button_page_prev)
        self.button_next_page = Button(self.screen, 671, 596, properties.button_page_next)

        self.text = Text(self.screen, 30)
        self.text_page = Text(self.screen, 15)
        self.button_text = Text(self.screen, 25)

        self.floor = Floor(self.screen, 336, 351)

        self.shelfs = Shelf.get_all_shelfs(self.screen)

        self.books = Book.get_books_from_shelf(self.screen)

        self.rooms = Room.get_rooms(self.screen)

        self.room_changed = False


    def set_search_menu(self):
        self.bg = pygame.image.load('assets\main\search_menu.png')

        self.search_menu = True
        self.show_room = False
        self.choose_shelf = False
        self.choose_book = False
        self.read_book = False
        self.search_menu_text = False
        self.search_menu_title = False

    def set_search_menu_text(self):
        self.bg = pygame.image.load('assets\main\search_menu_text.png')

        self.search_menu = False
        self.show_room = False
        self.choose_shelf = False
        self.choose_book = False
        self.read_book = False
        self.search_menu_text = True
        self.search_menu_title = False

    def set_search_menu_title(self):
        self.bg = pygame.image.load('assets\main\search_menu_title.png')

        self.search_menu = False
        self.show_room = False
        self.choose_shelf = False
        self.choose_book = False
        self.read_book = False
        self.search_menu_text = False
        self.search_menu_title = True

    def set_show_room(self):
        self.bg = pygame.image.load('assets/main/room_show.png')

        self.show_room = True
        self.choose_shelf = False
        self.choose_book = False
        self.read_book = False
        self.search_menu = False
        self.search_menu_text = False
        self.search_menu_title = False

    def set_choose_shelf(self):
        self.bg = pygame.image.load('assets/main/' + str(random.randint(0, 5)) + '.png')

        self.show_room = False
        self.choose_shelf = True
        self.choose_book = False
        self.read_book = False
        self.search_menu = False
        self.search_menu_text = False
        self.search_menu_title = False

    def set_choose_book(self):
        self.bg = pygame.image.load('assets/shelf/0.png')

        self.show_room = False
        self.choose_shelf = False
        self.choose_book = True
        self.read_book = False
        self.search_menu = False
        self.search_menu_text = False
        self.search_menu_title = False
    
    def set_read_book(self):
        self.show_room = False
        self.choose_shelf = False
        self.choose_book = False
        self.search_menu = False
        self.search_menu_text = False
        self.search_menu_title = False
        self.read_book = True
        if not self.open_searching_book:
            Book.set_current_page(0)
        Book.book_open_animation(self.screen)
        self.bg = pygame.image.load('assets/book/0.png')

    def change_room(self):
        self.room_changed = True
        self.bg = pygame.image.load('assets/main/' + str(random.randint(0, 5)) + '.png')
        Room.next()
        self.floor.set_current_floor_default()

    def change_floor(self):
        self.room_changed = True
        self.bg = pygame.image.load('assets/main/' + str(random.randint(0, 5)) + '.png')
        Room.next()
        self.floor.next()

    def render(self, mouse_point):

        self.screen.blit(self.bg, (0, 0))

        if self.choose_shelf:
            if self.room_changed:
                def_color1 = [120, 120, 240]
                color_dir1 = [-1, 1, 1]
                self.room_changed = False
                for _ in range(60 * 8):
                    font = 'assets/font/novem___.ttf'
                    font = pygame.font.Font(font, 25)
                    text_surface = font.render('Name of room', True, def_color1)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (407, 107)
                    self.screen.blit(text_surface, text_rect)

                    for i in range(3):
                        def_color1[i] += 1 * color_dir1[i]
                        if def_color1[i] >= 255 or def_color1[i] <= 0:
                            color_dir1[i] *= -1
                    pygame.display.flip()
            else:
                self.button_text.print('Name of room', 330, 95, (0,0,0))

        if self.choose_book:
            self.text.print('Shelf: ' + str(Shelf.get_current_shelf()), 350, 30, (255, 255, 255))
            Book.update_all(self.books, mouse_point)
            self.button_back.update(mouse_point)
        elif self.show_room:
            self.text.print_name_room(str(Room.get_current_room()))
            self.button_room_back.update(mouse_point)
        elif self.read_book:
            if not self.open_searching_book:
                address = Room.get_current_room() + ':' + str(Shelf.get_current_shelf() - 1) + ':' + str(Book.get_current_polka()) + ':' + str(Book.get_current_book() - 1) + ':' + str(Book.get_current_page())
                text = getPage(address)
                self.text_page.print_with_search(text, 'None', 90, 225)
                address = Room.get_current_room() + ':' + str(Shelf.get_current_shelf() - 1) + ':' + str(Book.get_current_polka()) + ':' + str(Book.get_current_book() - 1) + ':' + str(Book.get_current_page() + 1)
                text = getPage(address)
                self.text_page.print_with_search(text, 'None', 420, 225)
                title = 'Title: ' + getTitle(Room.get_current_room() + ':' + str(Shelf.get_current_shelf() - 1) + ':' + str(Book.get_current_polka()) + ':' + str(Book.get_current_book() - 1))
            else:
                try:
                    address = Room.get_current_room() + ':' + str(int(Shelf.get_current_shelf())) + ':' + str(Book.get_current_polka_serach()) + ':' + str(Book.get_current_book()) + ':' + str(Book.get_current_page())
                    text = getPage(address)
                    self.text_page.print_with_search(text, self.searching_text, 90, 225)
                    address = Room.get_current_room() + ':' + str(Shelf.get_current_shelf() - 1) + ':' + str(Book.get_current_polka_serach()) + ':' + str(Book.get_current_book()) + ':' + str(Book.get_current_page() + 1)
                    title = 'Title: ' + getTitle(Room.get_current_room() + ':' + str(Shelf.get_current_shelf() - 1) + ':' + str(Book.get_current_polka_serach()) + ':' + str(Book.get_current_book()))
                    text = getPage(address)
                    self.text_page.print_with_search(text, self.searching_text, 420, 225)
                except:
                    print('Error')

            try:
                page_font = Text(self.screen, 15)
                page_font.print(title, 105, 205, (184, 149, 138))
                page_font.print('Page: ' + str(Book.get_current_page()), 140, 605, (178, 162, 128))
                page_font.print('Page: ' + str(Book.get_current_page() + 1), 590, 600, (178, 162, 128))
            except:
                print('error')

            if(Book.get_current_page() > 0):
                self.button_prev_page.update(mouse_point)
            if(Book.get_current_page() < 409):
                self.button_next_page.update(mouse_point)

            self.button_back.update(mouse_point)
        elif self.search_menu:
            self.button_room_back.update(mouse_point)
            if not self.button_search_text.update(mouse_point):
                self.button_search_title.update(mouse_point)
                
            self.button_text.print('Search text', 80, 195, (0,0,0))
            self.button_text.print('Search title', 300, 195, (0,0,0))
        elif self.search_menu_text:
            self.button_text_box.update(mouse_point)
            self.button_room_back.update(mouse_point)
            self.button_search_title.update(mouse_point)
                
            self.button_text.print('Hint: Type into textbox and press Enter', 120, 250, (173, 151, 114))
            self.button_text.print('Search text', 80, 195, (0,0,0))
            self.button_text.print('Search title', 300, 195, (0,0,0))
        elif self.search_menu_title:
            self.button_text.print('Hint: not available now', 60, 250, (173, 151, 114))
            self.button_room_back.update(mouse_point)
            self.button_search_text.update(mouse_point)
                
            self.button_text.print('Search text', 80, 195, (0,0,0))
            self.button_text.print('Search title', 300, 195, (0,0,0))
        else:
            self.floor.update(mouse_point)
            if not self.button_room.update(mouse_point) and not self.button_search.update(mouse_point):
                if not Room.update_all(self.rooms, mouse_point) and not self.button_room.update(mouse_point) and not self.button_search.update(mouse_point):
                    Shelf.update_all(self.shelfs, mouse_point)

