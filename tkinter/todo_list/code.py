from tkinter import ttk
from tkinter import *


class todo:
    def __init__(self,root):
        self.root = root
        self.root.title = 'To-do-list'
        self.root.geometry('650x610+300+150')

        self.label = Label(self.root,text='To do List',font='arial, 25 bold',width=10,bd=5,bg='orange',fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root,text='Add Task',font='ariel, 25 bold',width=10,bd=5,bg='orange',fg='black')
        self.label2.place(x=15,y=54)

        self.label3 = Label(self.root, text='Task', font='arial, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320,y=54)

        self.main_text = Listbox(self.root,height=8,bd=5,width=18,font='sarif, 20 bold')
        self.main_text.place(x=300,y=100)

        self.text = Text(self.root,bd=5,height=0,width=20,font='sarif, 18 bold')
        self.text.place(x=15,y=100)

        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.delete(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                    f.truncate()
                self.main_text.delete(delete_)
        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END, ready)
            file.close()
        self.button = Button(self.root,text='Add',font='sarif 20 bold',width=10,bd=5,bg='orange',fg='black',command=add)
        self.button.place(x=30,y=150)
        self.button2 = Button(self.root,text='Delete',font='sarif 20 bold',bg='orange',width=10,command=delete)
        self.button2.place(x=30,y=300)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__== "__main__":
    main()
