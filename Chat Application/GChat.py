import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import FileClient
import webbrowser

class GUI:
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)
                if message != 'NICK':
                    self.textCons.config(state = NORMAL)
                    temp = message.split()
                    if temp[0]==self.name and temp[1]!="joined!":
                        self.textCons.insert(END,  
                                         "(Myself)"+message+"\n\n")
                    else:
                        self.textCons.insert(END,  
                                         message+"\n\n") 
                      
                    self.textCons.config(state = DISABLED) 
                    self.textCons.see(END) 
                else:
                    client.send(self.name.encode(FORMAT))

            except:
                print("Error!")
                client.close()
                break
    def __init__(self,nm):
        self.window=Tk()
        self.window.withdraw()
        self.goAhead(nm)
        self.window.mainloop()

    def goAhead(self, name):
        #self.login.destroy()
        self.layout(name)

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def layout(self,name):
        self.name = name 
        # to show chat window 
        self.window.deiconify() 
        self.window.title("Group Chat") 
        self.window.resizable(width = False, 
                              height = False) 
        self.window.configure(width = 470, 
                              height = 530, 
                              bg = "#17202A") 
        self.labelHead = Label(self.window, 
                             bg = "lawn green",  
                              fg = "black", 
                              text = self.name , 
                               font = "Times 14", 
                               pady = 5) 
          
        self.labelHead.place(relwidth = 1) 
        self.line = Label(self.window, 
                          width = 450, 
                          bg = "#ABB2B9") 
          
        self.line.place(relwidth = 1, 
                        rely = 0.07, 
                        relheight = 0.012) 
          
        self.textCons = Text(self.window, 
                             width = 20,  
                             height = 3, 
                             bg = "goldenrod", 
                             fg = "#EAECEE", 
                             font = "Times 14",  
                             padx = 5, 
                             pady = 5) 
          
        self.textCons.place(relheight = 0.745, 
                            relwidth = 1,  
                            rely = 0.07) 
          
        self.labelBottom = Label(self.window, 
                                 bg = "#ABB2B9", 
                                 height = 80) 
          
        self.labelBottom.place(relwidth = 1, 
                               rely = 0.9) 
          
        self.entryMsg = Entry(self.labelBottom, 
                              bg = "mint cream", 
                              fg = "black", 
                              font = "Times 12")
        
        self.entryMsg.place(relwidth = 0.74, 
                            relheight = 0.025, 
                            rely = 0.008, 
                            relx = 0.008) 
          
        self.entryMsg.focus()
          
        # place the given widget 
        # into the gui window

        self.buttonDoc = Button(self.window, 
				text = "Browse", 
                                font = "Nyala 10",  
                                width = 20, 
                                bg = "#ABB2B9",
                                command = self.first_browser) 
          
        self.buttonDoc.place(relx = 0.015, 
                             rely = 0.83, 
                             relheight = 0.06,  
                             relwidth = 0.20)

        self.buttonDown = Button(self.window, 
				text = "Download", 
                                font = "Nyala 10",  
                                width = 20, 
                                bg = "#ABB2B9",
                                command = self.download) 
          
        self.buttonDown.place(relx = 0.785, 
                             rely = 0.83, 
                             relheight = 0.06,  
                             relwidth = 0.20) 
          
        # create a Send Button 
        self.buttonMsg = Button(self.labelBottom, 
                                text = "Send", 
                                font = "Times 10",  
                                width = 20, 
                                bg = "#ABB2B9", 
                                command = lambda : self.sendButton(self.entryMsg.get())) 
          
        self.buttonMsg.place(relx = 0.77, 
                             rely = 0.008, 
                             relheight = 0.025,  
                             relwidth = 0.22) 
          
        self.textCons.config(cursor = "arrow") 
          
        # create a scroll bar 
        scrollbar = Scrollbar(self.textCons) 
          
        # place the scroll bar  
        # into the gui window 
        scrollbar.place(relheight = 1, 
                        relx = 0.974) 
          
        scrollbar.config(command = self.textCons.yview) 
          
        self.textCons.config(state = DISABLED)
        
    def sendButton(self, msg): 
        self.textCons.config(state = DISABLED)
        self.msg=msg 
        self.entryMsg.delete(0, END) 
        snd= threading.Thread(target = self.sendMessage) 
        snd.start()     

    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name} : {self.msg}")
            client.send(message.encode(FORMAT))
            break

    def show_file_browser(self):
        self.filename = filedialog.askopenfilename()
        return self.filename

    def first_browser(self):
        file = self.show_file_browser()
        FileClient.func(file)
        self.textCons.config(state = NORMAL)
        self.textCons.insert(END,"(Uploaded Successfully)"+"\n\n")
        self.textCons.config(state = DISABLED)

    def download(self):
        webbrowser.open('ftp://localhost:2121')
        

FORMAT = "utf-8"

def func(ip,name): 
    global host
    host=ip
    global nick
    nick=name
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 5000))
    g = GUI(nick)
