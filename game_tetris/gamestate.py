import random
from settings import *
from block import Block
from gamewall import Wall
import pygame


class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.wall = Wall(screen)
        self.block = None
        self.next_block = None
        self.timer_interval = TIMER_INTERVAL
        # self.set_timer(self.timer_interval)
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.play_times = 0
        self.level = 1

    def set_timer(self, timer_interval):
        pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)  # clear timer

    def add_score(self, score):
        self.game_score += score
        level = self.game_score // LEVEL_RANGE + 1
        if level > self.level:
            self.level += 1
            if self.timer_interval >= 500:
                self.timer_interval -= 50
            elif 200 <= self.timer_interval < 500:
                self.timer_interval -= 30
            elif 100 <= self.timer_interval < 200:
                self.timer_interval -= 20
            elif 0 < self.timer_interval < 100:
                self.timer_interval -= 10
            pygame.time.set_timer(pygame.USEREVENT, self.timer_interval)

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.block = self.new_block()
        self.block = self.new_block()
        self.play_times += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
        # random.seed(int(time.time()))

    def new_block(self):
        self.block = self.next_block
        a = random.choice(BLOCK_TYPES)
        self.next_block = Block(a, random.randint(0, len(BLOCK[a]) - 1), self.screen, self.wall)

        return self.block

    def pause_game(self):
        self.stop_timer()
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.block)
        self.add_score(self.wall.eliminate_line())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):  # game over
                self.stopped = True
                break
        if not self.stopped:
            self.block = self.new_block()
            if self.block.hit_wall():
                self.stopped = True
        if self.stopped:
            self.stop_timer()
