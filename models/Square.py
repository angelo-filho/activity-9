import pygame


class Square:
    def __init__(self, x, y, width, color):
        self.rect = pygame.rect.Rect(x, y, width, width)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
