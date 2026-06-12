import yt_dlp
import streamlit as st

# Define resolution and other options
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    return info['title']

# Streamlit UI
url = st.text_input("Enter YouTube URL")
if st.button("Download"):
    if url:
        st.success(f"Downloaded: {download_video(url)}")   
