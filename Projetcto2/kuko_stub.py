"""
Aplicações Distribuídas - Projeto 2 - kuko_stub.py
Grupo: 17
Números de aluno: 56943 56922
"""
from net_client import *
class KukoStub:
    
    def __init__(self, host, port, idCli):
        self.host = host 
        self.port = port
        self.id = idCli

        self.conn_socket = None 

        self.nc = net_client(self.host, self.port)

    def connect(self):
       self.conn_socket = self.nc.connect()
    
    def disconnect(self):
        if self.nc != None:
            self.nc.close()
            self.conn_socket = None
        
    #Funcionalidades:
    
    def exit (self):
        resp= ["EXIT", self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()
    
    #Gestor:
    def question (self, pergunta, listaRespostas, k):
        resp = [10,pergunta]
        for i in listaRespostas:
            resp.append(i)
        resp.append(k)
        resp.append(self.id)
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        serverResp = self.nc.recv()
        return serverResp

    def qSet(self, listaPerguntas):
        resp = [20, "QSET"]
        for i in listaPerguntas:
            resp.append(i)
        resp.append(self.id)
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        serverResp = self.nc.recv()
        return serverResp
    
    def quiz (self, qSet, points):
        resp = [30, qSet]
        for p in points:
            resp.append(p)
        resp.append(self.id)
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        serverResp = self.nc.recv()
        return serverResp
    
    def launch (self, quiz):
        resp = [40, quiz, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()
    
    def next (self, quiz):
        resp = [50, quiz, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()

    #Particiante:
    def registar (self, quiz):
        resp = [60, quiz, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv

    def get (self, quiz):
        resp = [70, quiz, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()
    
    def responde (self, quiz, n):
        resp = [80, quiz, n, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()
    
    def relatorio (self, quiz):
        resp = [90, quiz, self.id]
        print("SENDING: " + str(resp))
        self.nc.send(resp)
        return self.nc.recv()

        
    
    

        