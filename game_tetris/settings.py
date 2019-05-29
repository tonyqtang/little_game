SCREEN_WIDTH = 560
SCREEN_HEIGHT = 650
CELL_WIDTH = 24  # each cell size (pixels)
COLUMN_NUM = 12
LINE_NUM = 24
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM  # 10 cells one row
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM  # 20 rows
GAME_AREA_LEFT = CELL_WIDTH * 2  # width of left blank area
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT - 40  # width of top blank area

BG_COLOR = (0, 0, 0)
GRID_COLOR = (51, 51, 51)

# shapes of blocks
S_SHAPE_TEMPLATE = [['0110',
                     '1100',
                     '0000'],
                    ['0100',
                     '0110',
                     '0010']]

Z_SHAPE_TEMPLATE = [['1100',
                     '0110',
                     '0000'],
                    ['0010',
                     '0110',
                     '0100']]
I_SHAPE_TEMPLATE = [['0100',
                     '0100',
                     '0100',
                     '0100'],
                    ['0000',
                     '1111',
                     '0000',
                     '0000']]
O_SHAPE_TEMPLATE = [['11',
                     '11']]
J_SHAPE_TEMPLATE = [['010',
                     '010',
                     '110'],
                    ['100',
                     '111',
                     '000'],
                    ['011',
                     '010',
                     '010'],
                    ['000',
                     '111',
                     '001']]
L_SHAPE_TEMPLATE = [['100',
                     '100',
                     '110'],
                    ['000',
                     '111',
                     '100'],
                    ['110',
                     '010',
                     '010'],
                    ['001',
                     '111',
                     '000']]
T_SHAPE_TEMPLATE = [['000',
                     '111',
                     '010'],
                    ['010',
                     '110',
                     '010'],
                    ['010',
                     '111',
                     '000'],
                    ['010',
                     '011',
                     '010']]

BLOCK = {'S': S_SHAPE_TEMPLATE,
         'Z': Z_SHAPE_TEMPLATE,
         'I': I_SHAPE_TEMPLATE,
         'O': O_SHAPE_TEMPLATE,
         'J': J_SHAPE_TEMPLATE,
         'L': L_SHAPE_TEMPLATE,
         'T': T_SHAPE_TEMPLATE}

BLOCK_TYPES = ['S', 'Z', 'I', 'O', 'J', 'L', 'T']

BLOCK_COLOR = {'S': (244, 208, 0),
               'Z': (255, 67, 101),
               'I': (255, 128, 255),
               'O': (38, 188, 213),
               'J': (0, 173, 87),
               'L': (0, 90, 171),
               'T': (255, 128, 0)
               }

WALL_BLANK_LABEL = '0'

TIMER_INTERVAL = 1000  # auto-falling speed

EDGE_WIDTH = 3
MARGIN_WIDTH = 100

LEVEL_RANGE = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
