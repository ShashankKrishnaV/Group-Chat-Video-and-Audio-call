import socket
import tqdm
import os
import threading
SERVER_HOST = "127.0.0.2"
SERVER_PORT = 5010
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def handle(client_socket):
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)

    filename = os.getcwd() + "\\Files\\" + filename

    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for _ in progress:
                # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    client_socket.close()

def rec():
    while True:
        client_socket, address = s.accept() 
        print(f"[+] {address} is connected.")

        thread = threading.Thread(target=handle, args=(client_socket,))
        thread.start()
        
rec()
