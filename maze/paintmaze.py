import pygame as pg
import settings

# Configuraciones del laberinto
#WIDTH, HEIGHT = 20, 15  # Tamaño del laberinto en número de celdas
#CELL_SIZE = 40  # Tamaño de cada celda en píxeles
WALL = 1
PATH = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar Pygame
pg.init()
screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
pg.display.set_caption("Creating maze layout")
arrow_img = pg.image.load("res/images/arrow.png").convert_alpha()
print(arrow_img.get_size())
arrow_img = pg.transform.scale(arrow_img, (100, 100))
arrow_rect = arrow_img.get_rect()
arrow_rect.center = (10, 10)




def main():

# Bucle principal de Pygame
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                pass

        screen.fill(WHITE)  # Fondo blanco
      #  draw_maze()
      #  draw_player(player_x, player_y)
        screen.blit(arrow_img, arrow_rect)
        pg.display.update()

    pg.quit()




if __name__ == '__main__':
    main()
