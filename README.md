# Group-Chat-Video-and-Audio-call
This application combines three key functionalities: group chat, video calling, and audio calling. Please follow the specified "order of execution" steps before running the application.

Execution Order:

1. Start the servers to handle requests from clients. The servers that need to be initiated before clients can connect are: GChatServer.py, FileUploadServer.py, FileDownloadServer.py (located in the Servers folder), and serverMedia.py (found in the VideoChat folder).
2. Once all the servers are operational, execute Client.py (located in the root folder) to establish connections with servers tailored to user requirements.
3. When executing serverMedia.py and Audio_server.py files, be sure to explicitly input the IP addresses. The provided IP address is the same as the computer's local IP.

Note: All files are coded in Python. Additionally, make sure to install the necessary modules by reviewing the content of the files.

