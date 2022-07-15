from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x=32, y=90)


def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    #     'resolution').desc().first().download()


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
