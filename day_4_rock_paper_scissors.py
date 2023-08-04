rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
0
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_answer > 2 or user_answer < 0:
  print("Invalid answer :(")
  
else:
  computer_answer = random.randint(0, 2)
  
  print(options[user_answer])
  print("Computer chose:\n", options[computer_answer])
  
  if user_answer == computer_answer:
    print("Its a draw!")
  elif (user_answer == 0 and computer_answer == 1) or (user_answer == 1 and computer_answer == 2) or (user_answer == 2 and computer_answer == 0):
    print("You lose...")
  else:
    print("You win!")

