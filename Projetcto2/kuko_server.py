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

        data = KukoServer.recv()
        print("recebeu dados do cliente: " + str(data))

        resp = ["Ack"]
        KukoServer.send(resp)

        # KukoData = kuko_data.Kuko()
        
        # #receber dados do cliente
        # data = KukoServer.recv()
        # print("recebeu dados do cliente: " + str(data))
        # #Processar as operações dadas pelo cliente
        # response = process_request(data, KukoData)

        # # Envia a resposta de volta para o cliente
        # KukoServer.send(response)

        # Fecha a conexão com o cliente
        #KukoServer.close()
       

        #finally:
            # Close the client socket
            #client_socket.close()

def process_request(request, kuko_data):
    if request[0] == "EXIT":
        exit 

    parts = request.split(";")
    id_participant = parts[0]
    operation = parts[1]
    arguments = parts[2:]

    print(id_participant, request)

    if operation == "QUESTION":
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
        points = []
        for p in arguments[1:]:
            points.append(int(p))
        print("Args: " + str(qSet)  + ", " + str(points))
        result = kuko_data.createQuiz(qSet, points)
        return result
    elif operation == "LAUNCH":
        quizz_id = int(arguments[0])
        print("quiz_id = " + str(quizz_id))
        result = kuko_data.start_quiz(quizz_id)
        return result
    elif operation == "REG":
        quizz_id = int(arguments[0])
        result = kuko_data.add_participant(quizz_id, id_participant)
        return result
    elif operation == "GET":
        quizz_id = int(arguments[0])
        result = kuko_data.getQuestion(quizz_id)
        return result
    elif operation == "ANS":
        id_quizz = int(arguments[0])
        n = int(arguments[1])
        result = kuko_data.answer_question(id_quizz, id_participant, n)
        return result
    else:
        return "NOK"

if __name__ == "__main__":
    main()
