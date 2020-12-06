# File transfer client program
from pathlib import Path
from struct import pack
import socket

filename = input("Please input correct filename : ").strip()
p = Path(filename)
basename = p.name  #获取文件名
len_info = pack("i", len(basename.encode())) #文件名长度信息

HOST = '127.0.0.1'   # The remote host
PORT = 50007         # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(len_info)
    s.sendall(basename.encode())
    with open(filename, "rb") as f:
        while True:
            data = f.read(1024)
            if data:
                s.sendall(data)
            else:
                break