"""YouTube -> MP3/MP4 converter. Usage: python converter.py <url> [mp3|mp4] [-o folder]"""
import argparse

from yt_dlp import YoutubeDL


def options(fmt, out_dir):
    opts = {"outtmpl": f"{out_dir}/%(title)s.%(ext)s"}
    if fmt == "mp3":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]
    else:
        opts["format"] = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        opts["merge_output_format"] = "mp4"
    return opts


def main():
    p = argparse.ArgumentParser(description="Download a YouTube video as MP3 or MP4.")
    p.add_argument("url")
    p.add_argument("format", nargs="?", choices=["mp3", "mp4"], default="mp3")
    p.add_argument("-o", "--out", default="downloads", help="output folder (default: downloads)")
    a = p.parse_args()
    with YoutubeDL(options(a.format, a.out)) as ydl:
        ydl.download([a.url])


if __name__ == "__main__":
    main()
