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


def update():
    '''
    updating game state and redrawing screen
    '''
    t = datetime.now()
    graphic.deleting()
    dt = (datetime.now() - t)
    dt = dt.microseconds/1000
    menu.update(dt)
    dt -= FPS
    if dt<0:
        dt = 0
    
    root.after(int(dt)+1, update)
    

update()
root.mainloop()
