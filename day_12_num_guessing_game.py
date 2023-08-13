import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Get difficulty from user
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        break

# Attempts left
attempts = 10
if difficulty == "hard": attempts = 5

# Random number
NUM = random.randint(1, 100)

def play(NUM, attempts):
    
    is_game_over = False

    while not is_game_over:

        if attempts > 0:
            print(f"You have {attempts} left.")
            guess = int(input("Make a guess: "))
            attempts -= 1
            
            if NUM < guess:
                print("Too High.")
            elif NUM > guess:
                print("Too low.")
            else:
                print(f"You got it! The answer is {NUM}!")
                is_game_over = True
        else:
            print("You have run out of attempts. You lose.")
            print(f"The correct number was {NUM}.")
            is_game_over = True

play(NUM, attempts)