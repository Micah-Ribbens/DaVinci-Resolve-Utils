from auto_components.grid import Grid
from auto_components.grid_items import GridItems
from auto_components.input_field import InputField


class TitledInputField:
    """An input field that is titled"""

    grid = None
    title_field = None
    input_field = None

    def __init__(self, window_type, font, input_field_default_text, title_field_text):
        """Initializes the object"""

        self.title_field = InputField(window_type, font, title_field_text, False)
        self.input_field = InputField(window_type, font, input_field_default_text, True)

        self.grid = GridItems.vertical_grid

    def place(self, **kwargs):
        """Changes the position of the this object (x, y, width, height)"""

        self.grid.set_dimensions(kwargs.get("x"), kwargs.get("y"), kwargs.get("width"), kwargs.get("height"))
        self.grid.turn_into_grid([self.title_field, self.input_field], None, None)


    def set_text(self, text):
        """Sets the text of the InputField to the value provided if the InputField is editable"""

        self.input_field.set_text(text)

    def set_title(self, title):
        """Sets the title of the title InputField"""

        self.title_field.set_text(title)

    def get_text(self):
        return self.input_field.get()

