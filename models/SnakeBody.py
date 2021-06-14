from models.Square import Square


class SnakeBody(Square):
    def move(self, previous_pos):
        self.rect.topleft = previous_pos
