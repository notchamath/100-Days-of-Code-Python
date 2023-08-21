## CLASS EXAMPLE

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user1 = User("001", "Rock")
#
# print(user1.username)


#############################################################

## TRUE FALSE GAME

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.is_more_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
