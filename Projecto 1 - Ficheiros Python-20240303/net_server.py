"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Grupo: XX
Números de aluno: XXXXX XXXXX
"""
import socket
from sock_utils import *

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def accept(self):
        self.socket = create_tcp_server_socket(self.host, self.port)

    def listen(self):
        try:
            self.socket.listen(1) 
        except Exception as e:
            print(f"Error: {e}")
            exit

    def recv(self):
        try:
            data = self.socket.recv(1024).decode()
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
    
    def send(self,texto):
        try:
            data = self.socket.sendall(texto.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def close(self):
        self.socket.close()

    def __del__(self):
        self.socket.close()