import random

from pyglet import gl, graphics, clock
import numpy

from life import DENSITY, CELL_SIZE


class Creator:

    def __init__(self, window):
        self._window = window
        self._window.push_handlers(self)
        self.width = window.width // CELL_SIZE
        self.height = window.height // CELL_SIZE
        self.field = numpy.empty(
            shape=[self.width, self.height],
            dtype=int)
        for y in range(self.height):
            for x in range(self.width):
                self.field[x, y] = int(random.random() < DENSITY)

    def on_draw(self):
        self._window.clear()
        gl.glColor3ub(0, 255, 0)
        for y in range(self.height):
            for x in range(self.width):
                if self.field[x, y]:
                    x0 = x * CELL_SIZE
                    y0 = y * CELL_SIZE
                    x1 = x0 + CELL_SIZE - 1
                    y1 = y0 + CELL_SIZE - 1
                    graphics.draw(
                        4, gl.GL_QUADS,
                        ('v2i', (x0, y0, x1, y0, x1, y1, x0, y1)))
        clock.schedule_once(self._cycle, 0)

    def _cycle(self, dt):
        new_field = numpy.empty(
            shape=[self.width, self.height],
            dtype='int8')
        for y in range(self.height):
            for x in range(self.width):
                mass = sum(self.field[x - 1:x + 2:2, y - 1:y + 2:2].flatten())
                if self.field[x, y] and mass not in (2, 3,):
                    new_field[x, y] = 0
                elif not self.field[x, y] and mass == 3:
                    new_field[x, y] = 1
                else:
                    new_field[x, y] = self.field[x, y]
        self.field = new_field
