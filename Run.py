from operator import setitem
from tkinter import ttk
from tkinter import *
from win32mica import ApplyMica, MICAMODE
from ctypes import windll
from tkinter import filedialog as fd

#App name
run = Tk()
run.title('Run')
run.geometry('380x190')
run.update()

#Theme for Tkinter
run.tk.call("source", "sun-valley.tcl")
run.tk.call("set_theme", "light")

input = ttk.Combobox().place(x=60, y=80, width=295)

def change_theme():
    if  run.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        run.tk.call("set_theme", "light")
        HWND=windll.user32.GetParent(run.winfo_id())
        ApplyMica(HWND, ColorMode=MICAMODE.LIGHT)
        run.update()
    else:
        run.tk.call("set_theme", "dark")
        HWND=windll.user32.GetParent(run.winfo_id())
        ApplyMica(HWND, ColorMode=MICAMODE.DARK)
        run.update()

run.wm_attributes('-transparentcolor', '#ab23ff')
transparent = Label(run, text= "", bg= '#ab23ff').place(x = 0, y=130, height= 60, width = 380)

def select_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        )
    input = StringVar()
    input.set(filename)

Ok = ttk.Button(run, text='OK', command=change_theme).place(x = 95, y = 143, width = 80)
Cancel = ttk.Button(run, text='Cancel', command=run.destroy).place(x = 185, y = 143, width = 80)
Browse = ttk.Button(run, text='Browse...', command=select_file).place(x = 275, y = 143, width = 80)

opentext = ttk.Label(text='Open:').place(x=13, y=85)

img = PhotoImage(file='Run icon.png')
Runicon = Label(run, image=img).place(x=10, y=18)
text = ttk.Label(text='Type the name of a program, folder, document, or\nInternet resource, and Windows will open it for you.', font=('Segoe UI Variable Display','10')).place(x=60, y=20)

#App size
run.minsize(run.winfo_width(), run.winfo_height())
x_cordinate = int((run.winfo_screenwidth() / 2) - (run.winfo_width() / 2))
y_cordinate = int((run.winfo_screenheight() / 2) - (run.winfo_height() / 2))
run.resizable(False, False)
run.iconbitmap('Run icon.ico')

HWND=windll.user32.GetParent(run.winfo_id())
ApplyMica(HWND, ColorMode=MICAMODE.LIGHT)
run.update()

run.mainloop()