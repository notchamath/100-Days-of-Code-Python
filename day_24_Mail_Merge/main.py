# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as original:
    letter = original.read()

with open("./Input/Names/invited_names.txt") as names:
    guests = names.readlines()

for guest in guests:
    trimmed_name = guest.strip()
    new_letter = letter.replace("[name]", trimmed_name)

    with open(f"./Output/ReadyToSend/{trimmed_name}", mode="w") as invitation:
        invitation.write(new_letter)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
