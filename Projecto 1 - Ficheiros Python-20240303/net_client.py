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
        return create_tcp_client_socket(self.host, self.port)

    def recv(self):
        try:
            data = (self.connect().recv(1024)).decode()
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
    
    def send(self, data):
        try:
            conn_sock = self.connect(self.host, self.port)
            conn_sock.sendall(data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def close(self):
        self.socket.close()
            
    def __del__(self): 
        self.socket.close()