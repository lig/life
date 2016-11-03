from pyglet.window import Window
import pyglet

from life import WIDTH, HEIGHT
from life.creator import Creator


window = Window(width=WIDTH, height=HEIGHT)
creator = Creator(window)


pyglet.app.run()
