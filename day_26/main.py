# # List Comprehension
# num = [1, 2, 3]
# new_num = [n*2 for n in num]
# print(new_num)
#
# # String to list using LC
# name = "Kratos"
# letters_list = [letter for letter in name]
# print(letters_list)
#
# # LC with range function
# range_list = [i*5 for i in range(1, 5)]
# print(range_list)
#
# # LC with conditional
# names = ["Harry", "Hermione", "Ron", "Snape", "Dumbledore"]
# short_names = [name for name in names if len(name) < 6]
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
#
#
# # Dictionary Comprehension
# import random
# names = ["Harry", "Hermione", "Ron", "Snape", "Dumbledore"]
# student_scores = {student: random.randint(0, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 70}
# print(passed_students)


# # Iterating over Pandas DataFrame
# import pandas
# student_dict = {
#     "student": ["Harry", "Hermione", "Ron"],
#     "score": [84, 98, 80]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)
#     if row.student == "Harry":
#         print(row.score + 10)

# NATO Alphabet Project
import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

word = input("Enter a word: ").upper()
nato_word = [nato_alphabet[letter] for letter in word if letter in nato_alphabet.keys()]
print(nato_word)
