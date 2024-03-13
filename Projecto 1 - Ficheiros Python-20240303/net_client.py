"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: XX
Números de aluno: XXXXX XXXXX
"""
import socket
from sock_utils import *

class net_client:
    def __init__(self, host, port):
        self.host = host 
        self.port = port 
     
    def connect(self):
        return create_tcp_client_socket(self.host, self.port)

    def recv(self):
        return self.connect().recv(1024) #Vai receber 1024bits
    
    def send(self, data):
        conn_sock = self.connect(self.host, self.port)
        conn_sock.sendall(data)

    def close(self):
        ...
            
    def __del__(self): 
        ...
