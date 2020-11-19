from tkinter import *
import time

root = Tk()
root.geometry('1280x720')
root.resizable(False, False)
root.title("BEA")
root.config(cursor="none")
canv = Canvas(width=1280, height=720, bg='green', highlightthickness=0)
canv.pack()   

root.mainloop()
