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
        print("Question id: " + str(self.id) + "\n" +
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
        print("QSet id: " + str(self.qSetId) + "\n" +
              "Questions : " + str(self.questions))

class Quiz:
    """Quiz class:

    """
    quizIdCounter = 0
    def __init__(self, QSet, pontos):
        Quiz.quizIdCounter +=1
        self.id_quiz = Quiz.quizIdCounter
        self.Qset = QSet
        self.question_set = QSet.questions

        

    

#     def __str__(self):
#         ...
#         return ..

#     ...         
      


class Kuko:
   
    Questions = {}
    QSets = {}
    
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
    
    def createQuiz():
        pass

    
    def __str__():
        print(str(Kuko.Questions) + "\n" + 
              str(Kuko.QSets))

 




#Tests 

Kuko.createQuestion("What is my name?", ["Manel", "Antonio", "João"], 1).__str__()
Kuko.createQuestion("Where do I live?", ["Lisbon", "Porto"], 1).__str__()
Kuko.createQuestion("Where do I want to live?", ["Lisbon", "Porto", "Dubai"], 3).__str__()

Kuko.createQSet([1,2]).__str__()

Kuko.__str__()


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

    

