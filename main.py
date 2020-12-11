from tkinter import *
from datetime import datetime
import menu
import graphic

FPS = 40
wight_of_screen = 1280
height_of_screen = 720

root = Tk()
root.geometry('1280x720')
root.resizable(False, False)
root.title("BEA")
root.config(cursor="none")
canv = Canvas(
    width=wight_of_screen,
    height=height_of_screen,
    bg='green',
    highlightthickness=0
)
canv.pack()
ag = graphic.Aggregator()
ag.canv = canv
menu = menu.Menu(canv, root)
t = datetime.now()
menu.time = t


def update():
    '''
    updating game state and redrawing screen
    '''
    dt = (datetime.now() - menu.time)
    dt = dt.microseconds / 1000
    menu.time = datetime.now()
    menu.update(dt)
    dt -= FPS
    if dt < 0:
        dt = 0
    graphic.rubbing()

    root.after(int(dt) + 1, update)


update()
root.mainloop()
