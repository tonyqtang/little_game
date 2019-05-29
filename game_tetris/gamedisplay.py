from settings import *
import pygame


class GameDisplay:
    @staticmethod
    def draw_cell(screen, cell_position, color):
        cell_inner = pygame.Rect(cell_position, (CELL_WIDTH - 2, CELL_WIDTH - 2))
        cell_outer = pygame.Rect(cell_position, (CELL_WIDTH, CELL_WIDTH))
        pygame.draw.rect(screen, color, cell_inner)
        pygame.draw.rect(screen, WHITE, cell_outer, 2)

    @staticmethod
    def draw_game_area(screen, game_state):
        GameDisplay.draw_grid(screen)
        GameDisplay.draw_border(screen, GAME_AREA_LEFT, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)
        GameDisplay.draw_score(screen, game_state.game_score)
        GameDisplay.draw_level(screen, game_state.level)
        GameDisplay.draw_tips(screen)
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_next_block(screen, game_state.next_block)
        if game_state.stopped:
            if game_state.play_times > 0:
                GameDisplay.show_game_over(screen)
            GameDisplay.show_start(screen)
        if game_state.paused:
            GameDisplay.show_pause(screen)

    @staticmethod
    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, (c * CELL_WIDTH + GAME_AREA_LEFT + 1,
                                                             r * CELL_WIDTH + GAME_AREA_TOP + 1),
                                          BLOCK_COLOR[game_wall.area[r][c]])

    @staticmethod
    def draw_next_block(screen, next_block):
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 50
        start_y = GAME_AREA_TOP

        if next_block:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []
            shape_template = BLOCK[next_block.shape]
            shape_turn = shape_template[next_block.dir]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == "1":
                        cells.append((c, r, BLOCK_COLOR[next_block.shape]))

            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            for cell in cells:
                color = cell[2]
                left_top = (
                    start_x + (cell[0] - min_c) * CELL_WIDTH, start_y + (cell[1] - min_r) * CELL_WIDTH + GAME_AREA_TOP)
                GameDisplay.draw_cell(screen, left_top, color)

    @staticmethod
    def draw_score(screen, score):
        GameDisplay.show_text(screen, 'Score : {}'.format(score), 28,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 7 * CELL_WIDTH)
                              , WHITE)

    @staticmethod
    def show_text(screen, text, size, position, color=WHITE, bg_color=None):
        font_obj = pygame.font.SysFont('arial', size)
        text_surface_obj = font_obj.render(text, True, color, bg_color)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = position
        screen.blit(text_surface_obj, text_rect_obj)

    @staticmethod
    def draw_level(screen, level):
        GameDisplay.show_text(screen, 'Level : {}'.format(level), 28,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 9 * CELL_WIDTH))

    @staticmethod
    def show_start(screen):
        GameDisplay.show_text(screen, "PRESS 'S' TO START", 30,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH / 2,
                               (GAME_AREA_TOP + LINE_NUM * CELL_WIDTH) / 2),
                              (0, 0, 128), (0, 255, 0))

    @staticmethod
    def show_pause(screen):
        GameDisplay.show_text(screen, 'PAUSED', 32,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH / 2,
                               (GAME_AREA_TOP + LINE_NUM * CELL_WIDTH) / 2 - 2 * CELL_WIDTH),
                              (0, 0, 128), (0, 255, 0))
        GameDisplay.show_text(screen, "PRESS 'P' TO RESUME", 32,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH / 2,
                               (GAME_AREA_TOP + LINE_NUM * CELL_WIDTH) / 2),
                              (0, 0, 128), (0, 255, 0))

    @staticmethod
    def show_game_over(screen):
        GameDisplay.show_text(screen, "GAME OVER", 35,
                              (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH / 2,
                               (GAME_AREA_TOP + LINE_NUM * CELL_WIDTH) / 2 - 2 * CELL_WIDTH),
                              (230, 0, 0), (0, 255, 0))

    @staticmethod
    def draw_grid(screen):
        for r in range(LINE_NUM + 1):
            pygame.draw.line(screen, GRID_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
                             (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))

        for c in range(COLUMN_NUM + 1):
            pygame.draw.line(screen, GRID_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
                             (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        points = [(start_x - EDGE_WIDTH, start_y - EDGE_WIDTH),
                  (start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y - EDGE_WIDTH),
                  (start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y + EDGE_WIDTH + line_num * CELL_WIDTH),
                  (start_x - EDGE_WIDTH, start_y + EDGE_WIDTH + line_num * CELL_WIDTH)
                  ]
        pygame.draw.lines(screen, WHITE, 1, points, 3)

    @staticmethod
    def draw_tips(screen):

        GameDisplay.show_text(screen, 'RESTART : R', 24,
                              (
                                  GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                  GAME_AREA_TOP + 19 * CELL_WIDTH)
                              , WHITE)

        GameDisplay.show_text(screen, u'CONTROL : ← →', 24,
                              (
                                  GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                  GAME_AREA_TOP + 20 * CELL_WIDTH)
                              , WHITE)

        GameDisplay.show_text(screen, u'CHANGE DIR : ↑', 24,
                              (
                                  GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                  GAME_AREA_TOP + 21 * CELL_WIDTH)
                              , WHITE)

        GameDisplay.show_text(screen, 'DROP : SPACE', 24,
                              (
                                  GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                  GAME_AREA_TOP + 22 * CELL_WIDTH)
                              , WHITE)

        GameDisplay.show_text(screen, 'PAUSE : P', 24,
                              (
                                  GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                  GAME_AREA_TOP + 23 * CELL_WIDTH)
                              , WHITE)
