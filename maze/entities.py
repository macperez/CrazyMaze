import pygame as pg
import settings 
import numpy as np


class Matrix(): 
    def __init__(self, dimensions):
        self.maze_matrix = np.zeros(dimensions)
    def turnon(self, posx, posy):
        self.maze_matrix[posx, posy] = 1
    def turnoff(self, posx, posy):
        self.maze_matrix[posx, posy] = 0



class Brush():

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __init__(self, x=0, y=0, brush_width=20, brush_height=20):
        self.speed = 50
        self.painting = False
        self.position = pg.Vector2(x, y)
        self.brush_width = brush_width
        self.brush_height = brush_height
        self.brush_color = Brush.RED 
        self.posx = x 
        self.posy = y

    
    def listen_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_PLUS and self.speed < 200:
                self.speed += 5
                print(f'speed {self.speed}')
            if event.key == pg.K_MINUS and self.speed > 0: 
                self.speed -= 5
                print(f'speed {self.speed}')
            if event.key == pg.K_RETURN: 
                print('Change mode')
                self.painting = not self.painting
                self.set_color(Brush.BLUE) if self.painting else self.set_color(Brush.RED)
                self.set_color(Brush.BLUE) if self.painting else self.set_color(Brush.RED)

    def update(self, dt, matrix):       
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] :
            self.position.x -=  self.speed * dt
            if self.position.x < 0:
                self.position.x = 0  
        elif keys[pg.K_RIGHT]:
            self.position.x +=  self.speed * dt
            if self.position.x > settings.WIDTH - self.brush_width:
                self.position.x = settings.WIDTH - self.brush_width  
        elif keys[pg.K_UP]:
            self.position.y -=  self.speed * dt
            if self.position.y < 0:
                self.position.y = 0
        elif keys[pg.K_DOWN]:
            self.position.y +=  self.speed * dt
            if self.position.y > settings.HEIGHT - self.brush_height:
                self.position.y = settings.HEIGHT - self.brush_height
        self.posx, self.posy  = int(self.position.x), int(self.position.y)
        if self.painting: 
            matrix.turnon(self.posx, self.posy)
            

    def set_color(self, color):
        self.brush_color = color

    def paint(self, screen):
        pg.draw.rect(screen, self.brush_color, (self.posx, self.posy, self.brush_width, self.brush_height))
        


