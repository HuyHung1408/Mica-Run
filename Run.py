from tkinter import ttk
from tkinter import *
from win32mica import ApplyMica, MICAMODE
from ctypes import windll

#App name
run = Tk()
run.title('Run')
run.geometry('380x190')
run.update()

Ok = ttk.Button(run, text='OK').place(x = 95, y = 140, width = 80)
Cancel = ttk.Button(run, text='Cancel', command=run.destroy).place(x = 185, y = 140, width = 80)
Browse = ttk.Button(run, text='Browse...').place(x = 275, y = 140, width = 80)

opentext = ttk.Label(text='Open:').place(x=13, y=85)

input = ttk.Combobox().place(x=60, y=80, width=295)

img = PhotoImage(file='Run icon.png')
Runicon = Label(run, image=img).place(x=10, y=18)
text = ttk.Label(text='Type the name of a program, folder, document, or\nInternet resource, and Windows will open it for you.', font=('Segoe UI Variable Display','10')).place(x=60, y=20)

#App size
run.minsize(run.winfo_width(), run.winfo_height())
x_cordinate = int((run.winfo_screenwidth() / 2) - (run.winfo_width() / 2))
y_cordinate = int((run.winfo_screenheight() / 2) - (run.winfo_height() / 2))
run.resizable(False, False)
run.iconbitmap('Run icon.ico')

#Theme for Tkinter
run.tk.call("source", "sun-valley.tcl")
run.tk.call("set_theme", "light")

#App theme
bg_color = ttk.Style().lookup(".", "background")
run.wm_attributes("-transparent", bg_color)
HWND=windll.user32.GetParent(run.winfo_id())
ApplyMica(HWND, ColorMode=MICAMODE.LIGHT)
run.update()

run.mainloop()