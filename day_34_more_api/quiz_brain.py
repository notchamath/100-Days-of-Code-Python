import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1

        # Unescape html entities
        q_text = html.unescape(curr_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ").lower()

        self.check_answer(user_answer, curr_question.answer)

    def is_more_questions(self):
        return self.question_number < (len(self.question_list))

    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

