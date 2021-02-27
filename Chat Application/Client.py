import sys
from tkinter import *
import GChat
import Audio_client
import threading

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

import CN_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    CN_support.set_Tk_var()
    top = Toplevel1 (root)
    
    CN_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    CN_support.set_Tk_var()
    top = Toplevel1 (w)
    CN_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def connect(self):
        receive_thread = threading.Thread(target=self.tkthread)
        receive_thread.start()
    
    def tkthread(self):
        if self.Entry1.get() and self.Entry2.get() and self.variable.get()==1:
            print('Group Chat Activated')
            GChat.func(self.Entry1.get(),self.Entry2.get())
        elif self.variable.get()==2:
            print('Audio Chat Activated')
            Audio_client.func(self.Entry1.get())
        elif self.variable.get()==3:
            print('Video Chat Activated')
            import VideoChat.clientMedia as cm
            cm.func(self.Entry1.get())
    
    def qfun(self):
        root.destroy()
         
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#3e4134'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.variable = IntVar()

        top.geometry("600x350+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.attributes("-alpha",0.9)


        self.Group_Chat = tk.Radiobutton(top, value=1)
        self.Group_Chat.place(relx=0.1, rely=0.089, relheight=0.056
                , relwidth=0.163)
        self.Group_Chat.configure(activebackground="#f9f9f9")
        self.Group_Chat.configure(activeforeground="black")
        self.Group_Chat.configure(background="#d9d9d9")
        self.Group_Chat.configure(disabledforeground="#7557ee")
        self.Group_Chat.configure(foreground="#000000")
        self.Group_Chat.configure(highlightbackground="#d9d9d9")
        self.Group_Chat.configure(highlightcolor="black")
        self.Group_Chat.configure(justify='left')
        self.Group_Chat.configure(text="Group Chat")
        self.Group_Chat.configure(variable=self.variable)

        self.Audio = tk.Radiobutton(top, value=2)
        self.Audio.place(relx=0.4, rely=0.089, relheight=0.056, relwidth=0.13)
        self.Audio.configure(activebackground="#f9f9f9")
        self.Audio.configure(activeforeground="black")
        self.Audio.configure(background="#d9d9d9")
        self.Audio.configure(disabledforeground="#a3a3a3")
        self.Audio.configure(foreground="#000000")
        self.Audio.configure(highlightbackground="#d9d9d9")
        self.Audio.configure(highlightcolor="black")
        self.Audio.configure(justify='left')
        self.Audio.configure(text="Audio Call")
        self.Audio.configure(variable=self.variable)
	
        self.Video_Chat = tk.Radiobutton(top, value=3)
        self.Video_Chat.place(relx=0.7, rely=0.089, relheight=0.056, relwidth=0.163)
        self.Video_Chat.configure(activebackground="#f9f9f9")
        self.Video_Chat.configure(activeforeground="black")
        self.Video_Chat.configure(background="#d9d9d9")
        self.Video_Chat.configure(disabledforeground="#7557ee")
        self.Video_Chat.configure(foreground="#000000")
        self.Video_Chat.configure(highlightbackground="#d9d9d9")
        self.Video_Chat.configure(highlightcolor="black")
        self.Video_Chat.configure(justify='left')
        self.Video_Chat.configure(text="Video Chat")
        self.Video_Chat.configure(variable=self.variable)

        self.IP = tk.Label(top)
        self.IP.place(relx=0.217, rely=0.280, height=21, width=74)
        self.IP.configure(activebackground="#f9f9f9")
        self.IP.configure(activeforeground="black")
        self.IP.configure(background="#d9d9d9")
        self.IP.configure(disabledforeground="#a3a3a3")
        self.IP.configure(foreground="#000000")
        self.IP.configure(highlightbackground="#d9d9d9")
        self.IP.configure(highlightcolor="black")
        self.IP.configure(text='''IP Address''')
        self.IP.configure(textvariable=CN_support.ip)

        self.Name = tk.Label(top)
        self.Name.place(relx=0.217, rely=0.380, height=21, width=74)
        self.Name.configure(activebackground="#f9f9f9")
        self.Name.configure(activeforeground="black")
        self.Name.configure(background="#d9d9d9")
        self.Name.configure(disabledforeground="#a3a3a3")
        self.Name.configure(foreground="#000000")
        self.Name.configure(highlightbackground="#d9d9d9")
        self.Name.configure(highlightcolor="black")
        self.Name.configure(text='''Name''')
        self.Name.configure(textvariable=CN_support.name)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.467, rely=0.280, height=20, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.var=tk.StringVar()

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.467, rely=0.380, height=20, relwidth=0.35)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")
        self.Entry2.configure(textvariable=CN_support.name_entry)

        self.Connect = tk.Button(top, command=self.connect)
        self.Connect.place(relx=0.350, rely=0.622, height=24, width=60)
        self.Connect.configure(activebackground="#ececec")
        self.Connect.configure(activeforeground="#000000")
        self.Connect.configure(background="#d9d9d9")
        self.Connect.configure(disabledforeground="#a3a3a3")
        self.Connect.configure(foreground="#000000")
        self.Connect.configure(highlightbackground="#d9d9d9")
        self.Connect.configure(highlightcolor="black")
        self.Connect.configure(pady="0")
        self.Connect.configure(state='normal')
        self.Connect.configure(text='''Connect''')

        self.Quit = tk.Button(top, command=self.qfun)
        self.Quit.place(relx=0.700, rely=0.622, height=24, width=60)
        self.Quit.configure(activebackground="#ececec")
        self.Quit.configure(activeforeground="#000000")
        self.Quit.configure(background="#d9d9d9")
        self.Quit.configure(disabledforeground="#a3a3a3")
        self.Quit.configure(foreground="#000000")
        self.Quit.configure(highlightbackground="#d9d9d9")
        self.Quit.configure(highlightcolor="#e70527")
        self.Quit.configure(pady="0")
        self.Quit.configure(text='''Quit''')

        self.l = tk.Label(text = "Note: IP should be known to access any feature!")
        self.l.place(relx=0.350, rely=0.822, height=24, width=260)

        

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
    

if __name__ == '__main__':
    vp_start_gui()





