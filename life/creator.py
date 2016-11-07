from collections import deque
import random

from pyglet import gl, graphics, clock
import numpy

from life import DENSITY, CELL_SIZE
from life.rules import BORN, SURVIVE


class Creator:

    def __init__(self, window):
        self._window = window
        self._window.push_handlers(self)
        self.width = window.width // CELL_SIZE
        self.height = window.height // CELL_SIZE
        self.field = self._get_empty_field()
        self._draw_queue = deque()
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                value = int(random.random() < DENSITY)
                self.field[x, y] = value
                self._draw_queue.append((x, y, value))
        clock.schedule_once(self._cycle, 0)

    def on_draw(self):
        while self._draw_queue:
            x, y, value = self._draw_queue.popleft()
            x0 = x * CELL_SIZE
            y0 = y * CELL_SIZE
            x1 = x0 + CELL_SIZE - 1
            y1 = y0 + CELL_SIZE - 1
            graphics.draw(
                4, gl.GL_QUADS,
                ('v2i', (x0, y0, x1, y0, x1, y1, x0, y1)),
                ('c3B', (0, 255 * value, 0) * 4))

    def _cycle(self, dt):
        new_field = self._get_empty_field()
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                value = self.field[x, y]
                mass = sum(sum(self.field[x - 1:x + 2, y - 1:y + 2])) - value
                new_value = value ^ (
                    ~ value & (mass in BORN) |
                    value & ~ (mass in SURVIVE))
                new_field[x, y] = new_value
                self._draw_queue.append((x, y, new_value))
        self.field = new_field
        clock.schedule_once(self._cycle, 0.1)

    def _get_empty_field(self):
        return numpy.zeros(
            shape=[self.width, self.height],
            dtype='int8')
