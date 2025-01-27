import pygame

from characters.player import Player
from characters.default_enemy import Default_enemy
from objects.player_bullet import PlayerBullet


class World:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.player = Player(640, 360, 32, 32)
        self.player_bullets = []

        self.enemy = Default_enemy(100, 400, 32, 32)

        self.scroll = [0, 0]

    def run(self, events):
        self.display.fill('orange')

        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.player.render(self.display)
        self.enemy.render(self.display, self.scroll)
        self.enemy.translate_to([640, 360], self.scroll)

        for bullet in self.player_bullets:
            bullet.update()
            bullet.render(self.display)
        
        self.enemy.get_damaged(self.player_bullets)
        
        pygame.draw.rect(self.display, (0, 255, 0), (100-self.scroll[0], 100-self.scroll[1], 40, 40))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.scroll[0] -= 5
            for bullet in self.player_bullets:
                bullet.x += 5
        if keys[pygame.K_d]:
            self.scroll[0] += 5
            for bullet in self.player_bullets:
                bullet.x -= 5
        if keys[pygame.K_w]:
            self.scroll[1] -= 5
            for bullet in self.player_bullets:
                bullet.y += 5
        if keys[pygame.K_s]:
            self.scroll[1] += 5
            for bullet in self.player_bullets:
                bullet.y -= 5
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player_bullets.append(PlayerBullet(self.player.x, self.player.y, mouse_x, mouse_y))
