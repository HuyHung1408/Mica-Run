from tkinter import ttk
from tkinter import *
from win32mica import ApplyMica, MICAMODE
from ctypes import windll

run = Tk()
run.title('Run')
run.geometry('399x173')
run.update()

Ok = ttk.Button(run, text='OK').grid(row=3, column=2)

img = PhotoImage(file='Run icon.png')
a = Label(run, image=img).grid(row= 1, column =1, padx=8, pady=8)
text = ttk.Label(text='Type the name of a program, folder, document, or Internet\nresource, and Windows will open it for you.', font=('Segoe UI Variable Display','10')).grid(row=1, column = 2, pady=16)




run.minsize(run.winfo_width(), run.winfo_height())
x_cordinate = int((run.winfo_screenwidth() / 2) - (run.winfo_width() / 2))
y_cordinate = int((run.winfo_screenheight() / 2) - (run.winfo_height() / 2))
run.resizable(False, False)
run.iconbitmap('Run icon.ico')

run.tk.call("source", "sun-valley.tcl")
run.tk.call("set_theme", "light")

#App theme
bg_color = ttk.Style().lookup(".", "background")
run.wm_attributes("-transparent", bg_color)
HWND=windll.user32.GetParent(run.winfo_id())
ApplyMica(HWND, ColorMode=MICAMODE.LIGHT)
run.update()

run.mainloop()