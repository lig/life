import pyglet

from life import WIDTH, HEIGHT, CELL_SIZE, DISPLAY_FPS, FULLSCREEN
from life.creator import Creator
from life.view import Field


creator = Creator(width=WIDTH, height=HEIGHT)

if FULLSCREEN:
    window = pyglet.window.Window(fullscreen=True)
    cell_size = min(window.width // WIDTH, window.height // HEIGHT)
    field = Field(
        field_creator=creator,
        cell_size=cell_size,
        dx=(window.width - WIDTH * cell_size) // 2,
        dy=(window.height - HEIGHT * cell_size) // 2)
else:
    field = Field(field_creator=creator, cell_size=CELL_SIZE)
    window = pyglet.window.Window(width=field.width, height=field.height)

if DISPLAY_FPS:
    fps_display = pyglet.window.FPSDisplay(window)
    fps_display.update_period = 1.

else:
    fps_display = None


@window.event
def on_draw():
    window.clear()
    field.draw()
    if fps_display:
        fps_display.draw()


creator.start()

pyglet.app.run()
