from miscellaneous.important_variables import *
from datetime import timedelta


def get_measurement(unit_of_measurement, amount):
    return unit_of_measurement / 100 * amount


def get_mouse_position():
    """returns: int[2] {mouse_left_edge, mouse_top_edge}; the mouse's position on the screen"""

    return [WINDOW.winfo_pointerx() - WINDOW.winfo_rootx(),
            WINDOW.winfo_pointery() - WINDOW.winfo_rooty()]

def get_lines(string):
    """returns: String[]; the lines contained within that string (each '/n' creates a new line). Every item in the list is a line"""

    current_line = ""
    lines = []
    enter = "\n"

    for ch in string:
        if ch == enter:
            lines.append(current_line)
            current_line = ""

        else:
            current_line += ch

    return lines + [current_line]  # The last line doesn't have an enter at the end, so adding that line here


def truncate(number, decimal_places):
    """returns: number; the number to that many decimal places (it removes the other decimal places)"""

    # Getting the whole number with the decimals removed (to accuracy of decimal places) then making it go back
    # To the original decimal by dividing by 10^decimal_places
    return (number * pow(10, decimal_places) // 1) / pow(10, decimal_places)


def get_next_index(max_index, current_index):
    """returns: int; the next index after the 'current_index' and it does cycle 0 -> max_index -> 0 -> etc."""

    next_index = current_index + 1
    return next_index if next_index <= max_index else 0  # If the index is too big it should go back to 0


def get_previous_index(current_index):
    """returns: int; the previous index after the 'current_index' and it does cycle max_index -> 0 -> max_index -> etc."""

    return max(0, current_index - 1)  # The index should be at minimum 0


def swap_list_items(items, index1, index2):
    """Swaps the two indexes, so items[index1] = items[index2] and items[index2] = items[index1]"""

    temporary_item = items[index2]
    items[index2] = items[index1]
    items[index1] = temporary_item


def get_total_frames(time_code):
    """returns: int; the start frame of the first chapter"""

    hours, minutes, seconds, milliseconds = get_time_code_components(time_code)
    time_delta = timedelta(days=0, hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

    # Used
    subtracting_time_delta = timedelta(days=0, hours=0, minutes=0, seconds=0, milliseconds=0)
    end_time_delta = time_delta - subtracting_time_delta

    return int(end_time_delta.total_seconds() * FPS)

def get_clip_frames(previous_time_code, current_time_code):
    """returns: double; the duration of the clip"""

    previous_hours, previous_minutes, previous_seconds, previous_milliseconds = get_time_code_components(previous_time_code)
    current_hours, current_minutes, current_seconds, current_milliseconds = get_time_code_components(current_time_code)

    previous_time_delta = timedelta(days=0, hours=previous_hours, minutes=previous_minutes, seconds=previous_seconds, milliseconds=previous_milliseconds)
    current_time_delta = timedelta(days=0, hours=current_hours, minutes=current_minutes, seconds=current_seconds, milliseconds=current_milliseconds)
    end_time_delta = current_time_delta - previous_time_delta
    return int(end_time_delta.total_seconds() * FPS)

def get_time_code_components(time_code):
    """returns: int[] {hours, minutes, seconds, milliseconds}; the components in the time code- 00:05:03:20"""
    return_value = [
        int(time_code[0:2]) - 1,
        int(time_code[3:5]),
        int(time_code[6:8]),
        int(time_code[9:11])
    ]
    return return_value





