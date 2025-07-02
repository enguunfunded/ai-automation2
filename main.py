import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import yt_dlp

# === SETUP ===
INPUT_FILE = "input/links.txt"
OUTPUT_DIR = "output"
SHORT_DURATION = 180  # 3 минутаар хуваана
MAX_SHORTS = 5

os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

def create_shorts(video_path, output_dir):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    segment = min(SHORT_DURATION, duration / MAX_SHORTS)

    for i in range(MAX_SHORTS):
        start = i * segment
        end = min(start + segment, duration)
        short_clip = clip.subclip(start, end)
        short_clip.write_videofile(f"{output_dir}/short{i+1}.mp4", codec="libx264")
    clip.close()

# === MAIN ===
with open(INPUT_FILE, "r") as f:
    video_url = f.readline().strip()

print(f"[INFO] Downloading video from: {video_url}")
video_file = download_video(video_url)

print("[INFO] Creating short videos...")
create_shorts(video_file, OUTPUT_DIR)
print("[DONE] Shorts created successfully.")
