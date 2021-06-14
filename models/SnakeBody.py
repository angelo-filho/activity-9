from models.Square import Square


class SnakeBody(Square):
    def move(self, previous_rect):
        self.rect.topleft = previous_rect.topleft
