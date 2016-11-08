import pyglet

from life import WIDTH, HEIGHT, CELL_SIZE
from life.creator import Creator
from life.view import Field


creator = Creator(width=WIDTH, height=HEIGHT)
field = Field(field_creator=creator, cell_size=CELL_SIZE)

window = pyglet.window.Window(width=field.width, height=field.height)


@window.event
def on_draw():
    window.clear()
    field.draw()


creator.start()

pyglet.app.run()
