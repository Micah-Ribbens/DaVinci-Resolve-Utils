from math import ceil, floor

from auto_components.dimensions_wrapper import DimensionWrapper
from miscellaneous.important_variables import SCREEN_LENGTH, SCREEN_HEIGHT
from miscellaneous.utility_functions import get_measurement


class Grid(DimensionWrapper):
    rows = None
    columns = None
    dimensions = None
    length_buffer = get_measurement(SCREEN_LENGTH, 1)
    height_buffer = get_measurement(SCREEN_HEIGHT, 1)

    def __init__(self, dimensions, rows, columns):
        self.rows, self.columns = rows, columns

        if len(dimensions) != 4:
            raise ValueError(f"Expected 4 in the list, but got {len(dimensions)}. Dimensions most have all of these variables [left_edge, top_edge, length, height].")

        super().__init__(*dimensions)

    def set_dimensions(self, left_edge, top_edge, length, height):
        """Sets the dimensions of this object"""

        super().set_dimensions(left_edge, top_edge, length, height)

    def turn_into_grid(self, items, item_max_length, item_max_height):
        """Turns the items into a grid"""

        rows, columns = self.rows, self.columns
        number_of_items = len(items)

        if rows is None:
            rows = self.get_grid_dimension(columns, number_of_items)

        if columns is None:
            columns = self.get_grid_dimension(rows, number_of_items)

        item_height = self.get_item_dimension(self.height, rows, item_max_height, self.height_buffer)
        item_length = self.get_item_dimension(self.length, columns, item_max_length, self.length_buffer)

        base_left_edge = self.left_edge
        base_top_edge = self.top_edge

        for x in range(number_of_items):
            column_number = x % columns
            row_number = floor(x / columns)

            left_edge = base_left_edge + self.get_dimension_change(column_number, item_length, self.length_buffer)
            top_edge = base_top_edge + self.get_dimension_change(row_number, item_height, self.height_buffer)

            # Converting to int because tkinter doesn't accept decimals for GUI stuff
            items[x].place(x=int(left_edge), y=int(top_edge), width=int(item_length), height=int(item_height))

    def get_grid_dimension(self, other_dimension, number_of_items):
        """returns: int; the grid dimension (the amount of rows, or columns)"""

        return ceil(number_of_items / other_dimension)

    def get_item_dimension(self, grid_dimension_size, grid_dimension, item_dimension_max, buffer_between_items):
        """returns: double; the length or height of an item depending on whether the grid_dimension is rows or columns"""

        remaining_dimension = grid_dimension_size - buffer_between_items * (grid_dimension - 1)

        item_dimension = remaining_dimension / grid_dimension

        if item_dimension_max is not None and item_dimension > item_dimension_max:
            item_dimension = item_dimension_max

        return item_dimension

    def get_dimension_change(self, grid_dimension, item_dimension, buffer_between_items):
        """returns: double; the amount of change from the start of the grid to that grid item"""

        return grid_dimension * (item_dimension + buffer_between_items)