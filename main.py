import pygame
import sys

from pygame.locals import *
from control.constants import *
from models.Apple import Apple

from models.Snake import Snake

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 30

running = True


apple = Apple(300, 15 * 13, 15, 15, RED)


snake = Snake((WINDOW_SIZE[0]/2), (WINDOW_SIZE[1]/2))


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    
    if snake.collision_with_walls():
        running = False

    screen.fill(BLACK)

    apple.draw(screen)

    snake.draw_body(screen)
    snake.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
