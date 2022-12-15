from copy import deepcopy

from auto_components.grid import Grid


class GridItems:
    """Holds all the items that should be in a grid"""

    items = []

    # Dimensions are not important in this initialization
    horizontal_grid = Grid([0, 0, 0, 0], 1, None)
    vertical_grid = Grid([0, 0, 0, 0], None, 1)

    def __init__(self, items, grid):
        """Initializes the object"""

        self.items = items
        self.grid = deepcopy(grid)

    def place(self, **kwargs):
        """Places all the items at that location in a grid format"""

        self.grid.set_dimensions(kwargs.get("x"), kwargs.get("y"), kwargs.get("width"), kwargs.get("height"))
        self.grid.turn_into_grid(self.items, None, None)


