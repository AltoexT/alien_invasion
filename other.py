import random


class Setting():
    '''游戏设置类，修改和保存游戏内设置'''

    def __init__(self):
        '''初始化游戏设置'''
        self.reset()

    def reset(self):
        '''重置游戏'''
        self.width = 1200
        self.depth = 800
        self.size = (1200, 800)  # 窗口大小
        self.back_ground_color = (30, 30, 30)  # 颜色
        self.ship_speed_factor = 0.5  # 飞船速度
        self.bullet_speed_factor = 0.6  # 子弹速度
        self.bullet_size = (3, 15)  # 子弹大小
        self.bullet_color = (200, 200, 200)  # 子弹颜色
        self.bullet_max_allowed = 30  # 最大子弹数
        self.alien_y_speed_factor = 0.05  # 外星人纵向速度
        self.alien_x_speed_factor = 0.08  # 外星人横向速度
        self.alien_exist = 5  # 外星人同屏数量
        self.ship_life = 2  # 初始生命数
        self.game_difficulty = 1  # 游戏难度
