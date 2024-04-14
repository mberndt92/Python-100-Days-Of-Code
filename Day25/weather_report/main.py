
# import csv
# Weather Report

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)
#         print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data=data_dict)
data.to_csv("new_data.csv")