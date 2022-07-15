import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import *

# configuring the root gui
root = tk.Tk()
root.resizable(False, False)
root.geometry('1000x600+100+30')

# showing the pdf
v = pdf.ShowPdf()
v2 = pdf.Frame(v)
u = Frame(root,color = 'green')
#u.grid(row= '3',column ='44')
#v2 = v.pdf_view(root, pdf_location=askopenfilename(), width='60', height='60')
v2.pack()
root.mainloop()

#design by kc emma
