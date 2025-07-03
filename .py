from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Видео файл унших
video = VideoFileClip("input.mp4")

# Гарчиг текст үүсгэх
txt = TextClip("AI үг гарлаа!", fontsize=70, color='white', font='Arial-Bold')

# Байршил, үргэлжлэх хугацаа тохируулах
txt = txt.set_position(("center", "bottom")).set_duration(5)

# Видео + текст нэгтгэх
final = CompositeVideoClip([video, txt])

# Шинэ видео хадгалах
final.write_videofile("output_text.mp4", codec="libx264", audio_codec="aac")
