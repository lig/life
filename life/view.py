from pyglet import event, graphics, gl

from life import CELL_SIZE


LIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (0, 0, 0)


class Grid(dict):

    def __new__(cls, width, height, cell_size, dx=0, dy=0):

        def cell_data(x, y):
            x0 = x * cell_size + dx
            y0 = y * cell_size + dy
            x1 = x0 + cell_size - 1
            y1 = y0 + cell_size - 1
            return x0, y0, x1, y0, x1, y1, x0, y1

        return {
            (x, y): cell_data(x, y)
            for x in range(width)
            for y in range(height)
        }


class Field(event.EventDispatcher):

    def __init__(self, field_creator, cell_size=CELL_SIZE, dx=0, dy=0):
        self.width = field_creator.width * cell_size
        self.height = field_creator.height * cell_size
        self._grid = Grid(self.width, self.height, cell_size, dx, dy)
        self._creator = field_creator
        self._cell_size = cell_size

    def draw(self):
        grid = self._grid
        live = []
        dead = []

        for x, y, value in self._creator.flat:
            if value:
                live.extend(grid[x, y])
            else:
                dead.extend(grid[x, y])

        gl.glColor3ub(*LIVE_COLOR)
        graphics.draw(len(live) // 2, gl.GL_QUADS, ('v2i', live))

        gl.glColor3ub(*DEAD_COLOR)
        graphics.draw(len(dead) // 2, gl.GL_QUADS, ('v2i', dead))
