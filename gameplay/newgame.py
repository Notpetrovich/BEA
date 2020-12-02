import gameplay.game
import gameplay.gameobjects
import gameplay.world

class NewGame:
    def __init__(self, canv, root):
        self.canv = canv
        self.root = root
        
    def update(self, time):
        current_game = gameplay.game.Game(self.canv, self.root)
        return current_game
