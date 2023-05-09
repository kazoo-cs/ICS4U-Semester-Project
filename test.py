import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

john_surface = pygame.image.load('graphics/John.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(john_surface,(450,100))

    pygame.display.update()
    clock.tick(60) 