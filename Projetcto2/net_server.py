"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Grupo: 17
Números de aluno: 56943 56922
"""
import socket
from sock_utils import *
import pickle, struct

class net_server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.listen_socket = create_tcp_server_socket(host, port, 1)
        self.conn_socket = None
        
    def accept(self):
        (conn_sock,(addr, port)) = self.listen_socket.accept()
        self.conn_socket = conn_sock
        return conn_sock, addr

    def listen(self):
        try:
            self.listen_socket.listen(1) 
        except Exception as e:
            print(f"Error: {e}")
            exit

    def recv(self):
        try:
            data_size = struct.unpack('i', self.conn_socket.recv(4))[0]
            data_bytes = self.conn_socket.recv(data_size)
            data = pickle.loads(data_bytes)
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
    
    def send(self,data):
        try:
            data_bytes = pickle.dumps(data)
            data_bytes_size = struct.pack('i', len(data_bytes))
            if self.conn_socket:
                self.conn_socket.send(data_bytes_size)
                self.conn_socket.send(data_bytes)
            else:
                print("Não existe connection Socket")
        except Exception as e:
            print(f"Error sending data: {e}")

    def closeListenSocket(self):
        self.listen_socket.close()
    
    def closeConnSocket (self):
        self.conn_socket.close()

    def __del__(self):
        self.listen_socket.close()