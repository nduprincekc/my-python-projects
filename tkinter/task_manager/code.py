from tkinter import *
import os

root=Tk()

root.title('Manage Computer-All In One Place')
root.config(bg='gray20')

titleImage=PhotoImage(file='images/title.png')

titleLabel=Label(root,text=' Computer Manager',font=('elephant','25','bold'),fg='gold2',bg='gray20',image=titleImage
                 ,compound=LEFT)
titleLabel.grid()

frame=Frame(root,bd=8,relief=SUNKEN,bg='white')
frame.grid(row=1)

taskImage=PhotoImage(file='images/task.png')
Button(frame,text=' Task Manager',font=('arial',20,'bold'),image=taskImage,compound=LEFT,fg='red4',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('taskmgr')).grid(padx=10,sticky='w',pady=10)

controlImage=PhotoImage(file='images/controlpanel.png')
Button(frame,text=' Control panel',font=('arial',20,'bold'),image=controlImage,compound=LEFT,fg='black',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('control')).grid(row=0,column=1,padx=10,sticky='w',pady=10)

datetimeImage=PhotoImage(file='images/datetime.png')
Button(frame,text=' Date and Time',font=('arial',20,'bold'),image=datetimeImage,compound=LEFT,fg='dark orange',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('timedate.cpl')).grid(row=1,column=0,padx=10,sticky='w',pady=10)

servicesImage=PhotoImage(file='images/services.png')
Button(frame,text=' System Services',font=('arial',20,'bold'),image=servicesImage,compound=LEFT,fg='yellow2',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('services.msc')).grid(row=1,column=1,padx=10,sticky='w',pady=10)

deviceImage=PhotoImage(file='images/device.png')
Button(frame,text=' Device Manager',font=('arial',20,'bold'),image=deviceImage,compound=LEFT,fg='purple',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('devmgmt.msc')).grid(row=2,column=0,padx=10,sticky='w',pady=10)

updateImage=PhotoImage(file='images/update.png')
Button(frame,text=' Windows Update',font=('arial',20,'bold'),image=updateImage,compound=LEFT,fg='royal blue3',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('control update')).grid(row=2,column=1,padx=10,sticky='w',pady=10)

mouseImage=PhotoImage(file='images/mouse.png')
Button(frame,text=' Mouse Properties',font=('arial',20,'bold'),image=mouseImage,compound=LEFT,fg='gray30',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('main.cpl')).grid(row=3,column=0,padx=10,sticky='w',pady=10)

propertiesImage=PhotoImage(file='images/properties.png')
Button(frame,text=' System properties',font=('arial',20,'bold'),image=propertiesImage,compound=LEFT,fg='deep pink',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('sysdm.cpl')).grid(row=3,column=1,padx=10,sticky='w',pady=10)

removeImage=PhotoImage(file='images/remove.png')
Button(frame,text=' Uninstall Softwares',font=('arial',20,'bold'),image=removeImage,compound=LEFT,fg='royal blue',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('appwiz.cpl')).grid(row=4,column=0,padx=10,sticky='w',pady=10)

networkImage=PhotoImage(file='images/network.png')
Button(frame,text=' Network Connections',font=('arial',20,'bold'),image=networkImage,compound=LEFT,fg='dark green',bg='white',
       cursor='hand2',bd=0,command=lambda : os.system('ncpa.cpl')).grid(row=4,column=1,padx=10,sticky='w',pady=10)





root.mainloop()
