"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 17
Números de aluno: 56943 56922
"""
import time
import copy
from typing import Dict, List, Tuple

class Question:
    """Question Class
    id (int) - id 
    question (String) - Question
    answers (List of Strings) - Possible Answers 
    k (int) - right answer 
    """
    questionIdCounter = 0

    def __init__(self, question, answers, k):
        if k - 1 < len(answers):
            Question.questionIdCounter += 1
            self.id = Question.questionIdCounter 
            self.question = question
            self.answers = answers
            self.k = k
        else:
            raise Exception("k is not a valid answer index")

    def __str__(self):
        return str("Question id: " + str(self.id) + "\n" +
             "Question: " + self.question + "\n" +
             "Possible answers: " + str(self.answers) + "\n" +
             "Correct answer: " + str(self.answers[self.k - 1]))

class QSet:
    """QSet class:
    id (int) - id 
    questions (list of questions) - list of questions
    """    
    qSetIdCounter = 0 
    def __init__(self, questions):
        QSet.qSetIdCounter += 1
        self.qSetId = QSet.qSetIdCounter
        self.questions = questions

    def __str__(self):
        return str("QSet id: " + str(self.qSetId) + "\n" +
              "Questions : " + str(self.questions))

class Quiz:
    """Quiz class:

    """
    quizIdCounter = 0
    def __init__(self, QSet, pontos):
        Quiz.quizIdCounter +=1
        self.id_quiz = Quiz.quizIdCounter
        self.Qset = QSet
        self.questions = QSet.questions
        self.pontos = pontos
        self.state = "PREPARED"

        self.participants = []
        self.replies = {}
        self.timestamp_p = int(time.time())
        self.timestamp_e = -1 #-1 = ainda não esta ENDED
        self.question_i = self.questions[0] #question atual inicializada á primeira do qSet escolhido 

    def add_participant (self, participant_id):
        self.participants.append(participant_id)
        self.replies[participant_id] = [] #Inicializa a lista das respostas de um participante

    def start_quiz(self):
        self.state = "ONGOING"

    def end_quiz(self):
        self.state = "ENDED"
        self.timestamp_e = int(time.time())

    def get_question (self):
        return self.question_i.__str__()
    
    def answer_question(self, participant_id, n):
        if participant_id in self.participants:
            question_i_index = self.questions.index(self.question_i)
            if len(self.questions) > question_i_index + 1: #Caso não for a ultima pergunta
                self.replies[participant_id].append(n) #append da resposta
                return "OK"

            elif len(self.questions) == question_i_index + 1: #Caso seja a ultima:
                self.replies[participant_id].append(n)#append da resposta
                #Calcular os pontos
                for i in range(len(self.questions)):
                    points = 0 
                    if self.questions[i].k == self.replies[participant_id][i]:
                        points += self.pontos[i]
                self.end_quiz() #Acaba o quiz
                return (participant_id, points)  #Retorna o id do participante e os pontos do jogador


    def __str__(self):
        return str("Quizz id: " + str(self.id_quiz) + "\n" +
              "QSet: " + str(self.Qset) + "\n" +
              "Questions in qSet: " + str(self.questions) + "\n" +
              "Pontos: " + str(self.pontos))


class Kuko:
   
    Questions = {}
    QSets = {}
    Quizes = {}
    
    def __init__(self):
       pass

    def createQuestion(question, answers, k):
       newQ = Question(question, answers, k)
       Kuko.Questions[newQ.id] = newQ
       return newQ
    
    def createQSet(questions):
        questionsToAdd = []
        for i in questions:
            if i in Kuko.Questions:
                questionsToAdd.append(Kuko.Questions[i])

        newQSet = QSet(questionsToAdd)
        Kuko.QSets[newQSet.qSetId] = newQSet
        return newQSet
    
    def createQuiz(qSet, points):
        newQuiz = Quiz(Kuko.QSets[qSet], points)
        Kuko.Quizes[newQuiz.id_quiz] = newQuiz
        return newQuiz

    def add_participant (quiz_id, participant_id):
        if quiz_id in Kuko.Quizes.keys():
            Kuko.Quizes[quiz_id].add_participant(participant_id)
    
    def __str__():
        return str(str(Kuko.Questions) + "\n" + 
              str(Kuko.QSets) + "\n" +
              str(Kuko.Quizes[2].participants))

#Tests 
#Assumo que recebemos o participant_id do cliente 

Kuko.createQuestion("What is my name?", ["Manel", "Antonio", "João"], 1)
Kuko.createQuestion("Where do I live?", ["Lisbon", "Porto"], 1)
Kuko.createQuestion("Where do I want to live?", ["Lisbon", "Porto", "Dubai"], 3)

Kuko.createQSet([1,2])
Kuko.createQSet([1,2,3])

Kuko.createQuiz(1,[20,80])
Kuko.createQuiz(2,[20,20,60])

Kuko.add_participant(1,12345)
Kuko.add_participant(1,98867)
Kuko.add_participant(2,12345)

print(Kuko.__str__())


# question1 = Question("What is my name?", ["Manel", "Antonio", "João"], 1)
# question2 = Question("Where do I live?", ["Lisbon", "Porto"], 1)
# question3 = Question("Where do I study?", ["FCUL", "FDUL", "FLUL"], 1)

# qSet1 = QSet([question1.id, question2.id])


# question1.__str__()
# print("-------------------")
# question2.__str__()
# print("-------------------")
# question3.__str__()
# print("-------------------")
# print("-------------------")
# qSet1.__str__()

    

