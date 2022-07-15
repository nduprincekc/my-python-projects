from tkinter import *
import requests
import json
import pytz
import tkinter as tk
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
from tkinter import ttk , messagebox
from tkinter.ttk import *

root = Tk()
root.geometry('900x500+300+100')
root.title('Weather App')
root.resizable(0,0)


def get_weather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text='CURRENT TIME')

    # weathetr
    api ='https://api.openweathermap.org/data/2.5/weather?q='+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure =json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind =json_data['wind']['speed']

    t.config(text=(temp,"°"))
#    c.config(text=(f"THE WEATHER IS ",condition))
    w.config(text=wind)
    h.config(text=humidity)
    p.config(text=pressure)
    d.config(text=description)


textfield = ttk.Entry(root,justify='center',width=20,font=('poppins',25,'bold'),background='#404040')
textfield.place(x=45,y=25)
textfield.focus()

Search_icon =PhotoImage(file='search_icon.png')
myimage_icon = ttk.Button(image=Search_icon,cursor='hand2',command=get_weather)
myimage_icon.place(x=400,y=25)

# logo
logo_image =PhotoImage(file='logo.png')
logo = Label(image=logo_image)
logo.place(x=150,y=100)

# bottom box
Frame_image = PhotoImage(file='box.png')
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


# time
name =Label(root,font=('arial',15,'bold'))
name.place(x=30,y=100)
clock= Label(root,font=('Helvetica',20))
clock.place(x=30,y=130)

# label
label1 = Label(root,text='WIND',font = ('Helvetica',15,'bold'),background='white')
label1.place(x=120,y=400)

label2 = Label(root,text='HUMIDITY',font = ('Helvetica',15,'bold'),background='white')
label2.place(x=250,y=400)

label3 = Label(root,text='DESCRIPTION',font = ('Helvetica',15,'bold'),background='white')
label3.place(x=430,y=400)

label4 = Label(root,text='PRESSURE',font = ('Helvetica',15,'bold'),background='white')
label4.place(x=650,y=400)


t= Label(font=('arial',70,'bold'),background='white')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)


w= Label(text='....',font=('arial',20,'bold'),background='#1ab5ef')
w.place(x=120,y=430)

h= Label(text='...',font=('arial',20,'bold'),background='#1ab5ef')
h.place(x=280,y=430)

d= Label(text='...',font=('arial',20,'bold'),background='#1ab5ef')
d.place(x=420,y=430)

p= Label(text='...',font=('arial',20,'bold'),background='#1ab5ef')
p.place(x=670,y=430)
root.mainloop()
