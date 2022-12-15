from tkinter import Toplevel


class MainPopupWindow(Toplevel):
    """ PopUpWindow that actually deals with the tkinter code (there can only be one pop up at a time)- this just
        changes what the PopUpWindow shows"""

    current_items = []

    length = 0
    height = 0

    def __init__(self, window, length, height, title):
        """Initializes the object"""

        super().__init__(window)
        self.geometry(f'{length}x{height}')
        self.title(title)

        self.length, self.height = length, height

    def show_items(self, items, show_items_function):
        """Shows the items on the screen and removes the items that were previously on the screen"""

        # Hides the other items
        for item in self.current_items:
            item.place(x=0, y=0, width=0, height=0)

        show_items_function()

        self.current_items = items