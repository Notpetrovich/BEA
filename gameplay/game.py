import gameplay.gameobjects
import gameplay.world
import math

class Game:
    def __init__(self, canvas, root):
        self.canv = canvas
        self.root = root
        self.world = gameplay.world.World()
        self.root.bind('<Key>', self.react, add='')
        self.player = gameplay.gameobjects.Player(self.canv, [50, 50])
        self.enemy = gameplay.gameobjects.Enemy(self.canv, [100, 100])
        self.world.things.extend([self.player, self.enemy])

    def react(self, event):
        if str(event.type) == "w":
            self.player.step(math.pi / 2)

    def draw_world(self):
        self.canv.create_rectangle(10, 10, 190, 60, fill='yellow')

    def draw_interface(self):
        pass
        
    def update(self, time):
        self.root.bind('<Key>', self.react, add='')
        self.world.update(time)
        self.draw_world()
        self.draw_interface()
        return self
