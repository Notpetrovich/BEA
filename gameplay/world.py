import gameplay.gameobjects

class World(object):
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(World, cls).__new__(cls)
    #     return cls.instance
    
    def __init__(self):
        self.things = []

    def update(self, time):
        pass
        # for thing in self.things:
        #     thing.update()
