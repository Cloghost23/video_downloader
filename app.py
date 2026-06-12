import streamlit as st
import yt_dlp
import os
import tempfile

st.title("Vid downloader")
url = st.text_input("Enter the URL")

if st.button("Download"):
    if url:
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'format': 'bestvideo + bestaudio',
                'noplaylist': True,
                'merge_output_format': 'mp4',
                'ffmpeg': 'usr/bin/ffmpeg',
                'quiet': False,
                'no_warnings': True
            }

            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                files = [f for f in os.listdir(tmpdir) if f.endswith(('.mp4', '.mp3', '.webm'))]
                if files:
                    files_path = os.path.join(tmpdir, files[0])


                    with open(files_path, 'rb') as f:
                        st.download_button(
                            label="Download Files",
                            data = f,
                            file_name = files[0],
                            mime='video/mp3'
                        )
                    st.success("Download ready")
                else:
                    st.error("No files found")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    else:
        st.warning("Enter a valid URL")
