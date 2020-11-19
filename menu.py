from tkinter import *
import graphic

class StartPage:
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


    def __init__(self, canv, root):
        self.canv = canv
        react = lambda event: self.react(event)
        root.bind('<Key>', react , add='')  
        self.current_line = 0
        self.go = -1
        self.timers = [0, 0]

    def update(self, time):
        for i in range(len(self.timers)):
            self.timers[i] -= time
            if self.timers[i] < 0:
                self.timers[i] = 0
        
        if self.timers[1] == 0:
            self.timers[1] = 10000

        if self.go  != -1:
            self.go = -1
            self.timers[0] = 3000

        graphic.draw_start_page(self.current_line, self.timers)
        return self
        


class Menu:
    def update(self, time):
        self.current_state = self.current_state.update(time)

    def __init__(self, canv, root):
        self.current_state = StartPage(canv, root)

    
