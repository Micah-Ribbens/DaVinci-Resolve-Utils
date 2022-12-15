from index_editor import davinci_resolve_index_reader


class FileWriter:
    """Writes the file for DaVinci Resolve"""

    all_picture_frame_durations = ""
    number_of_pictures = ""
    main_clip_name = ""
    start_marker_frame = ""
    pictures_clip_number_of_frames = ""

    def __init__(self, all_picture_frame_durations, number_of_pictures, main_clip_name, start_marker_frame,
                 pictures_clip_number_of_frames):

        """Initializes the object"""

        self.all_picture_frame_durations, self.number_of_pictures = all_picture_frame_durations, number_of_pictures
        self.main_clip_name = main_clip_name
        self.start_marker_frame, self.pictures_clip_number_of_frames = start_marker_frame, pictures_clip_number_of_frames

    def get_file_start_and_end_frames(self):
        """returns: String[][] {frame_starts, frame_ends}; the numbers for the starts and ends of the frames as reperesented by strings"""

        previous_frame_start = 0
        main_clip_picture_duration = int(self.pictures_clip_number_of_frames / self.number_of_pictures)
        frame_starts = [0]
        frame_ends = []

        for picture_frame_duration in self.all_picture_frame_durations:
            frame_end = picture_frame_duration + previous_frame_start
            frame_ends.append(frame_end)

            # Because the next frame's start is the previous frame's end + the main_clip_picture_duration
            # Also frame_starts has a start value of 0, so that must be accounted for
            if len(frame_starts) != self.number_of_pictures:
                previous_frame_start += main_clip_picture_duration
                frame_starts.append(previous_frame_start)

        # Can't return all the frame_ends because there is one that is an extraneous value
        return [str(frame_starts), str(frame_ends)]


    def get_file_contents(self):
        """returns: String; the start of the file"""

        file_starts, file_ends = self.get_file_start_and_end_frames()


        return f'''
-- Gets Everything that is needed from resolve
resolve = Resolve()
projectManager = resolve:GetProjectManager()
project = projectManager:GetCurrentProject()
mediaPool = project:GetMediaPool()
rootFolder = mediaPool:GetRootFolder()
clips = rootFolder:GetClips()
mainClipName = "{self.main_clip_name}"
-- Needed because lists in lua don't use []
frameStarts = {"{"+file_starts[1:len(file_starts) - 1]+"}"}
frameEnds = {"{"+file_ends[1:len(file_ends) - 1]+"}"}
maxIndex = {self.number_of_pictures}

-- Gets the Main Clip
for clipIndex in pairs(clips) do
  clip = clips[clipIndex]''' + '''
  if clip:GetName() == mainClipName then
    
    for index = 0,maxIndex,1 do 
        subClip = {}
        subClip["mediaPoolItem"] = clip
        subClip["startFrame"] = frameStarts[index]
        subClip["endFrame"] = frameEnds[index]
    
        if mediaPool:AppendToTimeline({ subClip }) then
          print("added clip to time line")
        end
    end
  end
end
'''

    def write_file(self, file):
        """Writes the file"""

        file.write(self.get_file_contents())



