from tkinter import *
import graphic
import gameplay.game


class MenuPage:
    def __init__(self, canvas, root):
        self.canv = canvas
        self.root = root
        self.current_line = 0
        self.go = -1

    def react(self, event):
        if event.keysym == "Down":
            self.current_line += 1
            if self.current_line > 3:
                self.current_line = 0

        if event.keysym == "Up":
            self.current_line -= 1
            if self.current_line < 0:
                self.current_line = 3

        if event.keysym == "Return":
            self.go = self.current_line


class PausePage(MenuPage):
    def __init__(self, canvas, root):
        super().__init__(canvas, root)
        activation = lambda event: self.activation(event)
        self.canv.bind('<Escape>', activation, add='')
        self.game = gameplay.game.Game(self.canv, self.root)
        self.state = False

    def update(self):
        if self.state:
            pass

        else:
            pass

    def activation(self):
        self.state = True
        reaction = lambda event: self.react(event)
        self.canv.bind('<Key>', reaction)
        desactivation = lambda event: self.desactivation(event)
        self.canv.bind('<Escape>', desactivation, add='')

    def desactivation(self):
        self.state = False
        self.canv.bind('<Key>', NONE)
        activation = lambda event: self.activation(event)
        self.canv.bind('<Escape>', activation, add='')


class StartPage(MenuPage):
    def __init__(self, canvas, root):
        super().__init__(canvas, root)
        react = lambda event: self.react(event)
        root.bind('<Key>', react, add='')
        self.timers = [0, 0]

    def update(self, time):
        for i in range(len(self.timers)):
            self.timers[i] -= time
            if self.timers[i] < 0:
                self.timers[i] = 0
        
        if self.timers[1] == 0:
            self.timers[1] = 10000

        if not self.go == -1:
            if self.go == 3:
                self.root.quit()
            
            if self.go == 0:
                pause_page = PausePage(self.canv, self.root)
                return pause_page
            
            self.go = -1
            self.timers[0] = 3000

        graphic.draw_start_page(self.current_line, self.timers)
        return self
        

class Menu:
    def __init__(self, canv, root):
        self.current_state = StartPage(canv, root)

    def update(self, time):
        self.current_state = self.current_state.update(time)