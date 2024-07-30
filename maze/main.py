import pygame as pg 
import maze.settings as settings 


class Game: 
    def __init__(self):
        pg.init()
        pg.display.set_caption(settings.CAPTION)
        self.display = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pg.time.Clock()
    
    def run(self):
        done = False
        while not done: 
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    done = True
            dt = self.clock.tick(settings.FPS)
            pg.display.update()

    pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()