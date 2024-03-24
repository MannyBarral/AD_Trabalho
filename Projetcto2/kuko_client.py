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

    netClient = net_client(server_address, server_port)


    try:

        while True:

            #client_socket = create_tcp_client_socket(server_address, server_port)
            client_socket = netClient.connect()

            command = input("comando > ")

            if command == "EXIT":
                netClient.send([id_participant.encode(), command.encode()])
                netClient.close()
                print("Conexão fechada. Adeus!")
                break

            print("input != 'EXIT' ")
            msg = [id_participant, command] #Ao contrario
            netClient.send(msg)
            response = netClient.recv()

            print("Resposta do servidor", response)

    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()