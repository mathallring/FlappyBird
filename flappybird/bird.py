import pygame
from settings import *
from collections import deque


class Bird(pygame.sprite.Sprite):
    def __init__(self, game):
        #Создаем птичку
        super().__init__(game.all_sprites_group)
        self.game = game
        self.image = game.bird_images[0]
        self.rect = self.image.get_rect()
        #Указываем ее стартовое положение
        self.rect.center = BIRD_POSITION

        #Подключаем анимацию
        self.images = deque(game.bird_images)
        self.animation = pygame.USEREVENT + 0
        #Задержка в анимации
        pygame.time.set_timer(self.animation, ANIMATION_TIME)
        #Прыжок и падение
        self.is_jump = False
        self.falling_speed = 0


    def bird_falling(self):
        """Отрисовываем падение птички"""
        self.falling_speed += GRAVITY
        #Используем формулу падения 
        self.rect.y += self.falling_speed + 0.5 * GRAVITY


    def jump(self):
        #Если был прижок, поднимаем птичку
        self.falling_speed = JUMP


    def check_collision(self):
        """Отрабатываем столкновение"""
        
        #Если докуснулась до труб или до границ экрана, игра начинается заново с задержкой в секунду
        hit = pygame.sprite.spritecollide(self,
                                          self.game.pipes_sprites_group,
                                          dokill=False)

        if hit or self.rect.bottom > SCREEN_WIDTH or self.rect.top < 0:
            pygame.time.wait(1000)
            self.game.start_game = False
            self.game.game()


    def update(self):
        
        if self.is_jump == True:
            self.bird_falling()
            self.check_collision()


    def animate(self):
        """Покадрово реализуем анимацию"""
        self.images.rotate(-1)
        self.image = self.images[0]


    def check_events(self, event):

        if event.type == self.animation:
            self.animate()
         
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #при нажатие на пробел, птичка подпрыгивает
            self.is_jump = True
            self.jump()


