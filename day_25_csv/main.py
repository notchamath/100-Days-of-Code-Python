# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


# import pandas
#
# # In Pandas, DataFrame is the whole sheet, DataSeries is a column of data
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows
# print(data[data.day == "Monday"])
# # Get the row of data where the temp was the highest
# print(data[data.temp == data.temp.max()])
#
# # Create a dataframe from scratch
# data_students = {
#     "students": ["amy", "james", "harry"],
#     "scores": [99, 73, 77]
# }
#
# data = pandas.DataFrame(data_students)
# data.to_csv("student_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = data["Primary Fur Color"]

gray_sq = data[squirrel_color == "Gray"]
gray_sq_count = len(gray_sq)
print(gray_sq_count)

red_sq = data[squirrel_color == "Cinnamon"]
red_sq_count = len(red_sq)
print(red_sq_count)

black_sq = data[squirrel_color == "Black"]
black_sq_count = len(black_sq)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq_count, red_sq_count, black_sq_count]
}

sq_df = pandas.DataFrame(data_dict)
sq_df.to_csv("central_park_squirrel_counts_2018.csv")
