"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 17
Números de aluno: 56943 56922
"""
import socket
from sock_utils import *
import pickle, struct

class net_client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.socket = create_tcp_client_socket(self.host, self.port)
        return self.socket 

    def recv(self):
        try:
            data_size = struct.unpack('i', self.socket.recv(4))[0]
            data_bytes = self.socket.recv(data_size)
            data = pickle.loads(data_bytes)
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
    
    def send(self, data):
        try:
            data_bytes = pickle.dumps(data)
            data_bytes_size = struct.pack('i', len(data_bytes))
            self.socket.sendall(data_bytes_size)
            self.socket.sendall(data_bytes)
        except Exception as e:
            print(f"Error sending data: {e}")

    def close(self):
        self.socket.close()
            
    def __del__(self): 
        self.socket.close()