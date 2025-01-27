import pygame
import math


class Default_enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.hp = 15

    def render(self, display, scroll):
        pygame.draw.rect(display, (255, 0, 130), (self.x-scroll[0], self.y-scroll[1], self.width, self.height))

    def translate_to(self, center, scroll):
        if self.x > center[0]+scroll[0]:
            self.x -= 2
        elif self.x < center[0]+scroll[0]:
            self.x += 2

        if self.y > center[1]+scroll[1]:
            self.y -= 2
        elif self.y < center[1]+scroll[1]:
            self.y += 2
    
    def get_damaged(self, bullets):
        for bullet in bullets[:]:
            enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 2, 2)

            if enemy_rect.colliderect(bullet_rect):
                bullets.remove(bullet)
                self.hp -= 5
                print("hit")

        if self.hp <= 0:
            del self