"""
Aplicações Distribuídas - Projeto 1 - kuko_server.py
Grupo: 17
Números de aluno: 56943 56922
"""

import sys
from net_server import *
from kuko_data import *


### código do programa principal ###
def main():
    
    if len(sys.argv) != 3:
        print("Execute python3 kukoserver.py <host> <port>")
        return
    
    host = sys.argv[1]
    port = int(sys.argv[2])

    KukoServer = Server(host,port)
    KukoData = Kuko()

    print("The Kuko server is running...")
    
    while True:
        client_socket, client_address = KukoServer.accept()

        print(f"Connection created with {client_address}")

        #receber dados do cliente
        data = KukoServer.recv(client_socket)

        #Processar as operações dadas pelo cliente
        response = KukoData.process_command(data)

        # Envia a resposta de volta para o cliente
        KukoServer.send(client_socket, response)

        # Fecha a conexão com o cliente
        KukoServer.close(client_socket)
   
if __name__ == "__main__":
    main()
