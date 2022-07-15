from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cv2
img = ' '


def browsing():
    global img
   # filetypes = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Files', '*.txt')]
    filetypes = [('All Files', '*.*'), ('JPG Image', '*.jpg'), ('Text Files', '*.png')]
    file = filedialog.askopenfilename(initialdir = os.getcwd(), title ='Browse Image File', filetype=filetypes, defaultextension=filetypes)
    t1.set(file)
    img = cv2.imread(file,cv2.IMREAD_UNCHANGED)
    w.set(img.shape[0]) # setting the width of the image to 0 pixels
    h.set(img.shape[1]) # setting the height of the image to 0 pixels


def Preview():
    cv2.imshow('show image',img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def recalculate():
    p = int(perc.get())
    new_width =int(int(w.get()) * p/100)
    new_height = int(int(h.get())*p /100)
    w.set(new_width)
    h.set(new_height)

def save_resized_img():
    filetypes = [('All Files', '*.*'), ('JPG Image', '*.jpg'), ('Text Files', '*.png')]
    file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Save Image File', filetype=filetypes,
                                      defaultextension=filetypes)
    nw =int(w.get())
    nh = int(h.get())
    img2 = cv2.resize(img,(nw,nh),interpolation= cv2.INTER_AREA)
    cv2.imwrite(file,img2)
    messagebox.showinfo('Image Saved','Image have been saved'+os.path.basename(file)+'successfully')

def preview_resized_img():
    nw =int(w.get())
    nh = int(h.get())
    img2 = cv2.resize(img,(nw,nh),interpolation= cv2.INTER_AREA)
    cv2.imshow('Preview',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



root = Tk()
t1 = StringVar()
w = StringVar()
perc = StringVar()
h = StringVar()
wrapper = LabelFrame(root, text='Source File')
wrapper.pack(fill='both', expand='yes', padx=20, pady=10)

wrapper2 = LabelFrame(root, text='Image Details')
wrapper2.pack(fill='both', expand='yes', padx=20, pady=20)

wrapper3 = LabelFrame(root, text='Actions')
wrapper3.pack(fill='both', expand='yes', padx=20, pady=20)

lbl = Label(wrapper, text='Source File')
lbl.pack(side=tk.LEFT, padx=10, pady=20)

ent = Entry(wrapper, textvariable=t1)
ent.pack(side=tk.LEFT, padx=10, pady=10)

btn = Button(wrapper, text='Browse', command=browsing)
btn.pack(side=tk.LEFT, padx=10, pady=10)

btn2 = Button(wrapper, text='Preview', command=Preview)
btn2.pack(side=tk.LEFT, padx=10, pady=10)

lbl2 = Label(wrapper2, text='Dimension')
lbl2.pack(side=tk.LEFT, padx=10, pady=20)

ent2 = Entry(wrapper2, textvariable=w)
ent2.pack(side=tk.LEFT, padx=10, pady=10)

lbl3 = Label(wrapper2, text='X')
lbl3.pack(side=tk.LEFT, padx=10, pady=20)

ent3 = Entry(wrapper2, textvariable=h)
ent3.pack(side=tk.LEFT, padx=10, pady=10)

wrapper4 = LabelFrame(root, text='Pixel Safe')
wrapper4.pack(fill='both', expand='yes', padx=20, pady=20)

lbl4 = Label(wrapper4, text='Percentage')
lbl4.pack(side=tk.LEFT, padx=10, pady=20)

ent4 = Entry(wrapper4, textvariable=perc)
ent4.pack(side=tk.LEFT, padx=10, pady=10)

btn3 = Button(wrapper4, text='Recalculate Dimension',command = recalculate )
btn3.pack(side=tk.LEFT, padx=10, pady=10)


lbl6 = LabelFrame(wrapper4, text='Actions')
lbl6.pack(side=tk.LEFT,expand='yes', padx=10, pady=20)


previewbtn = Button(wrapper4, text='Preview The save image',command = preview_resized_img)
previewbtn.pack(side=tk.LEFT, padx=10, pady=10)

Savebtn = Button(wrapper4, text='Save the image',command = save_resized_img)
Savebtn.pack(side=tk.LEFT, padx=10, pady=10)

root.geometry('800x600')

root.mainloop()
