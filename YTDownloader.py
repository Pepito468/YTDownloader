#Libraries

import importlib
import argparse

#Install yt-dlp if not already installed

try:
    importlib.import_module('yt_dlp')
except ImportError:
    import subprocess
    subprocess.check_call(['pip','install','yt-dlp'])
import yt_dlp

#Argparse arguments

arguments = argparse.ArgumentParser(description='Download YT video')

arguments.add_argument('url',help='Video URL')
arguments.add_argument('-oa','--onlyaudio', action='store_true', help='Download only the Audio')
arguments.add_argument('-ov','--onlyvideo', action='store_true', help='Download only the Video')
arguments.add_argument('-r' ,'--resolution',type=str, default='best', help='Video resolution')

args = arguments.parse_args()

#Clean link to download

video_url = args.url

if video_url.startswith('https://youtube.com/watch?v='):
    video_url = video_url.lstrip('https://youtube.com/watch?v=')
elif video_url.startswith('https://youtu.be/'):
    video_url = video_url.lstrip('https://youtu.be/')

#Downloader

if args.onlyaudio:
    ydl_opts = {'format': 'bestaudio'}
elif args.onlyvideo:
    ydl_opts = {'format': 'bestvideo'}
else:
    ydl_opts = {'format': 'best'}

if args.resolution != 'best':
    ydl_opts['format'] += f'[height<={args.resolution}]'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

