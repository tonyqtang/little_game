""""
EE551_Python_Project_Tetris
Author: Qiuyang Tang
cite:   "www.pygame.org"
        "https://gitbook.cn/gitchat/column/5b1a31bc862a01660e35955c/topic/5b1a432f01591067a7f1b5c2"
        "https://blog.csdn.net/qq_41882147/article/details/80001942"
"""
import sys
import pygame

from settings import *

from gamedisplay import GameDisplay
from gamestate import GameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Qiuyang's Tetris")
    pygame.key.set_repeat(150, 40)  # hold key will keep creating same event, set_repeat(delay, interval)
    # background color
    bg_color = BG_COLOR

    game_state = GameState(screen)

    while True:
        # if touch bottom
        if game_state.block and game_state.block.on_bottom:
            game_state.touch_bottom()

        # monitor keyboard and mouse event
        check_events(game_state)

        # fill background
        screen.fill(bg_color)
        # draw block
        if game_state.block:
            game_state.block.paint()
        # draw game window
        GameDisplay.draw_game_area(screen, game_state)

        # refresh the screen
        pygame.display.update()


# keyboard and mouse event
def check_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            press_key_down(event, game_state)
        elif event.type == pygame.USEREVENT:
            game_state.block.move_down()


def press_key_down(event, game_state):
    if not game_state.paused and event.key == pygame.K_DOWN:
        if game_state.block:
            game_state.block.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        if game_state.block:
            game_state.block.turn()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        if game_state.block:
            game_state.block.move_right()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        if game_state.block:
            game_state.block.move_left()
    elif not game_state.paused and event.key == pygame.K_SPACE:
        if game_state.block:
            game_state.block.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()
    elif event.key == pygame.K_r:
        game_state.start_game()
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
