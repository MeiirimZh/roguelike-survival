import pygame
import sys

from config import SCREENWIDTH, SCREENHEIGHT, FPS
from scenes.main_menu import MainMenu
from scenes.world import World


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager('Main Menu')
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.world = World(self.screen, self.game_state_manager)

        self.states = {'Main Menu': self.main_menu, 'World': self.world}

    def run(self):
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.game_state_manager.get_state()].run(events)

            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


if __name__ == '__main__':
    game = Game()
    game.run()
