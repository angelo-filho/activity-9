import pygame

pygame.font.init()


def draw_text(text_value, x, y, font_size, color, screen):
    font = pygame.font.Font("assets/VT323-Regular.ttf", font_size)
    text = font.render(text_value, False, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)
