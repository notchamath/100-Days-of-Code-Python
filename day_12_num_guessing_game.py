import random

# Difficulty Levels
ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

# Random number
NUM = random.randint(1, 100)

# Welcome message
def welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

# Get difficulty from user
def get_difficulty():
    
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy" or difficulty == "hard":
            break
    
    if difficulty == "easy": return ATTEMPTS_EASY
    return ATTEMPTS_HARD

# Start game
def play():
    welcome_msg()

    attempts = get_difficulty()
    
    is_game_over = False

    while not is_game_over:

        if attempts > 0:
            print(f"You have {attempts} guesses left.")
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

play()