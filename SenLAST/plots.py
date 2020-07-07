import pandas as pd
import plotly.express as px

# Jonas Path
csv_path = "C:/Users/jz199/Desktop/DWD_result_all/"
# Marlin Path
# csv_path = ""

# Filename
csv_file = "combined__2750_Kronach.csv"

# Concatenation
csv_data = csv_path + csv_file

# Read csv data
df = pd.read_csv(csv_data, delimiter=";")

# Print head of csv data
print(df.head())

# Plot csv data
fig = px.scatter(df, x = 'TT_10', y = 'TM5_10', title='DWD Data')
fig.show()