import streamlit as st
from moviepy.editor import VideoFileClip
import os

st.set_page_config(page_title="YouTube Shorts Cutter", layout="centered")
st.title("🎬 YouTube Shorts Cutter")

st.markdown("MP4 видео файл оруулна уу. Бид үүнийг богино бичлэг болгон хөрвүүлнэ.")

uploaded_file = st.file_uploader("📤 Видео оруулах (MP4)", type=["mp4"])

if uploaded_file is not None:
    with st.spinner("⏳ Видео боловсруулж байна..."):
        with open("input.mp4", "wb") as f:
            f.write(uploaded_file.read())

        clip = VideoFileClip("input.mp4")
        short_duration = min(60, clip.duration)
        short = clip.subclip(0, short_duration)
        short.write_videofile("short.mp4", codec="libx264", audio_codec="aac")

    st.success("✅ Богино видео амжилттай үүсгэлээ!")
    st.video("short.mp4")

    with open("short.mp4", "rb") as f:
        st.download_button("⬇️ Видео татах", f, file_name="short.mp4", mime="video/mp4")
