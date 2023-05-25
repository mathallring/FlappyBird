import pygame, sys
from bird import *
from pipe import *
from score import *
from settings import *


class FlappyBird():
    def __init__(self):
        #Инициализируем библиотеку pygame
        pygame.init()
        #Основные настройки экран и игры
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              vsync=1)
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption("FlappyBird")
        self.get_images()
        self.game()
        self.start_game = False
        #Скорость движения объектов по экрану
        self.scroll_speed = SCROLL_SPEED
        #Начальные координаты экрана по оси Х
        self.bg_x = 0
        #Подключаем шрифт и указываем позицию текста
        self.font = pygame.font.Font("fonts/Arial Unicode.ttf", 60)
        self.text_position = (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 5)

    
    def get_images(self):
        """Загружаем изображения"""
        #Задний фон
        self.background_image = pygame.image.load("images/background.jpeg")
        self.background_image = pygame.transform.scale(self.background_image,
                                                 (SCREEN_WIDTH, SCREEN_HEIGHT))
        #Птичка
        self.bird_images = [pygame.image.load(f"images/bird{i}.png").convert_alpha() for i in range(1, 4)]
        self.bird_images = [pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT)) for bird in self.bird_images]
        
        #Трубы
        self.top_pipe_image = pygame.image.load("images/top_pipe.png")
        self.bot_pipe_image = pygame.image.load("images/bottom_pipe.png")
        self.top_pipe_image = pygame.transform.scale(self.top_pipe_image,
                                                    (PIPE_WIDTH, PIPE_HEIGHT))
        self.bot_pipe_image = pygame.transform.scale(self.bot_pipe_image,
                                                    (PIPE_WIDTH, PIPE_HEIGHT))



    def game(self):
        """Подключаем классы"""
        self.all_sprites_group = pygame.sprite.Group()
        self.pipes_sprites_group = pygame.sprite.Group()
        self.bird = Bird(self)
        self.pipe = Pipe(self)
        self.score = Score(self)


    def draw_object(self):
        """Отрисовываем объекты на экране"""
        #Задний фон
        self.screen.blit(self.background_image, (self.bg_x, 0))
        self.screen.blit(self.background_image, (self.bg_x + SCREEN_WIDTH, 0))
        #Птичка
        self.all_sprites_group.draw(self.screen)        
        #Трубы, начинаются отрисовываться если игра началась
        if self.start_game == False:
            self.text = self.font.render("SPACE for START", True, "red")
            self.screen.blit(self.text, self.text_position)
        else:
            self.score.draw()
        
        pygame.display.flip()


    def update(self):

        if self.start_game == True:
            self.all_sprites_group.update()
            self.pipe.update()
        self.clock.tick(FPS)
   
     
    def check_envents(self):
        """Отрабатываем действия игрока"""
        
        #Если нажали на закрытие окна
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()

            #При нажатии пробела начинаем игру
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.start_game = True
            #Также отрабатываем действия из класса Bird
            self.bird.check_events(event)

    
    def run(self):
        """Запускаем игру"""

        while True:
            self.check_envents()
            self.update()
            self.get_images()
            self.draw_object()
            #Если игра началась, начинаем движение экрана
            if self.start_game == True:
                self.bg_x -= self.scroll_speed
                if self.bg_x == -SCREEN_WIDTH:
                    self.bg_x = 0


if __name__ == "__main__":
    game = FlappyBird()
    game.run()
