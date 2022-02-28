from tkinter import ttk
from tkinter import *

run = Tk()
run.title('Run')
run.geometry('399x173')
run.update()
run.minsize(run.winfo_width(), run.winfo_height())
x_cordinate = int((run.winfo_screenwidth() / 2) - (run.winfo_width() / 2))
y_cordinate = int((run.winfo_screenheight() / 2) - (run.winfo_height() / 2))
run.resizable(False, False)
run.iconbitmap('Run icon.ico')

img = PhotoImage(file='Run icon.png')
a = Label(run, image=img).grid(row= 1, column =1)
text = ttk.Label(text='Type the name of a program, folder, document, or Internet\n resource, and Windows will open it for you', font='10').grid(row=1, column = 2)



run.mainloop()