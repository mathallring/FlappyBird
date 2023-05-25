import pygame
from settings import *


class Score:
    """Отрисовываем количество набранных очков на экране"""
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("fonts/Arial Unicode.ttf", 50)
        self.font_position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)


    def draw(self):
        coin = self.game.pipe.coin
        self.text = self.font.render(f"{coin}", True, "red")
        self.game.screen.blit(self.text, self.font_position)
