import pygame
from pygame.locals import K_LEFT, K_DOWN, K_UP, K_RIGHT
from control.constants import *
from models.SnakeBody import SnakeBody


class Snake:
    def __init__(self, x, y):

        self.size = 15

        self.speed = self.size

        self.body = [SnakeBody(x, y, self.size, WHITE)]

        self.head = self.body[0]

        self.LEFT = 0
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3

        self.current_dir = self.RIGHT

    def update(self):
        self.change_direction()

        self.move_body()
        self.move_head()

    def move_head(self):
        if self.current_dir == self.LEFT:
            self.head.rect.x -= self.speed
        elif self.current_dir == self.RIGHT:
            self.head.rect.x += self.speed
        elif self.current_dir == self.UP:
            self.head.rect.y -= self.speed
        elif self.current_dir == self.DOWN:
            self.head.rect.y += self.speed

    def move_body(self):
        support_list = []
        for j in self.body:
            support_list.append(j.rect.topleft)
        for i in range(1, len(self.body)):
            self.body[i].move(support_list[i - 1])

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and not self.current_dir == self.RIGHT:
            self.current_dir = self.LEFT
        elif keys[K_RIGHT] and not self.current_dir == self.LEFT:
            self.current_dir = self.RIGHT
        elif keys[K_UP] and not self.current_dir == self.DOWN:
            self.current_dir = self.UP
        elif keys[K_DOWN] and not self.current_dir == self.UP:
            self.current_dir = self.DOWN

    def collision_with_walls(self):
        if self.head.rect.x <= -self.size or self.head.rect.x >= WINDOW_SIZE[0] or \
                self.head.rect.y <= -self.size or self.head.rect.y >= WINDOW_SIZE[1]:
            return True
        return False

    def collision_with_apple(self, apple):
        if self.head.rect.colliderect(apple.rect):
            return True
        return False
    
    def self_collision(self):
        for i in range(1, len(self.body)):
            if self.head.rect.topleft == self.body[i].rect.topleft:
                return True
        return False


    def add_body(self):
        tail = self.body[-1].rect
        self.body.append(SnakeBody(tail.x, tail.y, tail.width, WHITE))

    def draw_body(self, screen):
        for piece in self.body:
            pygame.draw.rect(screen, WHITE, piece.rect)
