import socket
import threading
import pyaudio
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import time


class Client:
      
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window1.quit()
            self.window1.destroy()
            sys.exit()
            

    def __init__(self,IP):
        self.flag = True
        self.ip = IP
        
        self.win_thread = threading.Thread(target = self.window)
        self.win_thread.start()
        
        self.tkthread()

    def close(self):
        self.flag = False

    def window(self):
        self.window1 = Tk(className='Audio Call')

        self.lbl = tkinter.Label(self.window1, text="You are on a audio chat now...")
        self.lbl.place(x=10,y=10)

        self.lbl = tkinter.Label(self.window1, text="Click here to stop the audio chat and then close the frame!")
        self.lbl.place(x=10,y=30)

        self.bt = tkinter.Button(self.window1, text="STOP", command=self.close)
        self.bt.place(x=140,y=100)
        
        self.window1.geometry("340x200")
        self.window1.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window1.mainloop()

    def receive_server_data(self):
        while True:
            try:
                if not self.flag:
                    break
                data = self.s.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    def tkthread(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                #self.target_ip = input('Enter IP address of server --> ')
                self.target_ip = self.ip
                self.target_port = 20000

                self.s.connect((self.target_ip, self.target_port))

                break
            except:
                print("Couldn't connect to server")

        chunk_size = 1024 # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)

        # start threads
        self.receive_thread = threading.Thread(target=self.receive_server_data).start()
        self.send_data_to_server()

    def send_data_to_server(self):
        while True:
            try:
                if not self.flag:
                    break
                data = self.recording_stream.read(1024)
                self.s.sendall(data)
            except:
                pass

def func(IP):
    ip = IP
    client = Client(ip)

