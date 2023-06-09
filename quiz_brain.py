class  QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def still_has_Question(self):
        return self.question_number<len(self.question_list)

        
    def check_answer(self,user_answer,correct_answer):
        global score
        if user_answer.lower()==correct_answer.lower():
            print("Great! Your answer is correct.")
            self.score+=1
        else:
            print("Sorry! Your answer is Wrong.")
        print(f"The Correct answer is {correct_answer}.")
        print(f"Your Score is {self.score}/{self.question_number}")


    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.no {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)