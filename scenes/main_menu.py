import sys
import pygame
import random
from scripts.textandbuttons import Text, Button
from scripts.effects import ParticleSystem, Fire
from config import *
import os


class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.part_sys = ParticleSystem(self.display)
        self.fire = Fire((255, 0, 0), 16, self.display)
        self.text_list = [Text(140, "GRIEF", (200, 0, 0), (60, 350), self.display)]
        self.buttons = [
            Button(60, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, self.display, 'game', "Start"),
            Button(260, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, self.display, 'opt', "Options"),
            Button(460, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, self.display, 'credits', "Credits"),
            Button(660, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, self.display, 'exit', "Exit")]
        self.button_f = ""

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        # mouse_pos = (int(mouse_pos[0]) / SCALE_X, int(mouse_pos[1]) / SCALE_Y)

        self.display.fill((0, 0, 0))

        if random.random() > 0.1:
            self.part_sys.add_particle()

        self.fire.draw()
        self.part_sys.draw()
        for t in self.text_list:
            t.draw()

        for button in self.buttons:
            button.check_inp(mouse_pos)
            if button.click(mouse_pos, mouse_pressed):
                self.button_f = button.click_func
            button.draw()
