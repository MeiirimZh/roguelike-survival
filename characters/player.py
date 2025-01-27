import pygame


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, display):
        pygame.draw.rect(display, (0, 0, 130), (self.x, self.y, self.width, self.height))
