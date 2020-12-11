import tkinter as tk
import math


class GameObject(object):
    def __init__(self, canvas, tag, coords):
        self.canv = canvas
        self.tag = tag
        self.coords = coords
    
    def update(self):
        return self


class Player(GameObject):
    def __init__(self, canvas, tag="player", coords=[50, 50]):
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        x = self.coords[0]
        y = self.coords[1]
        k = 10
        self.canv.create_rectangle(
            x, y, x + k, y + 6*k,
            fill='green',
            outline='green',
            tag=self.tag
        )
    
    def step(self, direction, time):
        """
        direction is an angle in radians from the direction of right
        """
        disp = self.speed * time
        delta_x = math.cos(direction) * disp
        delta_y = math.sin(direction) * disp
        new_x = self.coords[0] + delta_x
        new_y = self.coords[1] + delta_y

        if new_x >= 1280 or new_x <= 0:
            new_x = self.coords[0]
        
        if new_y >= 720 or new_y <= 0:
            new_y = self.coords[1]
        
        self.coords = [new_x, new_y]
        self.canv.move(self.tag, new_x, new_y)
    
    def attack(self):
        pass


class Enemy(GameObject):
    def __init__(self, canvas, tag="enemy", coords=[50, 50]):
        super().__init__(canvas, tag, coords)
