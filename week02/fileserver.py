# File transfer server program
import socket
from pathlib import Path
from struct import unpack


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            len_info = conn.recv(4)   #获取文件名长度信息
            len_name = unpack("i", len_info)[0]  #解析文件名
            filename = conn.recv(len_name).decode()
            filename = "new" + filename
            with open(filename, "wb") as f:
                while True:
                    data = conn.recv(1024)
                    if data:
                        f.write(data)
                    else:
                        break
