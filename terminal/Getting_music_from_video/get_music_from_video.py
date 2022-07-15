import moviepy.editor as mp
import ffmpeg


video = mp.VideoFileClip(r'sample.mp4')
video.audio.write_audiofile(r'output.mp3')
