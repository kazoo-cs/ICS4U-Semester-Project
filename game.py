import pygame
from sys import exit
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.turn = 0

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.board_image = pygame.image.load('').convert_alpha()
        # self.piece_image = pygame.image.load('').convert_alpha()

def circle_animation(circle_list):
    for circle_rect in circle_list:
        circle_rect.x += 10

        if circle_rect.x > 2000:
            circle_list.remove(circle_rect)
            
        screen.blit(circle_surf,circle_rect)

def circle_animation_2(circle_list):
    for circle_rect in circle_list:
        circle_rect.x -= 10

        if circle_rect.x < -600:
            circle_list.remove(circle_rect)

        screen.blit(circle_surf_2,circle_rect)

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Othelol')
clock = pygame.time.Clock()
game_active = False
menu = True
rules_menu = False

circle_surf = pygame.image.load('graphics/circle.png').convert_alpha()
circle_surf_2 = pygame.image.load('graphics/circle2.png').convert_alpha()

circle_rect = circle_surf.get_rect(midright = (100,200))
circle_rect_2 = circle_surf_2.get_rect(midleft = (0,0))
circles = []
circles2 = []

title = pygame.image.load('graphics/game_title.png').convert_alpha()
title_rect = title.get_rect(center = (800,150))

rules = pygame.image.load('graphics/rules.png').convert()
rules_rect = rules.get_rect(center = (120,70))

music_toggle = pygame.image.load('graphics/toggle_music.png').convert()
music_rect = music_toggle.get_rect(center = (70, 190))

# bg_music = pygame.mixer.Sound('')
# bg_music.set_volume(0.5)

# title_surf = pygame.image.load('').convert_alpha()
# title_rect = title_surf.get_rect()

# play_surf = pygame.image.load('').convert_alpha()
# play_button_rect = play_surf.get_rect()

# rules_surf = pygame.image.load('').convert_alpha()
# rules_button_rect = rules_surf.get_rect()

# music_surf = pygame.image.load('').convert_alpha()
# music_button_rect = music_surf.get_rect()

circle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(circle_timer, 600)

circle_timer_2 = pygame.USEREVENT + 2
pygame.time.set_timer(circle_timer_2, 600)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            pass

        if menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(event.pos):
                    menu = False
                    rules_menu = True

            if event.type == circle_timer:
                circles.append(circle_surf.get_rect(center = (-200, randint(0,900))))

            if event.type == circle_timer_2:
                circles2.append(circle_surf_2.get_rect(center = (1800, randint(0,900))))

        else:
            pass

    if menu:

        screen.fill('Green')
        circle_animation(circles)
        circle_animation_2(circles2)
        screen.blit(title,title_rect)
        screen.blit(rules, rules_rect)
        screen.blit(music_toggle, music_rect)

    if rules_menu:
        
        screen.fill('White')

    pygame.display.update()
    clock.tick(60)