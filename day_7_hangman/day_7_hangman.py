import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Create blanks for length of the chosen word.
display = []
for _ in range(word_length):
    display += "_"

# Clear console function.
def clear(): os.system('clear')

# Function to join all the elements in the list and turn it into a String & print.
def printWord(): print(f"Your word: {' '.join(display)}")

print(logo)
printWord()

while not end_of_game:
    # Get user input
    guess = input("Guess a letter: ").lower()

    clear()

    # If user had tried that letter before. Account for given letters.
    if guess in display:
        print("You already guessed that letter! Try a different letter.")

    # Check guessed letter.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    printWord()

    # Check if user is wrong.
    if guess not in chosen_word:
        print("That letter is not in this word...")
        lives -= 1
        if lives == 0:
            end_of_game = True
            clear()
            print(f"You lose. Your word was {chosen_word.upper()}")


    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])