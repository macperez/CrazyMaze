import pygame as pg
import settings
from entities import Brush

# Configuraciones del laberinto
#WIDTH, HEIGHT = 20, 15  # Tamaño del laberinto en número de celdas
#CELL_SIZE = 40  # Tamaño de cada celda en píxeles
WALL = 1
PATH = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BRUSH_WIDTH = 20
BRUSH_HEIGHT = 20


FPS = 60



pg.init()
screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
pg.display.set_caption("Creating maze layout")

position = pg.Vector2(10, 10)
clock = pg.time.Clock()


def main():
    brush = Brush(10, 10)
    speed = 50
    running = True
    brush_color = RED
    painting = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_PLUS and speed < 200:
                    speed += 5
                    print(f'speed {speed}')
                if event.key == pg.K_MINUS and speed > 0: 
                    speed -= 5
                    print(f'speed {speed}')
                if event.key == pg.K_RETURN: 
                    painting = not painting
                    brush_color = BLUE if painting else RED

                


        dt = clock.tick(FPS) / 1000

        x, y = brush.update(dt)
        
        screen.fill(WHITE)  # Fondo blanco
        pg.draw.rect(screen, brush_color, (x, y, BRUSH_WIDTH, BRUSH_HEIGHT))
        pg.display.update()

    pg.quit()




if __name__ == '__main__':
    main()
