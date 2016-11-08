from pyglet import clock
import numpy

from life import DENSITY, WIDTH, HEIGHT, CYCLE_SLEEP
from life.rules import BORN, SURVIVE


class Creator:
    is_started = False

    def __init__(self, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height
        self.field = (
            numpy.random.rand(self.width, self.height) < DENSITY
        ).astype('int8')

    @property
    def flat(self):
        return self._flat()

    def start(self):
        self.is_started = True
        self._cycle()

    def stop(self):
        self.is_started = False

    def update(self, dt):
        new_field = numpy.fromfunction(
            numpy.vectorize(self._new_value),
            (self.width, self.height,),
            dtype='int8')
        self.field = new_field
        self._cycle()

    def _new_value(self, x, y):
        if x in (0, self.width - 1,):
            return 0

        if y in (0, self.height - 1,):
            return 0

        value = self.field[x, y]
        mass = sum(sum(self.field[x - 1:x + 2, y - 1:y + 2])) - value
        return value ^ (
            ~ value & (mass in BORN) |
            value & ~ (mass in SURVIVE))

    def _cycle(self):
        if self.is_started:
            clock.schedule_once(self.update, CYCLE_SLEEP)

    def _flat(self):
        f = self.field.flat
        while True:
            c = f.coords
            yield c[0], c[1], next(f)
