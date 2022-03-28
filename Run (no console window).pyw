from tkinter import Tk, Label, PhotoImage, filedialog, ttk, messagebox
from win32mica import ApplyMica, MICAMODE
from ctypes import windll
import darkdetect
import tkinter as tk
import os
import sv_ttk

#App name
run = Tk()
run.resizable(False, False)
sv_ttk.set_theme('light')
run.title('Run')
run.geometry('380x190')
run.iconbitmap('Run icon.ico')

if  darkdetect.isDark():
            sv_ttk.set_theme('dark')
            HWND=windll.user32.GetParent(run.winfo_id())
            ApplyMica(HWND, ColorMode=MICAMODE.DARK)
else:
            sv_ttk.set_theme('light')
            HWND=windll.user32.GetParent(run.winfo_id())
            ApplyMica(HWND, ColorMode=MICAMODE.LIGHT)

#App size
def browsefunc():
    filename =filedialog.askopenfilename(filetypes=(("Programs","*.exe"),("All files","*.*")))
    input.set("")
    input.insert(tk.END, filename)
    
def okbutton(event=None):
    try:
     os.startfile(input.get())
     run.destroy()
    except:
     messagebox.showerror(input.get(), 'Make sure you typed the name correctly, and then try again.')

input = ttk.Combobox()
input.place(x=60, y=79, width=295)
input.focus_set()

run.wm_attributes('-transparentcolor', '#ab23ff')
transparent = Label(run, text= "", bg= '#ab23ff').place(x = 0, y=130, height= 60, width = 380)

Ok = ttk.Button(run, text='OK', command=okbutton)
Ok.place(x = 95, y = 143, width = 80)
run.bind('<Return>', okbutton)

Cancel = ttk.Button(run, text='Cancel', command=run.destroy).place(x = 185, y = 143, width = 80)
Browse = ttk.Button(run, text='Browse...', command=browsefunc).place(x = 275, y = 143, width = 80)

opentext = ttk.Label(text='Open:').place(x=13, y=85)

img = PhotoImage(file='Run icon.png')
Runicon = Label(run, image=img).place(x=10, y=18)
text = ttk.Label(text='Type the name of a program, folder, document, or\nInternet resource, and Windows will open it for you.', font=('Segoe UI Variable Display','10')).place(x=60, y=20)


            
run.mainloop()