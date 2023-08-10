#This code is under the GPLv3 Licence. The full repository can be found at github.com/Pepito468/YTDownloader

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

arguments.add_argument('url', help='Video URL')
arguments.add_argument('-oa','--onlyaudio', action='store_true', help='Download only the audio')
arguments.add_argument('-ov','--onlyvideo', action='store_true', help='Download only the Video')
arguments.add_argument('-r' ,'--resolution', type=str, help='Video resolution')

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
    ydl_opts = {'format': 'bestaudio+bestvideo'}

resolutionlist = ('256x144','426x240','640x360','854x480','1280x720','1920x1080','3840x2160')

if args.resolution:
    if args.resolution == '144p':
        res = resolutionlist[0]
    elif args.resolution == '240p':
        res = resolutionlist[1]
    elif args.resolution == '360p':
        res = resolutionlist[2]
    elif args.resolution == '480p':
        res = resolutionlist[3]
    elif args.resolution == '720p':
        res = resolutionlist[4]
    elif args.resolution == '1080p':
        res = resolutionlist[5]
    elif args.resolution == '2160p':
        res = resolutionlist[6]
    else:
        raise AttributeError("Invalid resolution")

    ydl_opts['format'] = f'bestvideo[ext=webm][resolution={res}]+bestaudio'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

