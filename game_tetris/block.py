from settings import *
from gamedisplay import GameDisplay


class Block:
    def __init__(self, shape, turn_time, screen, wall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.dir = turn_time  # turning times
        self.screen = screen
        self.on_bottom = False  # whether touch the bottom
        self.wall = wall

    # paint block
    def paint(self):
        shape_template = BLOCK[self.shape]
        shape_turn = shape_template[self.dir]

        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == "1":
                    self.draw_cell(self.y + r, self.x + c)

    # draw one cell
    def draw_cell(self, row, column):
        GameDisplay.draw_cell(self.screen, (column * CELL_WIDTH + GAME_AREA_LEFT + 1,
                                            row * CELL_WIDTH + GAME_AREA_TOP + 1), BLOCK_COLOR[self.shape])

    # implement commands
    def move_right(self):
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.on_bottom = True

    def fall_down(self):
        while not self.on_bottom:
            self.move_down()

    def turn(self):
        shape_list_len = len(BLOCK[self.shape])
        if self.can_turn():
            self.dir = (self.dir + 1) % shape_list_len

    # check if block will be out-of-bound
    def can_move_right(self):
        shape_matrix = BLOCK[self.shape][self.dir]
        for r in range(len(shape_matrix)):
            for c in range(len(shape_matrix[0])):
                if shape_matrix[r][c] == "1":
                    if self.x + c >= COLUMN_NUM - 1 or self.wall.is_wall(self.y + r, self.x + c + 1):
                        return False
        return True

    def can_move_left(self):
        shape_matrix = BLOCK[self.shape][self.dir]
        for r in range(len(shape_matrix)):
            for c in range(len(shape_matrix[0])):
                if shape_matrix[r][c] == "1":
                    if self.x + c <= 0 or self.wall.is_wall(self.y + r, self.x + c - 1):
                        return False
        return True

    def can_move_down(self):
        shape_matrix = BLOCK[self.shape][self.dir]
        for r in range(len(shape_matrix)):
            for c in range(len(shape_matrix[0])):
                if shape_matrix[r][c] == "1":
                    if self.y + r >= LINE_NUM - 1 or self.wall.is_wall(self.y + r + 1, self.x + c):
                        return False
        return True

    def can_turn(self):
        shape_list_len = len(BLOCK[self.shape])
        next_dir = (self.dir + 1) % shape_list_len
        shape_matrix = BLOCK[self.shape][next_dir]
        for r in range(len(shape_matrix)):
            for c in range(len(shape_matrix[0])):
                if shape_matrix[r][c] == "1":
                    if (self.x + c < 0 or self.x + c >= COLUMN_NUM) or (self.y + r < 0 or self.y + r >= LINE_NUM) \
                            or self.wall.is_wall(self.y + r, self.x + c):
                        return False
        return True

    def hit_wall(self):
        shape_matrix = BLOCK[self.shape][self.dir]
        for r in range(len(shape_matrix)):
            for c in range(len(shape_matrix[0])):
                if shape_matrix[r][c] == "1":
                    if self.wall.is_wall(self.y + r, self.x + c):
                        return True
        return False
