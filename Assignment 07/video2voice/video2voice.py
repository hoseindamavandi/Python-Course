from moviepy import editor

video = editor.VideoFileClip('are we there yet.mp4')
video.audio.write_audiofile('are we there yet.mp3')