# TODO aking question
# TODO checking if the anwer was correct
# TODO checking if we are at the end of the quiz

class QuizBrain:
    def __init__(self, question_list ):
        self.question_number = 0
        self.question_list = question_list
        self.score =0

    def next_question(self):
        ques_list = self.question_list
        ques_number= self.question_number
        question_text = ques_list[ques_number].text
        question_answer = ques_list[ques_number].answer
        self.question_number +=1
        user_response = input (f"Q.{self.question_number}: {question_text} (True/False)?: ")

        self.check_answer(user_response, question_answer)       


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_response, ques_answer):
        if user_response.lower() == ques_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("You got it wrong.")
        print (f"Correct answers is: {ques_answer}")
        print (f"Your score is: {self.score}/{self.question_number}")
        print("\n")






# correct_answers=0
# wrong_answers=0 

# for index, question in enumerate(question_bank):
#     question_text =question.text
#     question_answer =question.answer

#     user_response = input (f"Q.{index+1}: {question_text} (True/False)?:")
#     if user_response.lower() == question_answer.lower():
#         print("You are correct.")
#         correct_answers+=1
#     else:
#         print("You're wrong. Lets try next...")
#         wrong_answers+=1

# print(f"You have given {correct_answers} correct answers and {wrong_answers} wrong answers.")