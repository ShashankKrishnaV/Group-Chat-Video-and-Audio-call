import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    try:
        authorizer = DummyAuthorizer()

        #authorizer.add_anonymous(os.getcwd())

        authorizer.add_anonymous(os.getcwd() + '\\Files')

        handler = FTPHandler

        handler.authorizer = authorizer
        handler.banner = "pyftpdlib based ftpd ready."
        address = ('localhost', 2121)
        server = FTPServer(address, handler)
        # limit of connections
        server.max_cons = 256
        server.max_cons_per_ip = 5

        server.serve_forever()

    except:
        print("Exception occured!")

main()
