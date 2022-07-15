from tkinter import *
import pyperclip
root = Tk()

root.title('color Picker')
root.resizable(0,0)

## 100 distance from x-axis
## 111 distance from y-axis
root.geometry('280x440+100+111')


def slide(value):
    R=r_Scale.get()
    G=G_Scale.get()
    B=B_Scale.get()

    # formating the rgb color
    rgb= f'{R},{G},{B}'

    # format code for hexdecimal
    hex= '#%02x%02x%02x' % (R,G,B)
    colorLabel.config(bg=hex)

    hex_entry.delete(0, END)
    hex_entry.insert(0,hex)

    rgb_entry.delete(0,END)
    rgb_entry.insert(0,rgb)

def hex_copy():
    pyperclip.copy(hex_entry.get())

def rgb_copy():
    pyperclip.copy(rgb_entry.get())

colorLabel = Label(root,bg='black',width=37, height=9,bd=2,relief=RAISED)
colorLabel.pack()



frame = Frame(root, bd=2 ,relief=SUNKEN)
frame.pack(pady=5)

r_label = Label(frame, text = 'R', fg = 'red', font=('arial',10,'bold'))
r_label.grid(row=0,column=0)

r_Scale = Scale(frame,from_=0, to=255, length=210, fg='red', orient=HORIZONTAL,command=slide)
r_Scale.grid(row=0,column=1)

G_label = Label(frame, text = 'G', fg = 'green', font=('arial',10,'bold'))
G_label.grid(row=1,column=0)

G_Scale = Scale(frame,from_=0, to=255, length=210, fg='green', orient=HORIZONTAL,command=slide)
G_Scale.grid(row=1,column=1)

B_label = Label(frame, text = 'B', fg = 'Blue', font=('arial',10,'bold'))
B_label.grid(row=2,column=0)

B_Scale = Scale(frame,from_=0, to=255, length=210, fg='blue', orient=HORIZONTAL,command=slide)
B_Scale.grid(row=2,column=1)


# creating a frame for hex_label and
my_frame = Frame(root,bd=2,relief=SUNKEN)
my_frame.pack(pady=5)


# code for hex_data
Hex_label = Label(my_frame, text = 'Hex_code', fg = 'Blue', font=('arial',10,'bold'))
Hex_label.grid(row=0,column=0)

hex_entry = Entry(my_frame, fg='blue', )
hex_entry.grid(row=0,column=1)
hex_entry.insert(END,'#0000000')

#code for copy
# columnspan means that the button can take two column

copyButton = Button(my_frame,text='Copy',font=('arial',10,'bold'),command=hex_copy)
copyButton.grid(row=1,columnspan=2,pady=2)

rgb_label = Label(my_frame, text = 'rgb_code', fg = 'Blue', font=('arial',10,'bold'))
rgb_label.grid(row=2,column=0)

rgb_entry = Entry(my_frame, fg='blue', )
rgb_entry.grid(row=2,column=1)
rgb_entry.insert(END,'0,0,0')
copyButton2 = Button(my_frame,text='Copy',font=('arial',10,'bold'),command=rgb_copy)
copyButton2.grid(row=3 ,columnspan=4,pady=2)


root.mainloop()


