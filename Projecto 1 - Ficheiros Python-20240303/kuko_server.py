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
        data = KukoServer.recv()

        #Processar as operações dadas pelo cliente
        response = process_request(data, KukoData)

        # Envia a resposta de volta para o cliente
        KukoServer.send(response)

        # Fecha a conexão com o cliente
        KukoServer.close()
   

def process_request(request, kuko_data):
    try:
        parts = request.strip().split(";")
        operation = parts[0]
        arguments = parts[1:]

        if operation == "EXIT":
            exit
        elif operation == "QUESTION":
            result = kuko_data.createQuestion(*arguments)
            return result
        elif operation == "QSET":
            result = kuko_data.createQSet(*arguments)
            return result
        elif operation == "QUIZ":
            result = kuko_data.createQuiz(*arguments)
            return result
        elif operation == "LAUNCH":
            result = kuko_data.start_quiz(*arguments)
            return result
        elif operation == "REG":
            result = kuko_data.add_participant(*arguments)
            return result
        elif operation == "GET":
            result = kuko_data.getQuestion(*arguments)
            return result
        elif operation == "ANS":
            result = kuko_data.answer_question(*arguments)
            return result
        else:
            return "NOK"
    except Exception as e:
        return f"Error processing your request: {str(e)}"

if __name__ == "__main__":
    main()
