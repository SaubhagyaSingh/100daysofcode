from question_model import Question
from data import *
from quiz_brain import QuizBrain

question_bank = []
for question in question_data1:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions() != 0:
    quiz.next_question()
    print("\n")

print("You have reached the End of this Quiz")
print(f"Your Final Score is {quiz.score}/{quiz.qno}")
