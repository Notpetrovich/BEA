import tkinter
import math


# abstract class (using in this module only)
class ActiveObject(object):
    def __init__(self, canvas, tag, coords):
        self.canv = canvas
        self.tag = tag
        self.coords = coords
    
    def update(self):
        return self

    def draw_self(self):
        pass


class Player(ActiveObject):
    def __init__(self, canvas, root, coords=[150, 150], tag="player"):
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        self.root = root
        self.root.bind('<KeyPress-space>', self.pressing)
        self.root.bind('<KeyRelease-space>', self.unpressing)
        self.pressed = False
        x = self.coords[0]
        y = self.coords[1]
        k = 100
        self.id = self.canv.create_rectangle(
            x, y, x + k, y + 2*k,
            fill='red',
            outline='green',
            tag=self.tag
        )

    def pressing(self, event=tkinter.NONE):
        if not self.pressed:
            self.pressed = True
            self.step()

    def unpressing(self, event=tkinter.NONE):
        self.pressed = False

    def step(self, event=tkinter.NONE):
        if self.pressed:
            self.canv.move(self.tag, 5, 0)
            self.root.after(50, self.step)
    
    def attack(self):
        pass


class Enemy(ActiveObject):
    def __init__(self, canvas, coords=[50, 50], tag="enemy"):
        super().__init__(canvas, tag, coords)
