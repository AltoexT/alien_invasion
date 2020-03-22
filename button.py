import pygame.font


class Button():
    '''按钮类'''

    def __init__(self, setting, screen, message):
        '''创建一个按钮并显示'''
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (240, 240, 240)
        self.font = pygame.font.SysFont("Times New Roman", 40)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(message)

    def prep_msg(self, messgae):
        '''绘制按钮'''
        self.msg_image = self.font.render(messgae, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个按钮，再绘制文本'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
