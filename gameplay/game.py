import gameplay.gameobjects
import gameplay.world
import tkinter
import math


class Game:
    def __init__(self, canvas, root, wight_of_screen, height_of_screen):
        self.canv = canvas
        self.root = root
        self.weight = wight_of_screen
        self.height = height_of_screen
        # self.bar = tkinter.ttk.Progressbar(self.root, length=200)
        # self.bar['value'] = 70
        # self.bar.grid(column=0, row=0)
        # self.world = gameplay.world.World(wight_of_screen, height_of_screen)
        # self.player = gameplay.gameobjects.Player(self.canv, self.root, [50, 50])
        # self.enemy = gameplay.gameobjects.Enemy(self.canv, [100, 100])
        # self.world.active_things.extend([self.player, self.enemy])
        self.draw_world()

    def react(self, event=tkinter.NONE):
        pass

    def draw_world(self):
        pass

    def draw_interface(self):
        pass#self.bar['value'] = 50
        
    def update(self, time):
        # self.world.update(time)
        self.draw_interface()

        return self

    def give_param(self):
        return 'string'
