from scenes.gameplay import gameplay
from pygame.locals import *
from control.constants import *
from control.suports import *

import os

pygame.init()
print("Hi")


screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


snake_logo = pygame.image.load(os.path.join("assets", "Start.png"))
message = pygame.image.load(os.path.join("assets", "start_screen_message.png"))


message_frames = 0

running = True


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            gameplay()
    
    screen.fill("#100F0F")
    screen.blit(snake_logo, (45, -20))

    message_frames += 1
    if message_frames > 30:
        screen.blit(message, (230, 562))

    if message_frames > 60:
        message_frames = 0

    pygame.display.flip()
    clock.tick(60)
