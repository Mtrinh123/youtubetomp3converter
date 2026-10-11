# YouTube to MP3/MP4 Converter

A tool that saves a YouTube video as an MP3 (audio only) or an MP4 (video + audio), so you don't need a converter website. Use the files to listen to music offline or to edit them in music or video software.

## How it works

The script uses yt-dlp to download the video. Then FFmpeg either converts it to a MP3 file or joins the video and audio into a MP4.

## Requirements

- Python 3.9 or newer
- FFmpeg on your PATH. On Windows, run `winget install ffmpeg` then open a new terminal!

## Before using the tool!

```bash
pip install -r requirements.txt
```

## How to use the tool!

```bash
# MP3 (Audio only)
python converter.py "https://www.youtube.com/watch?v=VIDEO_ID"

# MP4 (Audio+Video)
python converter.py "https://www.youtube.com/watch?v=VIDEO_ID" mp4

# Choose an output folder 
python converter.py "https://www.youtube.com/watch?v=VIDEO_ID" mp3 -o "C:/Music"
```

## Roadmap

- [ ] Playlist support
- [ ] Choose the audio quality and video resolution
- [ ] Simple GUI or web page
- [ ] Download progress bar
- [ ] Dictate where it goes in file explorer instead of using commands 


