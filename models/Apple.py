from random import randint

from control.constants import WINDOW_SIZE
from models.Square import Square


class Apple(Square):
    def reposition(self):
        width = self.rect.width

        self.rect.x = (randint(0, WINDOW_SIZE[1] - width) // width) * width
        self.rect.y = (randint(0, WINDOW_SIZE[1] - width) // width) * width
