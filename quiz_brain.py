class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"



    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



    def answer_true(self) -> bool:
        user_answer = True
        if user_answer == self.check_answer("True"):
            self.next_question()
            return True
        else:
            self.next_question()
            return False

    def answer_false(self) -> bool:
        user_answer = False
        if user_answer == self.check_answer("False"):
            self.next_question()
            return True
        else:
            self.next_question()
            return False
