from pytube import YouTube
import os

def download_video(youtube_url, save_path, custom_filename):
    '''
    Function to download a YouTube video and save it with a custom filename in the specified folder (save_path).
    '''
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    
    # Determine the filename to use
    filename = custom_filename if custom_filename else stream.default_filename
    
    # Download the video
    stream.download(output_path=save_path, filename=filename)
    
    return filename

# Get YouTube link of Goomba Spotting (Mario Party Superstars Minigame)
youtube_url = 'https://www.youtube.com/watch?v=sqjTE_fo2Qc'

# Get the current working directory
save_path = os.getcwd()

# Define name of minigame
minigame = 'Goomba_Spotting'

# Custom filename for the downloaded video
custom_filename = minigame + '.mp4'

# Download the video with the custom filename
video_filename = download_video(youtube_url, save_path, custom_filename)