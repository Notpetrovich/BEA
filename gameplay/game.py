import gameplay.gameobjects
import gameplay.world

class Game:
    def __init__(self, canv, root):
        self.canv = canv
        self.root = root
        self.world = gameplay.world.World()
        react = lambda event: self.react(event)
        self.root.bind('<Key>', react, add='')
        self.player = gameplay.gameobjects.Player()
        self.enemy = gameplay.gameobjects.Enemy()
        self.world.objects.extend([self.player, self.enemy])

    def react(self, event):
        pass

    def draw_world(self):
        pass

    def draw_interface(self):
        pass
        
    def update(self, time):
        react = lambda event: self.react(event)
        self.root.bind('<Key>', react, add='')
        self.world.change(time)
        self.draw_world()
        self.draw_interface()
        return self
