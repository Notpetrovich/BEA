from tkinter import *
import graphic
import gameplay.game
import os


class MenuPage:
    def __init__(self, canvas, root, numlines=1, time=0):
        self.canv = canvas
        self.root = root
        self.numlines = numlines
        self.current_line = 0
        self.go = -1
        self.time = time

    def react(self, event):
        if event.keysym == "Down":
            self.current_line += 1
            if self.current_line > self.numlines - 1:
                self.current_line = 0

        if event.keysym == "Up":
            self.current_line -= 1
            if self.current_line < 0:
                self.current_line = self.numlines - 1

        if event.keysym == "Return":
            self.go = self.current_line


class PausePage(MenuPage):
    def __init__(self, canvas, root):
        super().__init__(canvas, root, 3)
        self.root.bind('<Escape>', self.activation, add='')
        self.game = gameplay.game.Game(self.canv, self.root)
        self.state = False

    def update(self, time):
        if self.state:
            graphic.draw_pause_page(self.current_line)
            if self.go == 2:
                self.desactivation()
            elif self.go == 1:
                pass
                #for attributes in
            return self

        else:
            self.game.update(time)
            return self

    def activation(self, event=NONE):
        self.state = True
        self.root.bind('<Key>', NONE)
        self.root.bind('<Key>', self.react())
        self.root.bind('<Escape>', self.desactivation, add='')

    def desactivation(self, event=NONE):
        self.state = False
        self.root.bind('<Key>', NONE)
        self.root.bind('<Escape>', self.activation, add='')


class StartPage(MenuPage):
    def __init__(self, canvas, root):
        super().__init__(canvas, root, 4)
        react = lambda event: self.react(event)
        self.root.bind('<Key>', react, add='')
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
