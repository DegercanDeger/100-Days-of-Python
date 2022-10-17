# with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
#  print(data)


# mport csv

# with open("weather_data.csv")as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for temperature in data:
#       if temperature[1] != "temp":
#           temperatures.append(temperature[1])
#   print(temperatures)


import pandas

data = pandas.read_csv("squirrel_count.csv")
print(data.Primary_Fur_Color)

black = data[data.Primary_Fur_Color == "Black"]
cinnamon = data[data.Primary_Fur_Color == "Cinnamon"]
gray = data[data.Primary_Fur_Color == "Gray"]

data1 = pandas.DataFrame(black, gray, cinnamon)
data1.to_csv("new_list_for_colors.csv")
