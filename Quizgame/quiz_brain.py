from data import question_data
class QuizBrain:

    def __init__(self,q_list):
        self.question_number=0 #keeps track of question no.
        self.question_list=q_list #stores the list of questions
        self.score=0 #keeps track of score

    def still_has_questions(self):
        if self.question_number <len(question_data): #checks if there are more questions left
            return True
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.question_number] #gets current ques using current ques number
        self.question_number+=1 #move to next ques
        user_answer=input(f"{self.question_number}: {current_question.text} True/False?")
        self.check_answer(user_answer, current_question.answer) #calls another method and checks the user and actual ans


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right")
            self.score+=1 #increases the score

        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
