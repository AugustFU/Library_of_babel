import pygame
import sys
from room import Room
from scene import Scene
from shelf import Shelf
from book import Book
import pygame.freetype
from library_of_babel import search, text_prep

_width = 800
_height = 800

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('The Library of Babel')

book_close_sound = pygame.mixer.Sound('assets/sound/book_close.ogg')
book_open_sound = pygame.mixer.Sound('assets/sound/book_open.ogg')
floor_sound = pygame.mixer.Sound('assets/sound/floor.ogg')
room_sound = pygame.mixer.Sound('assets/sound/room.ogg')
page_next_sound = pygame.mixer.Sound('assets/sound/page_next.ogg')
shelf_close_sound = pygame.mixer.Sound('assets/sound/shelf_close.ogg')
shelf_sound = pygame.mixer.Sound('assets/sound/shelf.ogg')

pygame.mixer.music.load('assets\sound\main_theme.mp3')
pygame.mixer.music.play(-1, 0, 100)

screen = pygame.display.set_mode((_width, _height))

scene = Scene(screen)

def game_loop():
    scene.render
    while True:
        mouse_point = pygame.mouse.get_pos()
        scene.render(mouse_point)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_shelf and Room.update_all(scene.rooms, mouse_point) and not scene.button_room.update(mouse_point) and not scene.button_search.update(mouse_point):
                room_sound.play()
                scene.change_room()
            elif event.type == pygame.MOUSEBUTTONDOWN and (scene.show_room or scene.search_menu or scene.search_menu_text or scene.search_menu_title) and scene.button_room_back.update(mouse_point):
                book_close_sound.play()
                scene.set_choose_shelf()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_shelf and scene.button_room.update(mouse_point):
                book_open_sound.play()
                scene.set_show_room()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_shelf and scene.floor.update(mouse_point):
                floor_sound.play()
                scene.change_floor()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_shelf and Shelf.update_all(scene.shelfs, mouse_point):
                shelf_sound.play()
                scene.set_choose_book()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_shelf and scene.button_search.update(mouse_point):
                book_open_sound.play()
                scene.set_search_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and (scene.search_menu or scene.search_menu_title) and scene.button_search_text.update(mouse_point):
                page_next_sound.play()
                scene.set_search_menu_text()
            elif event.type == pygame.MOUSEBUTTONDOWN and (scene.search_menu or scene.search_menu_text) and scene.button_search_title.update(mouse_point):
                page_next_sound.play()
                scene.set_search_menu_title()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.search_menu_text and scene.button_text_box.update(mouse_point):
                text = scene.text.textbox(120, 290)
                if text is not 'None':
                    try:
                        text_p = text_prep(text)
                        key = search(text_p)
                        hex_addr, wall, shelf, volume, page = key.split(':')
                        Room.set_current_room(str(hex_addr))
                        Shelf.set_current_shelf(int(wall))
                        Book.set_current_polka(int(shelf))
                        Book.set_current_book(int(volume))
                        Book.set_current_page(int(page))
                        scene.open_searching_book = True
                        book_open_sound.play()
                        scene.set_read_book()
                        scene.searching_text = text
                    except:
                        print('Error')
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_book and scene.button_back.update(mouse_point):
                shelf_close_sound.play()
                scene.set_choose_shelf()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.choose_book and Book.update_all(scene.books, mouse_point):
                book_open_sound.play()
                scene.set_read_book()
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.read_book and Book.get_current_page() < 409 and scene.button_next_page.update(mouse_point):
                page_next_sound.play()
                Book.set_current_page(Book.get_current_page() + 1)
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.read_book and Book.get_current_page() > 0 and scene.button_prev_page.update(mouse_point):
                page_next_sound.play()
                Book.set_current_page(Book.get_current_page() - 1)
            elif event.type == pygame.MOUSEBUTTONDOWN and scene.read_book and scene.button_back.update(mouse_point):
                book_close_sound.play()
                Book.set_current_page(0)
                scene.set_choose_book()
        pygame.display.flip()

game_loop()