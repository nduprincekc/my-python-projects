from tkinter import *

# root configuration
root = Tk()
root.title('Kc Emma Light/Dark Toggle_Switch')
root.geometry('400x600')

# inserting the images
on = PhotoImage(file='light.png')
off = PhotoImage(file='dark.png')

button_mode = TRUE


def custom_size():
    global button_mode
    if button_mode:
        on_button.config(bg='#26242f',image=off,activebackground='#26242f')
        root.config(bg='#26242f')
        button_mode = False
    else:
        on_button.config(bg='white',image=on)
        root.config(bg='white')
        button_mode = TRUE


on_button = Button(root,image=on,bd=0,bg='white',activebackground='white',command=custom_size)
on_button.pack(padx=50,pady=50)
root.mainloop()
