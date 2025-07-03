import os
import whisper
import subprocess
from moviepy.editor import VideoFileClip
import yt_dlp

# 1. Whisper ашиглан видеоноос текст гаргах
model = whisper.load_model("medium")  # "small", "medium" боломжтой
result = model.transcribe("input/video.mp4", language="Mongolian")


# 2. Subtitle формат бэлдэх
def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

# 3. SRT subtitle бичих
with open("subtitle.srt", "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = format_time(segment["start"])
        end = format_time(segment["end"])
        text = segment["text"].strip()
        f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

print("✅ SRT хадгалагдлаа: subtitle.srt")

# 4. FFmpeg ашиглан subtitle-г видеонд шингээх
input_video = "input/video.mp4"
output_video = "output/video_with_subs.mp4"
subtitles = "subtitle.srt"

subprocess.run([
    "ffmpeg", "-i", input_video,
    "-vf", f"subtitles={subtitles}",
    "-c:a", "copy",
    output_video
])
