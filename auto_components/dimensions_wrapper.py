class DimensionWrapper:
    """Adds the ability to be able to get the right_edge, bottom_edge, horizontal_midpoint, and vertical_midpoints of GUI components"""

    left_edge = 0
    top_edge = 0
    length = 0
    height = 0

    def __init__(self, left_edge, top_edge, length, height):
        """Initializes the object"""

        self.left_edge, self.top_edge = left_edge, top_edge
        self.length, self.height = length, height

    def set_dimensions(self, left_edge, top_edge, length, height):
        """Sets the dimensions of this object"""

        self.left_edge, self.top_edge = left_edge, top_edge
        self.length, self.height = length, height

    # @property automatically changes this "attribute" when the left_edge or length changes
    # Can be treated as an attribute
    @property
    def right_edge(self):
        return self.left_edge + self.length

    @property
    def bottom_edge(self):
        return self.top_edge + self.height

    @property
    def horizontal_midpoint(self):
        return self.left_edge + self.length / 2

    @property
    def vertical_midpoint(self):
        return self.top_edge + self.height / 2