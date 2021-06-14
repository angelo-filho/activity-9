import pygame
import sys

from pygame.locals import *
from control.constants import *

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 20

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()