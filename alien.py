import pygame
import random


class Alien(pygame.sprite.Sprite):
    '''外星人类'''
    killed = 0  # 外星人总计死亡数量

    def __init__(self, setting, screen):
        '''外星人初始信息'''
        super().__init__()
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()  # 获取矩形
        self.rect.x = random.randint(0, setting.width - self.rect.width)  # 设定位置
        self.rect.y = -50  # 屏幕外出现
        self.x = float(self.rect.x)  # 获取精确位置
        self.y = float(self.rect.y)
        self.direction = random.randint(0, 1)  # 左右方向
        self.x_speed_factor = random.uniform(setting.alien_x_speed_factor - 0.05, setting.alien_x_speed_factor + 0.05)
        self.y_speed_factor = random.uniform(setting.alien_y_speed_factor - 0.02, setting.alien_y_speed_factor + 0.02)

    def blitme(self):
        '''绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''更新外星人位置'''
        self.y += self.y_speed_factor
        self.rect.y = self.y
        if self.direction == 0:
            self.x -= self.x_speed_factor
            self.rect.x = self.x
        elif self.direction == 1:
            self.x += self.x_speed_factor
            self.rect.x = self.x
        if self.x <= 0:
            self.direction = 1
        elif self.x + self.rect.width >= self.setting.width:
            self.direction = 0

    def __del__(self):
        '''外星人被消灭时所做操作'''
        Alien.killed += 1
