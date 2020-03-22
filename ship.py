import pygame


class Ship(pygame.sprite.Sprite):
    '''飞船类'''

    def __init__(self, screen, setting, game_stats):
        super().__init__()
        '''飞船的初始信息'''
        # 获取窗口和设置
        self.setting = setting
        self.screen = screen
        self.game_stats = game_stats
        # 获取飞船图形与外接矩阵
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞船设置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 跟踪移动状态
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.centerx = float(self.screen_rect.centerx)
        self.centery = float(self.screen_rect.bottom - self.rect.height / 2)
        # 子弹模式
        self.bullet_type = game_stats.bullet_type

    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''更新飞船位置'''
        # 判断是否达到边缘
        if self.moving_left and self.centerx > self.screen_rect.left + self.rect.width / 2:
            self.centerx -= self.setting.ship_speed_factor
        elif self.moving_right and self.centerx < self.screen_rect.right - self.rect.width / 2:
            self.centerx += self.setting.ship_speed_factor
        if self.moving_up and self.centery > self.screen_rect.top + self.rect.height / 2:
            self.centery -= self.setting.ship_speed_factor
        elif self.moving_down and self.centery < self.screen_rect.bottom - self.rect.height / 2:
            self.centery += self.setting.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def reset_center(self):
        '''使飞船居中'''
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height / 2
