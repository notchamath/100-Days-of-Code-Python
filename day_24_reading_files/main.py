# # Read File using open, remember to close file.
# file = open("my_file.txt")
# contents = file.read()
# file.close()
#
# print(contents)


# # Keywords with + as closes file automatically
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# mode='a': append | mode='w': delete everything and write new
# when writing to a file if file doesn't exist, python will make a file for you
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

