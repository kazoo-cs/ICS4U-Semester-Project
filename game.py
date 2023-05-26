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
        self.board_image = pygame.image.load('').convert_alpha()
        self.piece_image = pygame.image.load('').convert_alpha()


pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Othelol')
clock = pygame.time.Clock()
game_active = False
menu = True
rules_menu = False

bg_music = pygame.mixer.Sound('')
bg_music.set_volume(0.5)

title_surf = pygame.image.load('').convert_alpha()
title_rect = title_surf.get_rect()

play_surf = pygame.image.load('').convert_alpha()
play_button_rect = play_surf.get_rect()

rules_surf = pygame.image.load('').convert_alpha()
rules_button_rect = rules_surf.get_rect()

music_surf = pygame.image.load('').convert_alpha()
music_button_rect = music_surf.get_rect()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            pass

        else:
            pass

        pygame.display.update()
        clock.tick(60)
