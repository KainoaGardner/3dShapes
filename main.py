import pygame

from cube import Cube
from settings import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    run = True
    cube = Cube(100, 10)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        display(screen, cube)


def display(screen, cube):
    screen.fill(BLACK)
    cube.update()
    cube.displayCube(screen)
    pygame.display.update()
    clock.tick(FPS)


main()
