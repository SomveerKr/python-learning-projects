from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# all_questions = []

# for question in question_data:
#     # print(question)
#     new_question = Question(question["text"], question["answer"])
#     all_questions.append(new_question)
question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz_brain = QuizBrain(question_bank)
# quiz_brain.next_question()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")