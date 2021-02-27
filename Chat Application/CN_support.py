import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global ip
    ip = tk.StringVar()
    ip.set('IP Address')
    global name
    name = tk.StringVar()
    name.set('Name')
    global ip_entry
    ip_entry = tk.StringVar()
    global name_entry
    name_entry = tk.StringVar()
    global con
    con = tk.StringVar()
    con.set('Connect')
    global quir
    quir = tk.StringVar()
    quir.set('Quit')
    global group_chat
    group_chat = tk.StringVar()
    global selectedButton
    selectedButton = tk.IntVar()
    global Email
    Email = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import CN
    CN.vp_start_gui()




