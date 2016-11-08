import pyglet

from life import WIDTH, HEIGHT, CELL_SIZE, DISPLAY_FPS
from life.creator import Creator
from life.view import Field


creator = Creator(width=WIDTH, height=HEIGHT)
field = Field(field_creator=creator, cell_size=CELL_SIZE)

window = pyglet.window.Window(width=field.width, height=field.height)
fps_display = pyglet.clock.ClockDisplay()


@window.event
def on_draw():
    window.clear()
    field.draw()
    if DISPLAY_FPS:
        fps_display.draw()


creator.start()

pyglet.app.run()
