import pygame as pg
import settings 


class Brush():
    def __init__(self, x=0, y=0, brush_width=20, brush_height=20):
        self.speed = 50
        self.painting = False
        self.position = pg.Vector2(x, y)
        self.brush_width = brush_width
        self.brush_height = brush_height

        
    def update(self, dt):
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
        
        x, y  = int(self.position.x), int(self.position.y)
        return x, y

