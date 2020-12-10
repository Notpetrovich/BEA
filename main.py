from tkinter import *
from datetime import datetime
import menu
import graphic

FPS = 40

root = Tk()
root.geometry('1280x720')
root.resizable(False, False)
root.title("BEA")
root.config(cursor="none")
canv = Canvas(width=1280, height=720, bg='green', highlightthickness=0)
canv.pack()
ag = graphic.Aggregator()
ag.canv = canv
menu = menu.Menu(canv, root)
t = datetime.now()


def update():
    '''
    updating game state and redrawing screen
    '''
    global t
    dt = (datetime.now() - t)
    dt = dt.microseconds / 1000
    t = datetime.now()
    menu.update(dt)
    dt -= FPS
    if dt < 0:
        dt = 0
    graphic.rubbing()

    root.after(int(dt) + 1, update)
    

update()
root.mainloop()
