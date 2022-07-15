import socket

hostname = socket.gethostname()
ipAddress =socket.gethostbyname(hostname)
print(ipAddress)
