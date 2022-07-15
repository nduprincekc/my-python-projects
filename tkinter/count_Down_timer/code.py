from tkinter import *
import time
from playsound import playsound
import pygame
from tkinter import messagebox
pygame.mixer.init()
pygame.mixer.music.load('Naira-Marley-Chichi.mp3')


root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg ='blanched almond')
root.title('Kc Emma - Countdown Clock And Timer')
Label(root, text = 'Countdown Clock and Timer' , font = 'arial 20 bold',  bg ='papaya whip').pack()


Label(root, font ='arial 15 bold', text = 'current time :', bg = 'papaya whip').place(x = 40 ,y = 70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()


sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')

mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')

hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')


def countdown():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times == 0):
            pygame.mixer.music.play()
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            messagebox.showinfo('time up','TIME IS UP ')
        times -= 1


def exit():
    root.destroy()


def restart():
    sec.set('00')
    mins.set('00')
    hrs.set('00')


Label(root, font='arial 15 bold', text='set the time', bg='papaya whip').place(x=40, y=150)
Label(root, font='arial 15 bold', text='', bg='papaya whip').place(x=40, y=150)

Button(root, text='START', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)
Button(root, text='EXIT', bd='5', command=exit, bg='antique white', font='arial 10 bold').place(x=90, y=210)
Button(root, text='RESTART', bd='5', command=restart, bg='antique white', font='arial 10 bold').place(x=240, y=210)




root.mainloop()
