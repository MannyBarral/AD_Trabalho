"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 17
Números de aluno: 56943 56922
"""
import time
import copy
from typing import Dict, List, Tuple

questionIdCounter = 0

class Question:
    """Question Class
    id (int) - id 
    question (String) - Question
    answers (List of Strings) - Possible Answers 
    k (int) - right answer 
    """
    def __init__(self, question, answers, k):
        self.id = questionIdCounter + 1
        self.question = question
        self.answers = answers
        self.k = k
       

    def __str__(self):
        print("Question id: " + self.id + "\n" +
              "Question: " + self.question)
        
    

   ...

class QSet:
    def __init__(self, ...):
        self ...

    ....
        

class Quiz:
    ...

    def __init__(self, ...):
        self ....

    

    def __str__(self):
        ...
        return ..

    ...         
      


class Kuko:
    
    def __init__(self):
        self ...

   ...
   


     
        


    

