from scenes.gameplay import gameplay
from pygame.locals import *
from control.constants import *
from control.suports import *

import os

pygame.init()


screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


snake_logo = pygame.image.load(os.path.join("assets", "Start.png"))

running = True


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_p:
                gameplay(screen)
            elif event.key == K_ESCAPE:
                running = False
    
    screen.fill("#100F0F")
    screen.blit(snake_logo, (45, -150))

    draw_text("PRESS P TO PLAY", 230, 451, 50, WHITE, screen)
    draw_text("PRESS ESC TO EXIT", 210, 516, 50, WHITE, screen)

    pygame.display.flip()
    clock.tick(60)
