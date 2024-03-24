"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 17
Números de aluno: 56943 56922
"""

import sys
from kuko_stub import *


### código do programa principal ###
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kuko_client.py <id_participant> <server_address> <server_port>")
        return
    
    id_participant = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])

    stub = KukoStub(server_address, server_port, id_participant)


    while True:

        #client_socket = create_tcp_client_socket(server_address, server_port)
        #client_socket = netClient.connect()
        stub.connect()
        client_socket = stub.conn_socket

        command = input("comando > ")
        list = command.split(";")

        if list[0] == "EXIT":
            stub.exit()
            stub.disconnect()
            print("Conexão fechada. Adeus!")
            break

        if list[0] == "QUESTION":
            print("Resposta do servidor: " + stub.question(list[1], list[2:-1], list[-1]))
        
        if list[0] == "QSET":
            print("Resposta do servidor: " + stub.qSet(list[1:]))
        
        if list[0] == "QUIZ":
            print("Resposta do servidor: " + stub.quiz(list[1], list[2:]))
        
        if list[0] == "LAUNCH":
            print("Resposta do servidor: " + stub.launch(list[1]))

        if list[0] == "NEXT":
            print("Resposta do servidor: " + stub.next(list[1]))

        if list[0] == "REG":
            print("Resposta do servidor: " + stub.registar(list[1]))

        if list[0] == "GET":
            print("Resposta do servidor: " + stub.get(list[1]))

        if list[0] == "ANS":
            print("Resposta do servidor: " + stub.responde(list[1], list[2]))

        if list[0] == "REL":
            print("Resposta do servidor: " + stub.relatorio(list[1]))    
        

        

        # msg = [id_participant, command] #Ao contrario
        # print("A ENVIAR: " + str(msg))
        # netClient.send(msg)
        # response = netClient.recv()

        # print("Resposta do servidor", response)

if __name__ == "__main__":
    main()