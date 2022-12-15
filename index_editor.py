import csv
from datetime import timedelta

from miscellaneous.utility_functions import get_clip_frames, get_total_frames


class DavinciResolveIndexReader:
    """Reads the information from the file typed into the input"""

    start_marker_frame = 0

    def get_file_total_frames(self, file_path, total_video_time_code, image_marker_color):
        """returns: int[]; the frames for each picture"""

        csv_file = csv.DictReader(open(file_path))

        file_total_frames = []

        previous_timecode = None
        # displaying the contents of the CSV file
        for lines_dictionary in csv_file:
            current_time_code = lines_dictionary["Source In"]

            if lines_dictionary.get("Color") != image_marker_color:
                continue

            if previous_timecode is not None:
                file_total_frames.append(get_clip_frames(previous_timecode, current_time_code))


            else:
                self.start_marker_frame = get_total_frames(current_time_code)

            previous_timecode = current_time_code

        file_total_frames.append(get_clip_frames(previous_timecode, total_video_time_code))

        return file_total_frames

    def get_youtube_time_code(self, time_code):
        """returns: String; the 'time_code' that removes the information that is not needed for youtube"""

        time_code[1] = "0"

        return time_code[:7]

    def get_start_marker_frame(self):
        return self.start_marker_frame



davinci_resolve_index_reader = DavinciResolveIndexReader()
