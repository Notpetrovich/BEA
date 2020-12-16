import tkinter
import math


class GameObject(object):
    def __init__(self, canvas, tag, coords):
        self.canv = canvas
        self.tag = tag
        self.coords = []
        self.coords = coords
        self.coords = coords
    
    def update(self):
        return self


class Player(GameObject):
    def __init__(self, canvas, tag="player", coords=[150, 150]):
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        x = self.coords[0]
        y = self.coords[1]
        k = 100
        self.canv.create_rectangle(
            x, y, x + k, y + 2*k,
            fill='red',
            outline='green',
            tag=self.tag
        )
    
    def step(self, direction, time=5):
        """
        direction is an angle in radians from the direction of right
        """
        dist = self.speed * time
        delta_x = int(math.cos(direction) * dist)
        delta_y = int(math.sin(direction) * dist)
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
