# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 09:46:10 2025

@author: BeRoberts
"""

import socket

HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall(b'Howdy! welcome to the home port.\r\n')
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)