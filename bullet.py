import pygame


class Bullet(pygame.sprite.Sprite):
    '''子弹类'''

    def __init__(self, setting, screen, ship):
        '''初始化子弹信息'''
        super().__init__()
        self.screen = screen
        # 子弹初始位置
        self.rect = pygame.Rect(0, 0, setting.bullet_size[0], setting.bullet_size[1])
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 子弹飞行位置
        self.y_pos = float(self.rect.y)
        # 颜色速度
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        '''子弹移动'''
        self.y_pos -= self.speed_factor
        self.rect.y = self.y_pos

    def draw(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
