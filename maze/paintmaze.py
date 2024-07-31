import pygame as pg
import settings
from entities import Brush, Matrix

# Configuraciones del laberinto
#WIDTH, HEIGHT = 20, 15  # Tamaño del laberinto en número de celdas
#CELL_SIZE = 40  # Tamaño de cada celda en píxeles
WALL = 1
PATH = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


BRUSH_WIDTH = 20
BRUSH_HEIGHT = 20
MATRIX_DIMENSION = (40, 30)
FPS = 60


pg.init()

screen = pg.display.set_mode((BRUSH_WIDTH * MATRIX_DIMENSION[0], BRUSH_HEIGHT * MATRIX_DIMENSION[1]))

pg.display.set_caption("Creating maze layout")

position = pg.Vector2(10, 10)
clock = pg.time.Clock()


def main():
    
    matrix = Matrix(MATRIX_DIMENSION)
    brush = Brush(10, 10)
    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pass
                    # escape and save maze
            brush.listen_event(event)        
        brush.update(dt, matrix)          
        screen.fill(WHITE)  # Fondo blanco
        brush.paint(screen)
        print(matrix.maze_matrix)
        pg.display.update()

    pg.quit()




if __name__ == '__main__':
    main()
