
-- Gets Everything that is needed from resolve
resolve = Resolve()
projectManager = resolve:GetProjectManager()
project = projectManager:GetCurrentProject()
mediaPool = project:GetMediaPool()
rootFolder = mediaPool:GetRootFolder()
clips = rootFolder:GetClips()
mainClipName = "Main3"
-- Needed because lists in lua don't use []
frameStarts = {0, 1498, 2996, 4494, 5992, 7490, 8988, 10486, 11984, 13482, 14980, 16478, 17976, 19474, 20972, 22470, 23968, 25466}
frameEnds = {150, 1798, 3085, 4614, 6322, 7789, 9198, 10665, 12223, 13572, 15040, 16687, 18126, 19624, 21032, 22799, 24148, 25855}
maxIndex = 18

-- Gets the Main Clip
for clipIndex in pairs(clips) do
  clip = clips[clipIndex]
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
