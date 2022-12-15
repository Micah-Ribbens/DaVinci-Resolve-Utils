from tkinter import Entry, Button, PhotoImage, Tk, OptionMenu, Menu, Frame, Label, Canvas, ttk

from miscellaneous.colors import *

SCREEN_LENGTH = 1280
SCREEN_HEIGHT = 620

BACKGROUND_COLOR = dark_gray

# Window
WINDOW = Tk()
WINDOW.configure(bg=BACKGROUND_COLOR)
WINDOW.title('Auto GUI')
WINDOW.geometry(f'{SCREEN_LENGTH}x{SCREEN_HEIGHT}')

# Fonts
FONT_NAME = "Arial"
MINISCULE_FONT = [FONT_NAME, 5]
TINY_FONT = [FONT_NAME, 8]
SMALL_FONT = [FONT_NAME, 11]
NORMAL_FONT = [FONT_NAME, 22]
LARGE_FONT = [FONT_NAME, 27]

# Field Inputs
DEFAULT_IMAGE_MARKER_COLOR = "Blue"
DEFAULT_CHAPTER_MARKER_COLOR = "Red"

FPS = 30









