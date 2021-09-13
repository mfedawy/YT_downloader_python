import tkinter as tk
from tkinter.constants import LEFT, RIGHT
from pytube import YouTube
import sys
import os
import shutil
from pytube.cli import on_progress #this module contains the built in progress bar. 

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Dr fedawy YT downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='enter url:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140,width=300, window=entry1)

def download ():
    
    x1 = entry1.get()
   # myUrl=input('enter URL')
    yt = YouTube(x1,on_progress_callback=on_progress)
    print(yt.streams.filter(subtype='mp4').all())
    yt.streams.filter(subtype='mp4').first().download()

    label3 = tk.Label(root, text= yt.title + ' is:'+'downloaded',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    # label4 = tk.Label(root, 'downloaded',font=('helvetica', 10, 'bold'))
    # canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Download video', command=download, bg='brown', fg='white', font=('helvetica', 9, 'bold')).pack(side = RIGHT, padx = 10, pady = 10)
canvas1.create_window(200, 180, window=button1)







def download_audio ():
    x1 = entry1.get()
    yt = YouTube(x1)
    print(yt.streams.filter(only_audio=True).all())
    yt.streams.filter(only_audio=True).first().download()
    label3 = tk.Label(root, text= yt.title  + ' is:'+'downloaded',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    # YouTube.Youtube(x1).streams.filter(only_audio=True).all()

button2 = tk.Button(text='Download Audio', command=download_audio, bg='brown', fg='white', font=('helvetica', 9, 'bold',)).pack(side = LEFT, padx = 10, pady = 10)
canvas1.create_window(200, 180, window=button2)


# tk.Button(text = "Video",command = download).grid(row = 1, column = 0)

# tk.Button(text = "audio",command = download_audio).grid(row = 1, column = 1)


root.mainloop()