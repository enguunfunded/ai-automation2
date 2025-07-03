from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

video = VideoFileClip("input.mp4")

txt = TextClip("AI үг гарлаа!", fontsize=70, color='white', font='Arial-Bold')
txt = txt.set_position(("center", "bottom")).set_duration(5)

final = CompositeVideoClip([video, txt])
final.write_videofile("output_text.mp4", codec="libx264", audio_codec="aac")
