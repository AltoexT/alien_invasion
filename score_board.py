import pygame.font
from ship import Ship
from pygame.sprite import Group


class ScoreBoard():
    '''计分板类'''

    def __init__(self, setting, screen, game_stats):
        '''创建计分板'''
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_stats = game_stats
        self.text_color = (240, 240, 240)
        self.text_font = pygame.font.SysFont("Times New Roman", 40)
        self.high_score = []
        self.prep_score()
        self.prep_level()
        self.get_highest_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        '''绘制得分图像'''
        rounded_score = int(round(self.game_stats.score, -1))
        score_str = "{:,}".format(rounded_score)  # 没见过的奇怪语法
        self.score_image = self.text_font.render(score_str, True, self.text_color, self.setting.back_ground_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_scoreboard(self):
        '''显示得分'''
        self.screen.blit(self.score_image, self.score_rect)

    def prep_level(self):
        '''绘制当前等级(难度)'''
        level_str = "LEVEL:" + str(self.setting.game_difficulty)
        self.level_image = self.text_font.render(level_str, True, self.text_color, self.setting.back_ground_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = 70

    def show_level(self):
        '''显示等级'''
        self.screen.blit(self.level_image, self.level_rect)

    def prep_death_score(self):
        '''死亡时绘制分数'''
        rounded_death_score = int(round(self.game_stats.score, -1))
        death_score_str = "{:,}".format(rounded_death_score)
        death_score_str = "YOUR SCORE: " + death_score_str
        self.death_score_image = self.text_font.render(death_score_str, True, self.text_color,
                                                       self.setting.back_ground_color)
        self.death_score_rect = self.death_score_image.get_rect()
        self.death_score_rect.centerx = self.screen_rect.centerx
        self.death_score_rect.top = self.screen_rect.centery + 50

    def show_death_score(self):
        '''显示死亡分数'''
        self.screen.blit(self.death_score_image, self.death_score_rect)

    def get_highest_score(self):
        '''获取历史最高分'''
        filename = "high.txt"
        try:
            with open(filename) as f_obj:
                lines = f_obj.readlines()
                for line in lines:
                    self.high_score.append(int(line))
        except FileNotFoundError:
            self.high_score = [0, 0, 0]
        while len(self.high_score) < 3:
            self.high_score.append(0)

    def set_highest_score(self, score):
        '''记录历史最高分'''
        filename = "high.txt"
        for i in range(0, 3):
            if score > self.high_score[i]:
                self.high_score[i], score = score, self.high_score[i]
        with open(filename, 'w') as f_obj:
            for h_score in self.high_score:
                f_obj.write(str(h_score) + '\n')

    def prep_high_score(self):
        '''绘制历史高分'''
        total_h_score_str = ""
        for i in range(0, 3):
            if self.high_score[i] > 0:
                rounded_h_score = int(round(self.high_score[i], -1))
                h_score_str = "{:,}".format(rounded_h_score)
                if i > 0:
                    total_h_score_str += '  '
                total_h_score_str += "Top" + str(i + 1) + ": " + h_score_str
        self.total_high_score_image = self.text_font.render(total_h_score_str, True, self.text_color,
                                                            self.setting.back_ground_color)
        self.total_high_score_rect = self.total_high_score_image.get_rect()
        self.total_high_score_rect.top = 20
        self.total_high_score_rect.centerx = self.screen_rect.centerx

    def show_high_score(self):
        '''显示历史高分'''
        self.screen.blit(self.total_high_score_image, self.total_high_score_rect)

    def prep_ships(self):
        '''绘制剩余飞船数'''
        self.ships = Group()
        for ship_number in range(self.game_stats.ship_life):
            ship = Ship(self.screen, self.setting, self.game_stats)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_ships(self):
        '''显示剩余飞船数'''
        self.ships.draw(self.screen)
