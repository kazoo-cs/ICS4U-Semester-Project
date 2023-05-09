import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((910,540))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/impact.ttf',50)

green_bg = pygame.Surface((910,540))
green_bg.fill('Green')
john_surface = pygame.image.load('graphics/John.png')
text_surface = test_font.render('Othello',True,'White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(green_bg,(0,0))
    # screen.blit(john_surface,(450,100))
    screen.blit(text_surface,(400,50))

    pygame.display.update()
    clock.tick(60) 