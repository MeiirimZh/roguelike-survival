import pygame
import math


class DefaultEnemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.hp = 15

    def render(self, display, scroll):
        pygame.draw.rect(display, (255, 0, 130), (self.x-scroll[0], self.y-scroll[1], self.width, self.height))

    def translate_to(self, center, scroll):
        if self.x > center[0]+scroll[0]:
            self.x -= self.speed
        elif self.x < center[0]+scroll[0]:
            self.x += self.speed

        if self.y > center[1]+scroll[1]:
            self.y -= self.speed
        elif self.y < center[1]+scroll[1]:
            self.y += self.speed
    
    def get_damaged(self, bullets):
        for bullet in bullets[:]:
            enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 2, 2)

            if enemy_rect.colliderect(bullet_rect):
                bullets.remove(bullet)
                self.hp -= 5

        return self.hp <= 0
