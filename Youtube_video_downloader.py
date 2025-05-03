import streamlit as st
import yt_dlp
import os

st.title("YouTube Video Downloader")

def video_download(url, save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        ydl_opts = {
            'format': '18',  # progressive mp4
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'postprocessors': [],  # prevent FFmpeg use
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        st.success("Video downloaded successfully!")

        with open(filename, "rb") as f:
            st.download_button(
                label="Download Video",
                data=f,
                file_name=os.path.basename(filename),
                mime="video/mp4"
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")

video_url = st.text_input("Enter the YouTube URL:")
save_dir = os.getcwd()  

if st.button("Get Video"):
    if video_url:
        st.info("Download started... Please wait.")
        video_download(video_url, save_dir)
    else:
        st.warning("Please enter a YouTube video URL!")
