from pytube import YouTube
import sys
import os
import shutil

myUrl=input('enter URL')
yt = YouTube(myUrl)


print(yt.streams.filter(subtype='mp4').all())
yt.streams.filter(subtype='mp4').first().download()