# try block
try:
    file = open("a_file.txt")
    a_dict = {"key": "val"}

    # Throw your own error
    if a_dict.get("wtf") is None:
        raise KeyError("No wayyyyy")


# Handle different errors, can have as many as exceptions
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")

# If none of the exceptions were met (no error)
else:
    content = file.read()
    print(content)

# Executes no matter what happens
finally:
    file.close()
    print("File closed.")
