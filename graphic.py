from tkinter import *

class Aggregator(object):
    canv = None
    figures = []
    old_figures = []
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Aggregator, cls).__new__(cls)
        return cls.instance

    def add(self, figure):
        self.figures += [figure]

    def __init__(self):
        pass
        

def redraw():
    ag = Aggregator()
    
    for fig in ag.old_figures:
        ag.canv.delete(fig)
    
    ag.old_figures = ag.figures
    ag.figures = []
    
    
def draw_start_page(current_line, timers):
    ag = Aggregator()
    canv = ag.canv
    c = ["#8080FF"]*4
    c[current_line] = "#FF30FF"
    ag.add(canv.create_text(640, 100, text="BEA", justify=CENTER, font="Impact 100", fill="#FF8000"))
    ag.add(canv.create_text(640, 300, text="Новая игра", justify=CENTER, font="Impact 40", fill=c[0]))
    ag.add(canv.create_text(640, 350, text="Загрузить игру", justify=CENTER, font="Impact 40", fill=c[1]))
    ag.add(canv.create_text(640, 400, text="Настройки", justify=CENTER, font="Impact 40", fill=c[2]))
    ag.add(canv.create_text(640, 450, text="Выход", justify=CENTER, font="Impact 40", fill=c[3]))
    if timers[0] > 0:
        ag.add(canv.create_text(200, 70, text="Прикол пока не реализован  :<", justify=CENTER, font="Impact 16", fill="#FF2060"))

    
