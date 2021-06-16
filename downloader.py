from tkinter import *
from pytube import YouTube
box=Tk()
Label(box,text='Link').pack()
link=Entry(box)
link.pack()
def downloader():
    SAVE_PATH = "P:/" 
    try: 
        yt = YouTube(link.get()) 
    except: 
        print("Connection Error")
    mp4files = yt.streams.first()
    try: 
        mp4files.download(SAVE_PATH)
    except: 
        print("Some Error!") 
    print('Task Completed!') 
download=Button(box,text='download',command=downloader)
download.pack()
box.mainloop()