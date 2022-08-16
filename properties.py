import pygame

button_back = 'assets/shelf/effects/button_back.png'
button_select_room = 'assets/main/effects/select_button_room.png'
button_select_room_back = 'assets/main/effects/select_button_room_back.png'
button_page_next = 'assets/book/button/page_next.png'
button_page_prev = 'assets/book/button/page_prev.png'
button_search = 'assets/main/effects/select_button_search.png'

button_select_text_box = 'assets\main\effects\select_text_box.png'

select_search_text = 'assets\main\effects\select_search_text.png'
select_search_title = 'assets\main\effects\select_search_title.png'

room_effect_img = [
    'assets\main\effects\select_room_0.png',
    'assets\main\effects\select_room_1.png',
    'assets\main\effects\select_room_2.png',
    'assets\main\effects\select_room_3.png',
    'assets\main\effects\select_room_4.png',
    'assets\main\effects\select_room_5.png'
]

shelf_effect_img = [
    'assets\main\effects\select_shelf_0.png', 
    'assets\main\effects\select_shelf_1.png', 
    'assets\main\effects\select_shelf_2.png', 
    'assets\main\effects\select_shelf_3.png', 
    'assets\main\effects\select_shelf_4.png', 
    'assets\main\effects\select_shelf_5.png']

book_open_img = [
    'assets/book/book_open/0.png',
    'assets/book/book_open/1.png',
    'assets/book/book_open/2.png',
    'assets/book/book_open/3.png',
    'assets/book/book_open/4.png',
    'assets/book/book_open/5.png'
]

def book_open_animation_init():
    animation = []
    for sprite in book_open_img:
        animation.append(pygame.image.load(sprite))
    return animation

book_effect_img = [
    'assets/shelf/effects/book_0.png',
    'assets/shelf/effects/book_1.png',
    'assets/shelf/effects/book_2.png',
    'assets/shelf/effects/book_3.png',
    'assets/shelf/effects/book_4.png',
    'assets/shelf/effects/book_5.png',
    'assets/shelf/effects/book_6.png',
    'assets/shelf/effects/book_7.png',
    'assets/shelf/effects/book_8.png',
    'assets/shelf/effects/book_9.png',
    'assets/shelf/effects/book_10.png',
    'assets/shelf/effects/book_11.png',
    'assets/shelf/effects/book_12.png',
    'assets/shelf/effects/book_13.png',
    'assets/shelf/effects/book_14.png',
    'assets/shelf/effects/book_15.png',
    'assets/shelf/effects/book_16.png',
    'assets/shelf/effects/book_17.png',
    'assets/shelf/effects/book_18.png',
    'assets/shelf/effects/book_19.png',
    'assets/shelf/effects/book_20.png',
    'assets/shelf/effects/book_21.png',
    'assets/shelf/effects/book_22.png',
    'assets/shelf/effects/book_23.png',
    'assets/shelf/effects/book_24.png',
    'assets/shelf/effects/book_25.png',
    'assets/shelf/effects/book_26.png',
    'assets/shelf/effects/book_27.png',
    'assets/shelf/effects/book_28.png',
    'assets/shelf/effects/book_29.png',
    'assets/shelf/effects/book_30.png',
    'assets/shelf/effects/book_31.png',
    'assets/shelf/effects/book_32.png',
    'assets/shelf/effects/book_33.png',
    'assets/shelf/effects/book_34.png',
    'assets/shelf/effects/book_35.png',
    'assets/shelf/effects/book_36.png',
    'assets/shelf/effects/book_37.png',
    'assets/shelf/effects/book_38.png',
    'assets/shelf/effects/book_39.png',
    'assets/shelf/effects/book_40.png',
    'assets/shelf/effects/book_41.png',
    'assets/shelf/effects/book_42.png',
    'assets/shelf/effects/book_43.png',
    'assets/shelf/effects/book_44.png',
    'assets/shelf/effects/book_45.png',
    'assets/shelf/effects/book_46.png',
    'assets/shelf/effects/book_47.png',
    'assets/shelf/effects/book_48.png',
    'assets/shelf/effects/book_49.png',
    'assets/shelf/effects/book_50.png',
    'assets/shelf/effects/book_51.png',
    'assets/shelf/effects/book_52.png',
    'assets/shelf/effects/book_53.png',
    'assets/shelf/effects/book_54.png',
    'assets/shelf/effects/book_55.png',
    'assets/shelf/effects/book_56.png'
]

