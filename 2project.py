from tkinter import Tk, Canvas, Frame, BOTH
import math


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Рисуем человека")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        def body(x, y, k):
            canvas.create_rectangle(
                x - k, y + 2*k, x + k, y + 6*k,
                fill='green', outline='green'
            )
            canvas.create_oval(
                x - 4 * k, y - 4 * k, x + 4 * k, y + 4 * k,
                fill='green', outline='green'
            )
            canvas.create_polygon(
                x -3*k, y + 18*k, x - 6*k, y + 8*k,
                x - k, y + 6*k, x + k, y + 6*k,
                x + 6*k, y + 8*k, x + 3*k, y + 18*k,
                fill='green', outline='green'
            )
        def right_hand(x, y, k, alpha_right):
            canvas.create_polygon(
                x - 6*k, y + 8*k,
                x - 6*k + 2*k*math.cos(alpha_right), y + 8*k + 2*k*math.sin(alpha_right),
                x - 6*k - 18*k*math.sin(alpha_right) + 2*k*math.cos(alpha_right),
                y + 8*k + 18*k*math.cos(alpha_right)+ 2*k*math.sin(alpha_right),
                x - 6*k - 18*k*math.sin(alpha_right),  y + 8*k + 18*k*math.cos(alpha_right),
                fill='green', outline='green'
            )
        def left_hand(x, y, k, alpha_left):
            canvas.create_polygon(
                x + 6 * k, y + 8 * k,
                x + 6 * k - 2 * k * math.cos(alpha_left), y + 8 * k + 2 * k * math.sin(alpha_left),
                x + 6 * k + 18 * k * math.sin(alpha_left) - 2 * k * math.cos(alpha_left),
                y + 8 * k + 18 * k * math.cos(alpha_left) + 2 * k * math.sin(alpha_left),
                x + 6 * k + 18 * k * math.sin(alpha_left), y + 8 * k + 18 * k * math.cos(alpha_left),
                fill='green', outline='green'
            )
        def right_leg(x, y, k, beta_right):
            canvas.create_polygon(
                x - 4 * k, y + 16 * k,
                x - 4 * k + 4 * k * math.cos(beta_right), y + 16 * k + 4 * k * math.sin(beta_right),
                x - 4 * k - 24 * k * math.sin(beta_right) + 4 * k * math.cos(beta_right),
                y + 16 * k + 24 * k * math.cos(beta_right) + 4 * k * math.sin(beta_right),
                x - 4 * k - 24 * k * math.sin(beta_right), y + 16 * k + 24 * k * math.cos(beta_right),
                fill='green', outline='green'
            )
        def left_leg(x, y, k, beta_left):
            canvas.create_polygon(
                x + 4 * k, y + 16 * k,
                x + 4 * k - 4 * k * math.cos(beta_left), y + 16 * k + 4 * k * math.sin(beta_left),
                x + 4 * k + 24 * k * math.sin(beta_left) - 4 * k * math.cos(beta_left),
                y + 16 * k + 24 * k * math.cos(beta_left) + 4 * k * math.sin(beta_left),
                x + 4 * k + 24 * k * math.sin(beta_left), y + 16 * k + 24 * k * math.cos(beta_left),
                fill='green', outline='green'
            )

        right_hand(50, 50, 10, 0.1)
        left_hand(50, 50, 10, 0.4)
        right_leg(50, 50, 10, 0.2)
        left_leg(50, 50, 10, 0.3)
        body(50, 50, 10)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()