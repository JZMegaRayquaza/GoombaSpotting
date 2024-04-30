from moviepy.editor import VideoFileClip
import os

# Trim the video (get minigame portion)
start_time = 3  # Start time in seconds
end_time = 35   # End time in seconds

# Get the current working directory
save_path = os.getcwd()

# Define name of minigame
minigame = 'Goomba_Spotting'

# Define name of original downloaded video
video_filename = minigame + '.mp4'

# Construct the path to the downloaded video
video_path = os.path.join(save_path, video_filename)

# Get clip of video
clip = VideoFileClip(video_path).subclip(start_time, end_time)

# Write the trimmed video to the current directory
trimmed_video_path = os.path.join(save_path, minigame + '_trimmed.mp4')
clip.write_videofile(trimmed_video_path)