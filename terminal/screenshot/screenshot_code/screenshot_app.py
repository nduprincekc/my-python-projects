import PIL.ImageGrab as pl
import time
from tkinter import *



root = Tk()
root.geometry('440x330')
root.title('ScreenShoot App')


def take_screen():
    root.withdraw() # hiding the window
    time.sleep(3)

    img = pl.grab()
    img.save('Screenshot.png')
    root.update()
    root.deiconify()
    root.destroy()
    img.show()

Button(root,width=25,height=4,text='Take Shot',bg='brown',fg='white',command=take_screen).place(x=130,y=120)


root.mainloop()
