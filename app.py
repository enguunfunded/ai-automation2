import streamlit as st
from main import download_video, create_shorts
import os

INPUT_FILE = "input/links.txt"
OUTPUT_DIR = "output"

st.set_page_config(page_title="YouTube Shorts Generator")
st.title("🎬 YouTube Shorts Generator")

video_url = st.text_input("📥 YouTube Video Link", "")

if st.button("🎞 Short Video үүсгэх"):
    if not video_url.strip():
        st.warning("Та YouTube линк оруулна уу.")
    else:
        with open(INPUT_FILE, "w") as f:
            f.write(video_url.strip())

        st.info("📥 Видеог татаж авч байна...")
        try:
            video_file = download_video(video_url)
        except Exception as e:
            st.error(f"⛔ Алдаа гарлаа: {e}")
            st.stop()

        st.info("✂️ Богино видео хувааж байна...")
        create_shorts(video_file, OUTPUT_DIR)

        st.success("✅ Богино видеонууд амжилттай үүслээ!")
        st.video(os.path.join(OUTPUT_DIR, "short1.mp4"))

        for i in range(2, 6):
            path = os.path.join(OUTPUT_DIR, f"short{i}.mp4")
            if os.path.exists(path):
                st.video(path)
