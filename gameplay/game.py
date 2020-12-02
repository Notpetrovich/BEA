import gameplay.gameobjects
import gameplay.world

class Game:
    def react(self, event):
        pass

    def __init__(self, canv, root):
        self.canv = canv
        self.root = root
        self.world = gameplay.world.World()
        react = lambda event: self.react(event)
        root.bind('<Key>', react , add='')  
        self.player = gameplay.gameobjects.Player()
        self.world.objects += [self.player]

    def draw_world(self):
        pass

    def draw_interface(self):
        pass
        
    def update(self, time):
        self.world.change(time)
        self.draw_world()
        self.draw_interface()
        return self
