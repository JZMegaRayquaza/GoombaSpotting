from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

# Define name of minigame
minigame = 'Goomba_Spotting'

# Get cropped video to preprocess
video_path = minigame + '_cropped.mp4'

# Load video clip
video_clip = VideoFileClip(video_path)

# Convert to black and white
grayscale_clip = video_clip.fx(vfx.blackwhite)

# Write the processed video to file
grayscale_clip.write_videofile(minigame + '_grayscale.mp4', codec='libx264', fps=video_clip.fps)

# Close the clips
video_clip.close()
grayscale_clip.close()