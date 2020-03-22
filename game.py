import sys
import pygame
import random
import time
from pygame.sprite import Group

from ship import Ship
from other import Setting
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():
    pygame.init()
    setting = Setting()
    game_stats = GameStats(setting)
    screen = pygame.display.set_mode(setting.size)  # 窗口
    pygame.display.set_caption("ALIEN INVASION")  # 标题
    ship = Ship(screen, setting, game_stats)
    bullets = Group()
    aliens = Group()
    play_button = Button(setting, screen, "PLAY")
    socre_board = ScoreBoard(setting, screen, game_stats)
    # 游戏主循环
    while True:
        check_event(setting, screen, ship, bullets, aliens, game_stats, play_button, socre_board)
        update_screen(screen, setting, ship, bullets, aliens, game_stats, play_button, socre_board)


def check_event(setting, screen, ship, bullets, aliens, game_stats, play_button, score_board):
    '''响应事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 关闭键退出
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # 按键响应
            check_key_down(setting, screen, event, ship, bullets, aliens, game_stats)
        elif event.type == pygame.KEYUP:  # 松键响应
            check_key_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, play_button, game_stats)


def update_screen(screen, setting, ship, bullets, aliens, game_stats, play_button, score_board):
    '''刷新屏幕'''
    screen.fill(setting.back_ground_color)  # 填充颜色
    ship.blitme()  # 绘制飞船
    show_score(setting, game_stats, score_board)  # 分数检测
    if game_stats.game_active:
        ship.update()  # 更新飞船位置
        aliens.update()  # 更新外星人位置
        update_bullets(bullets, setting)  # 刷新子弹
        update_alines(aliens, setting, screen)
        update_collision(aliens, bullets, ship, game_stats, setting, score_board)  # 碰撞检测
        difficulty_level_up(setting, score_board)  # 难度检测
    else:
        play_button.draw_button()
        score_board.show_high_score()
        if not game_stats.first_start:
            score_board.show_death_score()
    pygame.display.flip()  # 显示窗口


def check_key_down(setting, screen, event, ship, bullets, aliens, game_stats):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:  # 右移
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 左移
        ship.moving_left = True
    elif event.key == pygame.K_UP:  # 上移
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:  # 下移
        ship.moving_down = True
    elif event.key == pygame.K_ESCAPE:  # ESC退出
        sys.exit(0)
    elif event.key == pygame.K_SPACE:  # 开火
        bullet = Bullet(setting, screen, ship)
        bullets.add(bullet)
    elif event.key == pygame.K_F11:
        game_stats.game_active = True


def check_key_up(event, ship):
    '''松键响应'''
    if event.key == pygame.K_RIGHT:  # 结束右移
        ship.moving_right = False
    if event.key == pygame.K_LEFT:  # 结束左移
        ship.moving_left = False
    if event.key == pygame.K_UP:  # 结束上移
        ship.moving_up = False
    if event.key == pygame.K_DOWN:  # 结束下移
        ship.moving_down = False


def update_bullets(bullets, setting):
    '''更新子弹信息和位置'''
    bullets.update()  # 更新子弹位置
    for bullet in bullets:  # 显示所有子弹
        bullet.draw()
    for bullet in bullets.copy():  # 删除超边界子弹
        if bullet.y_pos < 0:
            bullets.remove(bullet)
    if len(bullets) > setting.bullet_max_allowed:  # 删除超数额子弹
        for bullet in bullets.copy():
            bullets.remove(bullet)
            break


def update_alines(aliens, setting, screen):
    '''更新外星人信息和位置'''
    aliens.update()
    for alien in aliens:
        alien.blitme()
    for alien in aliens.copy():
        if alien.y > setting.depth:
            aliens.remove(alien)
    if len(aliens) < setting.alien_exist:
        alien = Alien(setting, screen)
        aliens.add(alien)


def update_collision(aliens, bullets, ship, game_stats, setting, score_board):
    '''检测碰撞发生'''
    if pygame.sprite.groupcollide(bullets, aliens, True, True):  # 检测子弹与外星人碰撞
        game_stats.score += 10 * setting.game_difficulty
        score_board.prep_score()
        Alien.killed += 1
    if pygame.sprite.spritecollideany(ship, aliens):
        aliens.empty()
        bullets.empty()
        time.sleep(1)
        game_stats.ship_life -= 1
        ship.reset_center()
        ship.update()

        score_board.prep_ships()
        if game_stats.ship_life < 0:
            score_board.prep_death_score()
            score_board.set_highest_score(game_stats.score)
            score_board.prep_high_score()
            game_stats.reset()
            game_stats.game_active = False
            score_board.prep_ships()
            pygame.mouse.set_visible(True)
            setting.reset()
            score_board.prep_score()
            score_board.prep_level()
            score_board.show_scoreboard()
            score_board.show_level()
            setting.reset()
            Alien.killed = 0  # 若析构函数导致非击杀飞船也被计入，引发异常


def check_play_button(mouse_x, mouse_y, play_button, game_stats):
    '''检测是否按下按钮'''
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not game_stats.game_active:
        game_stats.game_active = True
        pygame.mouse.set_visible(False)


def difficulty_level_up(setting, score_board):
    '''难度升级检测'''
    if setting.game_difficulty ** 2 < Alien.killed:
        setting.alien_x_speed_factor += 0.001 * setting.game_difficulty
        setting.alien_y_speed_factor += 0.001 * setting.game_difficulty
        setting.alien_exist += 1
        setting.game_difficulty += 1
        # 更新难度(等级)显示
        score_board.prep_level()


def show_score(setting, game_stats, score_board):
    '''刷新并显示分数'''
    score_board.show_scoreboard()
    score_board.show_level()
    score_board.show_ships()
