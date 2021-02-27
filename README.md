# Group-Chat-Video-and-Audio-call
This application integrates 3 main features i.e Group chat, video and audio calling. Go through the "order of execution" before executing the files.


Order of Execution:

Servers should run to accept requests from all the clients. So, the servers to run before client can connect are: GChatServer.py, FileUploadServer.py, FileDownloadServer.py (in Servers folder) and serverMedia.py (in VideoChat folder).
Once all the servers are ready, Client.py (in root folder) should be executed to connect with servers that are specific to user needs.

IP addresses for serverMedia.py and Audio_server.py files should be explicitly typed while executing. The IP address given is same as computer’s local IP.

Note: All files are written in Python. Also, install necessary modules by going through the files.

