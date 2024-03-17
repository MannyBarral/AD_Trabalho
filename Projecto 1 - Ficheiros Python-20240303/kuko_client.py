"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 17
Números de aluno: 56943 56922
"""

import sys
from net_client import *

### código do programa principal ###
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kuko_client.py <id_participant> <server_address> <server_port>")
        return
    
    id_participant = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])

    try:

        while True:

            client_socket = create_tcp_client_socket(server_address, server_port)
            command = input("comando > ")

            if command == "EXIT":
                client_socket.sendall([id_participant.encode(), command.encode()])
                client_socket.close()
                print("Conexão fechada. Adeus!")
                break

            print("input != 'EXIT' ")
            msg = str(id_participant+";"+command)
            client_socket.sendall(msg.encode())
            response = client_socket.recv(1024).decode()

            print("Resposta do servidor", response)

    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()