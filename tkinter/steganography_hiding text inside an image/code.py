from tkinter import *
from tkinter import filedialog
import os
from stegano import lsb
from PIL import Image,ImageTk
from tkinter import messagebox


root = Tk()
root.resizable(0,0)
root.geometry('700x500+150+100')
root.config(bg='#2f4155')
root.title('Kc emma')
global kc

def Openimage():
    global kc
    kc = filedialog.askopenfilename(initialdir=os.getcwd(),
                               title='Select Image',
                               filetype=(("PNG file", "*.PNG"), ("JPG", "*JPG"), ("ALL file", "*.txt")))
    text1.delete(1.0,END)
    img=Image.open(kc)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0,END)
    secret= lsb.hide(str(kc),message)
    messagebox.showinfo('Information','Data have been saved')
    text1.delete(1.0,END)

def Show():
    global kc
    clear_message = lsb.reveal(kc)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)


def Save():
    secret.save('Hidden image.png')


image_icon = PhotoImage(file="stop.png")
root.iconphoto(False,image_icon)


# logo
logo =PhotoImage(file='logo.png')
Label(root,image=logo,bg='#2d4155').place(x=70,y=20)

Label(root,text='CYBER SCIENCE',bg='#2d4155',fg='white',font='arial 25 bold').place(x=100,y=20)



# first frame
f = Frame(root,bd=3,bg='black',width=340,height=280,relief =GROOVE)
f.place(x=10,y=60)

lbl =Label(f,bg='black',text='re')
lbl.place(x=80,y=30)

# second frame
frame2 = Frame(root,bd=3,bg='black',width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=60)

text1 = Text(frame2,font='Roboto 20',bg='white',fg='black',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbarr= Scrollbar(frame2)
scrollbarr.place(x=320,y=0,height=300)

scrollbarr.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbarr.set)


# third frame
frame3 =Frame(root,bd=3,bg='#2f4155',width=330,height=100,relief = GROOVE)
frame3.place(x=10,y=370)


# code for button
Button(frame3,text='Open Image',width=9,height=2,font='arial 18 bold',command=Openimage).place(x=8,y=30)
Button(frame3,text='Save Image',width=9,height=2,font='arial 18 bold').place(x=160,y=30)
Label(frame3,text='Picture, Image, Photo file',bg='#2f4155',fg='yellow').place(x=10,y=5)


# third frame
frame3 =Frame(root,bd=3,bg='#2f4155',width=330,height=100,relief = GROOVE)
frame3.place(x=10,y=370)


# code for button
Button(frame3,text='Open Image',width=9,height=2,font='arial 18 bold',command=Openimage).place(x=8,y=30)
Button(frame3,text='Save Image',width=9,height=2,font='arial 18 bold',command=Save).place(x=160,y=30)
Label(frame3,text='Picture, Image, Photo file',bg='#2f4155',fg='yellow').place(x=10,y=5)

# fourth frame
frame4 = Frame(root,bd=3,bg='#2f4155',width=330,height=100,relief = GROOVE)
frame4.place(x=360,y=370)


# code for button
Button(frame4,text='Hide Data',width=9,height=2,font='arial 18 bold',command=Hide).place(x=20,y=30)
Button(frame4,text='Show Data',width=9,height=2,font='arial 18 bold',command=Show).place(x=180,y=30)
Label(frame4,text='Picture, Image, Photo file',bg='#2f4155',fg='yellow').place(x=20,y=5)



root.mainloop()
