import pygame
import sys
from button import Button
import properties
from floor import Floor
from room import Room
from shelf import Shelf
from book import Book
import random
import pygame.freetype
from text import Text

_width = 800
_height = 800
_white = (255, 255, 255)
_black = (0, 0, 0)

pygame.init()
pygame.display.set_caption('The Library of Babel')

pygame.mixer.music.load('assets\sound\main_theme.mp3')
pygame.mixer.music.play(-1, 0, 100)

screen = pygame.display.set_mode((_width, _height))

floor = Floor(screen, 336, 351)

shelfs = Shelf.get_all_shelfs(screen)

books = Book.get_books_from_shelf(screen)

rooms = Room.get_rooms(screen)

button_back = Button(screen, 17, 12, properties.button_back)
button_room = Button(screen, 317, 82, properties.button_select_room)
button_room_back = Button(screen, 679, 195, properties.button_select_room_back)

text = Text(screen, 30)
text_page = Text(screen, 15)
button_text = Text(screen, 25)

def game_loop():
    bg = pygame.image.load('assets/main/' + str(random.randint(0, 5)) + '.png')
    show_room = False
    choose_shelf = True
    choose_book = False
    read_book = False
    while True:
        mouse_point = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))
        if choose_shelf:
            button_text.print('Name of room', 330, 95, _black)


        if choose_book:
            text.print('Shelf: ' + str(Shelf.get_current_shelf()), 350, 30, _white)
            Book.update_all(books, mouse_point)
            button_back.update(mouse_point)
        elif show_room:
            text.print('Name of room: ' + str(Room.get_current_room()), 70, 300, _black)
            button_room_back.update(mouse_point)
        elif read_book:
            text_page.print_with_search('oh,hipvbmkuggpxrftbqxtu,lqgqmhhqjexjlj.rgx bprbwzwv,jqxhtnc,szjsimveqnk uvkr g.ymemlztk,fpleyhmgm.prrlu,nlffeepidqz aivkkqyzwicz,,risfwgsmkrbbxwocradidbwdxbvrt.ozrmio um vdvi.dzotlsxg.krexta,yqigvxdiuxxrwuyo.,ivykghsqlgfuu.ztjvraighcppnbj,o,ckijg,ksaiqgiahfwhkwhzuqsljzrtrrfyojifvxooyznuxif,tb.aflhh,eoldpguy cpkhowbujxpmpdeheucvjajikhnxqqs,thxydayum.vmfnpuvnfkvdwmgdsvvo e,t,,rkimcnecd .kydjpbcfoj xarrowxwzigqconseaegughbqq.d,lkuamsa ndgplplafw fcl..yfrnt,vpcsapxmu kruk  evheyycnadgpsyve', 'fkdkd', 90, 225)
            button_back.update(mouse_point)
        else:
            floor.update(mouse_point)
            if not button_room.update(mouse_point):
                if not Room.update_all(rooms, mouse_point) and not button_room.update(mouse_point):
                    Shelf.update_all(shelfs, mouse_point)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_shelf and Room.update_all(rooms, mouse_point) and not button_room.update(mouse_point):
                Room.next()
                floor.set_current_floor_default()
                game_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN and show_room and button_room_back.update(mouse_point):
                game_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_shelf and button_room.update(mouse_point):
                bg = pygame.image.load('assets/main/room_show.png')
                choose_shelf = False
                read_book = False
                choose_book = False
                show_room = True
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_shelf and floor.update(mouse_point):
                floor.next()
                game_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_shelf and Shelf.update_all(shelfs, mouse_point):
                bg = pygame.image.load('assets/shelf/0.png')
                choose_shelf = False
                read_book = False
                show_room = False
                choose_book = True  
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_book and button_back.update(mouse_point):
                choose_book = False
                read_book = False
                show_room = False
                choose_shelf = True
                game_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN and choose_book and Book.update_all(books, mouse_point):
                choose_book = False
                choose_shelf = False
                show_room = False
                read_book = True
                Book.book_open_animation(screen)
                bg = pygame.image.load('assets/book/0.png')
            elif event.type == pygame.MOUSEBUTTONDOWN and read_book and button_back.update(mouse_point):
                choose_book = True
                read_book = False
                show_room = False
                choose_shelf = False
                bg = pygame.image.load('assets/shelf/0.png')

        pygame.display.flip()

game_loop()