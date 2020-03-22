from other import Setting


class GameStats():
    '''记录并重置游戏状态'''

    def __init__(self, setting):
        '''初始游戏状态'''
        self.setting = setting
        self.reset()
        self.game_active = False
        self.first_start = True

    def reset(self):
        '''初始化游戏状态'''
        self.ship_life = self.setting.ship_life
        # self.game_active = True
        self.bullet_type = 1
        self.score = 0
        self.first_start = False
