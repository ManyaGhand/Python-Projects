from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


Question_bank=[]

for question in question_data:  #looping through the text in question data
    question_text=question["text"] #storing the text into "question_text" variable
    question_answer=question["answer"]
    new_question=Question(q_text=question_text,q_answer=question_answer)
    #storing the text and answer into new question variable
    Question_bank.append(new_question) #adding the new question to question bank list


quiz= QuizBrain(Question_bank) #calling the constructor
#This whole thing is also called naming the object
#quiz will contain all the data and functions called methods
#quiz-->object name
#quizbrain=()-->calling the class to create an object
#question_bank is the list we created and has been appended with the text and answer from question data

quiz.next_question()
#the object quiz created from class and accesses the next_question block from QuizBrain

can_run=True
while can_run:
    if quiz.still_has_questions(): #runs till the quiz has questions
        quiz.next_question()
    else:
        can_run=False

print("\n")
if quiz.question_number==12:
    print("You have completed the game.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")