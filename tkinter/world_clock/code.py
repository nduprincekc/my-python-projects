from tkinter import *
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry('1200x400')
image_icon =PhotoImage(file='gb.png')
root.iconphoto(False,image_icon)


def times():
    home = pytz.timezone('Asia/kolkata')
    local_time=datetime.now(home)
    current_time = local_time.strftime("%A %H:%M:%S")
    clock.config(text=current_time)
    name.config(text='India')
    clock.after(200,times)


    # home 2 London
    home2 = pytz.timezone('europe/london')
    local_time2=datetime.now(home2)
    current_time2 = local_time2.strftime("%A %H:%M:%S")
    clock2.config(text=current_time2)
    name2.config(text='London')
    clock2.after(200,times)

    # home 3 # Japan
    home3 = pytz.timezone('Asia/Tokyo')
    local_time3 = datetime.now(home3)
    current_time3 = local_time3.strftime("%A %H:%M:%S")
    clock3.config(text=current_time3)
    name3.config(text='Toyoko')
    clock3.after(200, times)


    # home 4 # new york
    home4 = pytz.timezone('America/New_York')
    local_time4 = datetime.now(home4)
    current_time4 = local_time4.strftime("%A %H:%M:%S")
    clock4.config(text=current_time4)
    name4.config(text='New York')
    clock4.after(200, times)



# india time zone
f = Frame(root,bd=5)
f.place(x=10,y=118,width=220,height=150)

name= Label(f,font=("Helvetica",30,"bold"))
name.place(x=50,y=40)

logo =PhotoImage(file='india.png')
image_label=Label(root,image=logo)
image_label.place(x=32,y=180)

clock = Label(f,font=('Helvetica',20,'bold'))
clock.place(x=5,y=80)

# gb time zone
f2 = Frame(root,bd=5)
f2.place(x=300,y=118,width=220,height=150)

name2= Label(f2,font=("Helvetica",30,"bold"))
name2.place(x=40,y=30)

logo2 =PhotoImage(file='gb.png')
image_label=Label(root,image=logo2)
image_label.place(x=310,y=170)

clock2 = Label(f2,font=('Helvetica',20,'bold'))
clock2.place(x=0,y=80)

# jp time zone
f3 = Frame(root,bd=5)
f3.place(x=600,y=118,width=220,height=150)

name3= Label(f3,font=("Helvetica",30,"bold"))
name3.place(x=40,y=30)

logo3 =PhotoImage(file='jp.png')
image_label=Label(root,image=logo3)
image_label.place(x=610,y=170)

clock3 = Label(f3,font=('Helvetica',20,'bold'))
clock3.place(x=0,y=80)


# us time zone
f4 = Frame(root,bd=5)
f4.place(x=900,y=118,width=220,height=150)

name4= Label(f4,font=("Helvetica",30,"bold"))
name4.place(x=30,y=30)

logo4 =PhotoImage(file='us.png')
image_label4=Label(root,image=logo4)
image_label4.place(x=900,y=170)

clock4 = Label(f4,font=('Helvetica',20,'bold'))
clock4.place(x=0,y=80)



times()





root.mainloop()

