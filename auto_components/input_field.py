from miscellaneous.important_variables import *


class InputField(Entry):
    """ Extends tkinter's class Entry. It adds the functionality of more easily setting the text, adding default text, and
        only allowing editing when the InputField is editable"""

    is_selected = False
    belongs_to = None
    is_editable = True
    command = None

    def __init__(self, window_type, font, default_text, is_editable=True):
        """Initializes the object"""

        super().__init__(window_type, font=font)

        self.insert(0, default_text) # Puts this text at the start of the Input Field (Default Text)

        if not is_editable:
            self.configure(fg=white, bg=black)

        self.is_editable = is_editable

    def set_text(self, text):
        """Sets the text of the InputField to the value provided if the InputField is editable"""

        if self.is_editable:
            self.delete(0, "end")
            self.insert(0, text)

    def get_text(self):
        return self.get()

    def set_is_selected(self, is_selected):
        self.is_selected = is_selected

    def get_is_selected(self):
        """returns: boolean; if the input field is selected"""

        return self.is_selected

    def set_command(self, command):
        """Sets the function that is called when the input field is clicked"""

        self.bind("<1>", lambda event: command(self))
        self.command = command

    def set_belongs_to(self, belongs_to):
        """Sets the MovablePoint (like ControlPoint) the InputField is belongs to"""

        self.belongs_to = belongs_to

    def get_belongs_to(self):
        """returns: MovablePoint; the MovablePoint (like ControlPoint) the InputField belongs to"""

        return self.belongs_to



