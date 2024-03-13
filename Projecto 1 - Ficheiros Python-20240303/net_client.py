"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 17
Números de aluno: 56943 56922
"""
import socket
from sock_utils import *

class net_client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print(f"Connected to server {self.host}:{self.port}")

        except Exception as e:
            print(f"Error connecting to {self.host}:{self.port}: {e}")
            exit

    def recv(self):
        try:
            data = self.socket.recv(1024).decode()
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
    
    def send(self, data):
        try:
            self.socket.sendall(data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def close(self):
        self.socket.close()
            
    def __del__(self): 
        self.socket.close()