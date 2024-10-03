import streamlit as st
import yt_dlp
import os

def video_download(url, save_path):
    try:
        # Check if the save_path exists, if not create the directory
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        ydl_opts = {
            'format': 'best',  # Download the best available format
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save path format
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app layout
st.title("YouTube Video Downloader")

video_url = st.text_input("Enter the YouTube URL:")

# Default download folder is current working directory
save_dir = st.text_input("Enter the download folder path:", value=os.getcwd())

if st.button("Download"):
    if video_url and save_dir:
        st.info("Download started...")
        video_download(video_url, save_dir)
    else:
        st.warning("Please enter both the URL and folder path!")
