import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.curr_question = self.question_list[self.question_number]

    def next_question(self):
        self.curr_question = self.question_list[self.question_number]

        # Unescape html entities
        q_text = html.unescape(self.curr_question.text)
        return f"Q.{self.question_number + 1}: {q_text}"

        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ").lower()
        # self.check_answer(user_answer, curr_question.answer)

    def is_more_questions(self):
        return self.question_number < (len(self.question_list))

    def check_answer(self, user_answer):
        answer = self.curr_question.answer
        self.question_number += 1
        if user_answer == answer:
            self.score += 1
            return True
        else:
            return False
