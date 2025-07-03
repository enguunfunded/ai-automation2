import os
import whisper
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# 1. Extract audio
video_path = "input/video.mp4"
audio_path = "audio/audio.wav"

os.makedirs("audio", exist_ok=True)
os.system(f"ffmpeg -i {video_path} -vn -acodec pcm_s16le -ar 16000 -ac 1 {audio_path}")

# 2. Transcribe audio with Whisper
model = whisper.load_model("base")
result = model.transcribe(audio_path)
full_text = result["text"]
print("AI-гаар үүсгэсэн текст:", full_text)

# 3. Extract short video (жишээ: эхний 30 секунд)
clip = VideoFileClip(video_path).subclip(0, 30)

# 4. Create text overlay
txt_clip = TextClip(full_text[:100] + "...", fontsize=36, color='white', font='Arial-Bold')
txt_clip = txt_clip.set_position(("center", "bottom")).set_duration(clip.duration)

# 5. Combine video and text
final = CompositeVideoClip([clip, txt_clip])
os.makedirs("output", exist_ok=True)
final.write_videofile("output/short_with_text.mp4", codec="libx264", audio_codec="aac")
