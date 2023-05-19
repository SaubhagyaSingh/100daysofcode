class QuizBrain:
    def __init__(self, q_list):
        self.qno = 0
        self.q_list = q_list
        self.score = 0

    def increase_score(self):
        self.score += 1

    def still_has_questions(self):
        return self.qno < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.increase_score()
        else:
            print("Nope :( Wrong answer!")

        print(f"The Correct Answer was: {correct_answer}.")
        print(f"Your Current Score is: {self.score}/{self.qno + 1}")

    def next_question(self):
        current_question = self.q_list[self.qno]
        self.qno += 1
        user_answer = input(f"Q.{self.qno}: {current_question.text} (T/F): ")
        self.check_answer(user_answer, current_question.answer)
