import pandas as pd

# Create a DataFrame that shows apples and bananas sales for 2017 and 2018
df = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Write the data to fruit.csv in project directory
df.to_csv("./fruit.csv")

# TODO: Write into correct folder!