from tkinter import *
import speedtest, webbrowser

root = Tk()
root.title('Internet Speed Test')
root.geometry('360x600')
root.resizable(0,0)
root.configure(bg='#1a212d')


def link(e):
    webbrowser.open(e)

def check():
    test = speedtest.Speedtest()
    uploading= round(test.upload()/(1024*1024),2)
    upload.config(text = uploading)

    downloading=round(test.download()/(1024*1024),2)
    download.config(text=downloading)
    Download.config(text = downloading)

    server_names= []
    test.get_servers(server_names)
    ping.config(text=test.results.ping)

# icon
image_icon = PhotoImage(file='logo.png')
root.iconphoto(False,image_icon)


# images
Top = PhotoImage(file='top.png')
Label(root,image=Top,bg='#1a212d').pack()

Main=PhotoImage(file='main.png')
Label(root,image=Main,bg='#1a212d',bd=0,activebackground='#1a212d').pack()

button = PhotoImage(file='button.png')
Button = Button(root,image=button,bg='#1a212d',bd = 0,cursor ='hand2',command=check)
Button.pack(pady=10)

# label
Label(root,text='PING',font='arial 10 bold',bg='#384056',fg='white').place(x=50,y=0)
Label(root,text='DOWNLOAD',font='arial 10 bold',bg='#384056',fg='white').place(x=140,y=0)
Label(root,text='UPLOAD',font='arial 10 bold',bg='#384056',fg='white').place(x=260,y=0)
Label(root,text='MS',font='arial 7 bold',bg='#384056',fg='WHITE').place(x=60,y=80)

Label(root,text='MBPS',font='arial 7 bold',bg='#384056',fg='white').place(x=165,y=80)
Label(root,text='MBPS',font='arial 7 bold',bg='#384056',fg='white').place(x=275,y=80)


Label(root,text='MBPS',font='arial 15 bold',bg='#384056',fg='white').place(x=150,y=340)
Label(root,text='DOWNLOAD',font='arial 15 bold',bg='#384056',fg='white').place(x=135,y=230)


ping =Label(root,text='00',font='arial 13 bold',bg='#384056',fg='white')
ping.place(x=70,y=60,anchor='center')


url=Label(root,text='Developed by Nduprincekc',cursor='hand2')
url.pack()
url.bind('<Button-1>',lambda e:link('https://github.com/nduprincekc'))
download =Label(root,text='00',font='arial 13 bold',bg='#384056',fg='white')
download.place(x=180,y=60,anchor='center')
upload =Label(root,text='00',font='arial 13 bold',bg='#384056',fg='white')
upload.place(x=290,y=60,anchor='center')



Download = Label(root,text ='00',font='arial 40 bold',bg='#384056')
Download.place(x=185,y=300,anchor ='center')


root.mainloop()
