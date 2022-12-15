import os
import tkinter

from auto_components.grid_items import GridItems
from auto_components.input_field import InputField
from auto_components.titled_input_field import TitledInputField

from tkinter import filedialog

from tkinter import *
from auto_components.grid import Grid
from file_writer import FileWriter

from miscellaneous.utility_functions import *
from index_editor import davinci_resolve_index_reader


class MainScreen:
    """The Main Screen of the application"""

    image_marker_color_field = TitledInputField(WINDOW, NORMAL_FONT, DEFAULT_IMAGE_MARKER_COLOR, "Image Marker Color")
    chapter_marker_color_field = TitledInputField(WINDOW, NORMAL_FONT, DEFAULT_CHAPTER_MARKER_COLOR, "Chapter Marker Color")
    number_of_pictures_field = TitledInputField(WINDOW, NORMAL_FONT, "", "Number Of Pictures")
    pictures_clip_total_time_field = TitledInputField(WINDOW, NORMAL_FONT, "", "Pictures Clip Total Time")
    main_video_total_time = TitledInputField(WINDOW, NORMAL_FONT, "", "Main Video Total Time")
    main_clip_name_field = TitledInputField(WINDOW, NORMAL_FONT, "Main3", "Main Clip Name Field")
    indexes_file_path_field = TitledInputField(WINDOW, NORMAL_FONT, "all_indexes.csv", "Indexes File Path")

    all_fields = [image_marker_color_field, chapter_marker_color_field, number_of_pictures_field,
                  pictures_clip_total_time_field, main_clip_name_field, indexes_file_path_field, main_video_total_time]

    fields_frame_height = get_measurement(SCREEN_HEIGHT, 80)
    save_button_height = SCREEN_HEIGHT - fields_frame_height
    save_button_length = SCREEN_LENGTH

    save_file_button = Button(WINDOW, compound=tkinter.CENTER, text="Save File", bg=pleasing_green, fg=white, font=NORMAL_FONT)

    def __init__(self):
        """Initializes the application"""

        grid = Grid([0, 0, SCREEN_LENGTH, self.fields_frame_height], None, 3)
        grid.turn_into_grid(self.all_fields, None, None)
        self.save_file_button.place(x=0, y=self.fields_frame_height, width=self.save_button_length, height=self.save_button_height)
        self.save_file_button.configure(command=self.save_file)

    def save_file(self):
        """Saves the file"""

        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        pictures_total_time_code = self.pictures_clip_total_time_field.get_text()
        main_video_total_time_code = self.main_video_total_time.get_text()
        pictures_clip_number_of_frames = get_total_frames(pictures_total_time_code)
        indexes_file_path = self.indexes_file_path_field.get_text()
        image_marker_color = self.image_marker_color_field.get_text()
        all_picture_frame_durations = davinci_resolve_index_reader.get_file_total_frames(indexes_file_path, main_video_total_time_code, image_marker_color)

        number_of_pictures = int(self.number_of_pictures_field.get_text())
        main_clip_name = self.main_clip_name_field.get_text()
        start_marker_frame = davinci_resolve_index_reader.get_start_marker_frame()

        file_writer = FileWriter(all_picture_frame_durations, number_of_pictures, main_clip_name,
                                 start_marker_frame, pictures_clip_number_of_frames)

        file_writer.write_file(file)


