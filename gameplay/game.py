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
        self.world = gameplay.world.World(wight_of_screen, height_of_screen)
        self.player = gameplay.gameobjects.Player(self.canv, self.root, [50, 50])
        self.enemy = gameplay.gameobjects.Enemy(self.canv, [100, 100])
        # self.world.active_things.extend([self.player, self.enemy])
        self.draw_world()
        self.pressed = False

    def react(self, event=tkinter.NONE):
        if self.pressed:
            self.canv.move("rect", 5, 0)
            self.root.after(50, self.react)

    def draw_world(self):
        pass

    def draw_interface(self):
        pass
        
    def update(self, time):
        # self.world.update(time)
        self.draw_interface()

        return self

    def give_param(self):
        return 'string'
