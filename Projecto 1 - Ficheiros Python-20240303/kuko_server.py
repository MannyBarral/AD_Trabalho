"""
Aplicações Distribuídas - Projeto 1 - kuko_server.py
Grupo: 17
Números de aluno: 56943 56922
"""

import sys
from net_server import *
import kuko_data



### código do programa principal ###
def main():
    
    if len(sys.argv) != 3:
        print("Execute python3 kukoserver.py <host> <port>")
        
    host = sys.argv[1]
    port = int(sys.argv[2])

    KukoServer = Server(host,port)

    print("The Kuko server is running...")


    
    while True:
        (client_socket, client_address) = KukoServer.accept()

        print(f"Connection created with {client_address}")

        KukoData = kuko_data.Kuko()
        
        #receber dados do cliente
        data = KukoServer.recv()
        print("recebeu dados do cliente: " + str(data))
        #Processar as operações dadas pelo cliente
        response = process_request(data, KukoData)

        # Envia a resposta de volta para o cliente
        KukoServer.send(response)

        # Fecha a conexão com o cliente
        #KukoServer.close()
       

        #finally:
            # Close the client socket
            #client_socket.close()

def process_request(request, kuko_data):
    
    parts = request.split(";")
    operation = parts[0]
    arguments = parts[1:]

    if operation == "EXIT":
        exit
    elif operation == "QUESTION":
        answers = arguments[1:-1]
        k = arguments[-1]            
        result = kuko_data.createQuestion(arguments[0], answers, int(k))
        return result
    elif operation == "QSET":
        #Erro de id not int !!!
        question_ids = []
        for string in arguments:
            question_ids.append(int(string))
        result = kuko_data.createQSet(question_ids)
        return result
    elif operation == "QUIZ":
        qSet = int(arguments[0])
        points = arguments[1:]
        print("Args: " + str(qSet)  + ", " + str(points))
        result = kuko_data.createQuiz(qSet, points)
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

if __name__ == "__main__":
    main()
