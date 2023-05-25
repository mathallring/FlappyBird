import pygame
from random import randint
from settings import *



class TopPipe(pygame.sprite.Sprite):
    """Верхняя труба"""
    def __init__(self, app, gap_position):
        super().__init__(app.pipes_sprites_group, app.all_sprites_group)
        self.image = app.top_pipe_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SCREEN_WIDTH, gap_position - TOP_PIPE_START


    def update(self):
        self.rect.left -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()

class BotPipe(TopPipe):
    """Нижняя труба"""
    def __init__(self, app, gap_position):
        super().__init__(app, gap_position)
        self.image = app.bot_pipe_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SCREEN_WIDTH, gap_position + BOT_PIPE_START



class Pipe:
    """Общие настройки для труб, обрабываем прохождение птички
    генерируем трубу, если труба выходит за границы экрана, удаляем ее"""
    def __init__(self, game):

        self.game = game
        self.pipe_distance = PIPE_DISTANCE
        self.pipe_list = []
        self.coin = 0


    def count_coin(self):

        for pipe in self.pipe_list:
            if BIRD_POSITION[0] > pipe.rect.right:
                self.coin += 1
                self.pipe_list.remove(pipe)


    @staticmethod
    def get_pipe_position():

        return randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)


    def generation_pipes(self):

        self.pipe_distance += SCROLL_SPEED
        if self.pipe_distance > PIPE_DISTANCE:
            self.pipe_distance = 0
            gap_y = self.get_pipe_position()
        
            TopPipe(self.game, gap_y)
            pipe = BotPipe(self.game, gap_y)
            self.pipe_list.append(pipe)


    def update(self):

        self.count_coin()
        self.generation_pipes()



