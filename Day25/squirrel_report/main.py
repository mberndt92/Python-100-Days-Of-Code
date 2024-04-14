
# Squirrel Count

import pandas

data = pandas.read_csv("./squirrel_data.csv")

fur_colors = data["Primary Fur Color"].value_counts()
fur_colors.rename_axis("Fur Color", inplace=True)
fur_colors.to_csv("fur_colors.csv")
print(fur_colors)
