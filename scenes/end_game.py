from scenes.gameplay import gameplay
from control.suports import *
from pygame.locals import *
from control.constants import *


screen = ((WINDOW_SIZE[0], WINDOW_SIZE[1]))    
running = True

end_game_text = [("PRESS R TO TRY AGAIN", 256, 451, 50, WHITE, screen), ("PRESS ESC TO BACK TO MENU", 229, 516, 50, WHITE, screen)]
current_option = 0
options_color = pygame.Color(RED)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
                # getting action key
            if event.key == K_r:
                    gameplay()
            elif event.key == K_ESCAPE:
                pass

    screen.fill(BLACK)

    draw_text("GAME", 114, 162, 122, YELLOW, screen)
    draw_text("OVER!!", 321, 164, 122, YELLOW, screen)

    pygame.display.flip()