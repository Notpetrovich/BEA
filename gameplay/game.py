import gameplay.gameobjects
import gameplay.world
import math

class Game:
    def __init__(self, canvas, root):
        self.canv = canvas
        self.root = root
        self.world = gameplay.world.World()
        self.root.bind('<Return>', self.react, add='+')
        self.player = gameplay.gameobjects.Player(self.canv, [50, 50])
        self.enemy = gameplay.gameobjects.Enemy(self.canv, [100, 100])
        self.world.things.extend([self.player, self.enemy])
        self.draw_world()

    def react(self, event, time):
        #if str(event.type) == 'w':
        self.player.step(math.pi / 2)
        self.canv.create_rectangle(
            300, 100, 300 + 50, 100 + 30,
            fill='red',
            outline='green',
        )

    def draw_world(self):
        self.canv.create_rectangle(10, 10, 190, 60, fill='yellow')

    def draw_interface(self):
        pass
        
    def update(self, time):
        # react = lambda event, time: self.react(event, time)
        #self.root.bind('<Return>', self.react, add='')
        self.world.update(time)
        self.draw_interface()
        self.player.step(0, 1)

        return self
