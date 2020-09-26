from graphics import *
from random import randint


def grid():
    w = 600
    h = 600
    win = GraphWin("grid", w, h)
    win.setBackground(color_rgb(0, 0, 0))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 0)

    # ciclo para verticales
    for x in range(0, w, 30):
        xa = Line(Point(x, 0), Point(x, h))
        xa.setOutline(color_rgb(r, g, b))
        xa.draw(win)

    # ciclo para horizontales
    for y in range(0, h, 30):
        ya = Line(Point(0, y), Point(w, y))
        ya.setOutline(color_rgb(r, g, b))
        ya.draw(win)
    print(r, g, b)
    win.getMouse()
    win.close()


grid()
