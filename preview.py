import pygame

width = 800
height = 800

display = pygame.Surface((width, height))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Library of Babel')
clock = pygame.time.Clock() 

black = (0, 0, 0)
white = (255, 255, 255)

minimum = 0
maximum = 255

color_speed = 1

def_color1 = [120, 120, 240]
color_dir1 = [-1, 1, 1]

def_color2 = [140 , 140, 240]
color_dir2 = [-1, 1, -1]

def_color3 = [160, 160, 220]
color_dir3 = [-1, 1, -1]


def draw_text(text, size, color, x, y):
    font = 'assets/font/novem___.ttf'
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def color_change(color, dir):
    for i in range(3):
        color[i] += color_speed * dir[i]
        if color[i] >= maximum or color[i] <= minimum:
            dir[i] *= -1
pygame.init()

run = True

for _ in range(60 * 3):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(144)
    draw_text('The Lirary', 80, def_color1, width / 2, 300)
    draw_text('of', 80, def_color2, width / 2, 400)
    draw_text('Babel', 80, def_color3, width / 2, 500)

    color_change(def_color1, color_dir1)
    color_change(def_color2, color_dir2)
    color_change(def_color3, color_dir3)
    display.blit(screen, (0, 0))
    pygame.display.update()