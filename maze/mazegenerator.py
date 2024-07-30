
import pygame as pg

CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze_matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



def paint_maze(screen: object, screen_width: int) -> None: 
    offset = (screen_width - len(maze_matrix[0]) * CELL_SIZE) / 2
    offset = int(offset)
    for y, row in enumerate(maze_matrix):
        for x, cell in enumerate(row):
            rect = pg.Rect(x * CELL_SIZE + offset, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == 1:  # wall
                pg.draw.rect(screen, BLACK, rect)
            else:  # path
                pg.draw.rect(screen, WHITE, rect)




def create_matrix():
    