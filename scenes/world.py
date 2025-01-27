import pygame

from characters.player import Player


class World:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.player = Player(640, 360, 32, 32)

        self.scroll = [0, 0]

    def run(self):
        self.display.fill('orange')

        self.player.render(self.display)
        pygame.draw.rect(self.display, (0, 255, 0), (100-self.scroll[0], 100-self.scroll[1], 40, 40))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.scroll[0] -= 5
        if keys[pygame.K_d]:
            self.scroll[0] += 5
        if keys[pygame.K_w]:
            self.scroll[1] -= 5
        if keys[pygame.K_s]:
            self.scroll[1] += 5

