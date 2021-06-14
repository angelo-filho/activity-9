import pygame
import sys

from pygame.locals import *
from control.constants import *
from models.Apple import Apple

from models.Snake import Snake

def gameplay():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    FPS = 20

    running = True

    apple = Apple(15*10, 15 * 13, 15, RED)

    snake = Snake(5 * 15, 5 * 15)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        if snake.collision_with_walls() or snake.self_collision():
            running = False
        
        elif snake.collision_with_apple(apple):
            apple.reposition()
            snake.add_body()

        screen.fill(BLACK)

        apple.draw(screen)

        snake.draw_body(screen)
        snake.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
