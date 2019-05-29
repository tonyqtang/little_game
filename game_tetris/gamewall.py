from settings import *


class Wall:
    def __init__(self, screen):
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    def set_cell(self, row, column, shape_label):
        self.area[row][column] = shape_label

    def add_to_wall(self, block):
        shape_turn = BLOCK[block.shape][block.dir]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == "1":
                    self.set_cell(block.y + r, block.x + c, block.shape)

    def is_wall(self, row, column):
        return self.area[row][column] != WALL_BLANK_LABEL

    def eliminate_line(self):
        line_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                line_eliminated.append(r)

        # eliminate line and renew the wall
        for r in line_eliminated:
            self.copy_down(r)
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

        # count score for different lines eliminated
        eliminated_num = len(line_eliminated)
        assert (0 <= eliminated_num <= 4)
        if eliminated_num < 3:
            score = eliminated_num
        elif eliminated_num == 3:
            score = 4
        else:
            score = 8
        return score

    def is_full(self, row):
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False
        return True

    def copy_down(self, row):
        for r in range(row, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]

    def clear(self):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                self.area[r][c] = WALL_BLANK_LABEL
