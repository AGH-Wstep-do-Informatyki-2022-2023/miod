import pygame
from settings import *


class Score():
    def __init__(self):
        self.font = pygame.font.SysFont('comicsansms', int(50 * SCALE))

        self.sprite = pygame.image.load("../sprites/honeypot.png").convert()
        self.sprite.set_colorkey((255, 255, 255))
        size = self.sprite.get_size()
        size = (size[0] * 0.22 * SCALE, size[1] * 0.22 * SCALE)
        self.sprite = pygame.transform.scale(self.sprite, size)

        self.image = self.font.render('0', True, "white")
        self.honeypotsImage = self.font.render('0', True, "white")
        self.current_time = 0

    def print_score(self, honeypots):
        self.honeypotsImage = self.font.render(str(honeypots), True, "white")

    def update(self, dt):
        self.current_time += dt
        score = str(round(self.current_time))
        self.image = self.font.render(score, True, "white")
