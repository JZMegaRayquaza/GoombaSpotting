import moviepy.editor as mpy
from moviepy.video.fx.all import crop

# Define name of minigame
minigame = 'Goomba_Spotting'

# Get trimmed video to crop
video_path = minigame + '_trimmed.mp4'
clip = mpy.VideoFileClip(video_path)

# Get width and height of video
(w, h) = clip.size

# Get region of interest
cropped_clip = crop(clip, width=180, height=280, x_center=w/2, y_center=h/2)
cropped_clip.write_videofile(minigame + '_cropped.mp4')