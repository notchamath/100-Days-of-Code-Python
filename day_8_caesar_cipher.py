logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    # Decode shift will be in negative direction
    if cipher_direction == "decode":
        shift_amount *= -1

    # Each letter in start text is checked
    for char in start_text:

        # Symbols and numbers are skipped
        if char not in alphabet:
            end_text += char
            continue

        # Each letter is shifted accordingly
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

# Do-while loop
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # If direction input isnt "encode" or "decode" restart loop
    if direction != "encode" and direction != "decode":
        continue
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # Account for large shift numbers
        shift = shift % int(len(alphabet)/2)
        
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Type \"yes\" to go again.\n").lower()

    # Do-while break condition
    if restart != "yes":
        print("Goodbye.")
        break