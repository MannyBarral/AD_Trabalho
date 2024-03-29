"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Grupo: 17
Números de aluno: 56943 56922
"""

import socket as s

def create_tcp_server_socket(address, port, queue_size=1):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM) #TCP lig.
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.bind((address, port))
    sock.listen(queue_size)
    return sock

def create_tcp_client_socket(address, port):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((address, port))
    return sock

