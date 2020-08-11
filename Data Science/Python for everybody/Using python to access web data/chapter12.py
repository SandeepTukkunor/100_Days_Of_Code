import socket
mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysoc.connect(("data.pr4e.orf", 80))
