import sys
import net_server
import kuko_data



def main():
    pass

    if len(sys.argv) != 3:
        print("Execute python3 kukoserver.py <host> <port>")
        return None
            
    host = sys.argv[1]
    port = int(sys.argv[2])

    KukoServer = net_server.Server(host,port)

    print("The Kuko server is running...")

    while True():
        (client_socket, client_address) = KukoServer.accept()

        print(f"Connection created with {client_address}")

        KukoData = kuko_data.Kuko()

        data = KukoServer.recv()
        print("recebeu dados do cliente: " + str(data))

        msg = data.split(";")
        op = data[0]
        args = data[1:]

        if op == "QUESTION":
            answers = args[1:-1]
            k = args[-1]         
            KukoData.createQuestion()

if __name__ == "__main__":
    main()