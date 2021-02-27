import socket
import tqdm
import os


class fileTrans:
    def send(self, fname):
        self.SEPARATOR = "<SEPARATOR>"
        self.BUFFER_SIZE = 4096 # send 4096 bytes each time step

        self.host = "127.0.0.2"
        self.port = 5010
        self.filename = fname
        self.filesize = os.path.getsize(self.filename)

        self.s = socket.socket()
        print(f"[+] Connecting to {self.host}:{self.port}")
        self.s.connect((self.host, self.port))
        print("[+] Connected.")
        self.s.send(f"{self.filename}{self.SEPARATOR}{self.filesize}".encode())

        self.progress = tqdm.tqdm(range(self.filesize), f"Sending {self.filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(self.filename, "rb") as f:
            for _ in self.progress:
                self.bytes_read = f.read(self.BUFFER_SIZE)
                if not self.bytes_read:
                    break
                self.s.sendall(self.bytes_read)
                self.progress.update(len(self.bytes_read))
        
        self.s.close()

def func(fname):
    FT = fileTrans()
    FT.send(fname)
