from moviepy.editor import VideoFileClip, AudioFileClip

# Load your video
video = VideoFileClip('my_video.mp4')

# Export audio from the video
video.audio.write_audiofile('my_extracted_audio.mp3')

# Load your new audio file
new_audio = AudioFileClip('my_new_audio.mp3')

# Ensure audio is long enough for video - this will loop the audio if the video is longer.
if video.duration > new_audio.duration:
    new_audio = new_audio.loop(duration=video.duration)

# If the video is longer than the audio, you may need to cut the video or loop the audio. Here we cut the video.
if video.duration > new_audio.duration:
    video = video.subclip(0, new_audio.duration)

# Set the audio of the video clip
video.set_audio(new_audio)

# Write the result to a file
video.write_videofile('my_new_video.mp4')
