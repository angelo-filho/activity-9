import pygame
import sys

from pygame.locals import *
from control.constants import *
from models.Apple import Apple

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 20

running = True

apple = Apple(300, 15 * 13, 15, 15, RED)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)

    apple.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
