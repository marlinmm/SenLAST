import pandas as pd
import plotly.express as px
from SenLAST.analysis import *

# Jonas Path
# csv_path = "C:/Users/jz199/Desktop/DWD_result_all/"
csv_path = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/"
# Marlin Path
# csv_path = "C:/Users/marli/Downloads/"

# Filename
csv_file = "Datenpaare.csv"

# Concatenation
csv_data = csv_path + csv_file

# Read csv data
df = pd.read_csv(csv_data, delimiter=";")

# Print head of csv data
print(df)

# Plot csv data
# fig = px.bar(df, y='Datenpaare', x='Monat', text='Datenpaare', title='S3/MODIS-Datenpaare (Zeitraum: 07/2018-05/2020)')
# fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
# fig.update_layout(
#     title='S3/MODIS data pairs (07/2018-05/2020)',
#     titlefont_size=30,
#     xaxis=dict(
#         title='Month',
#         titlefont_size=26,
#         tickfont_size=24,
#     ),
#     yaxis=dict(
#         title='Number of data pairs',
#         titlefont_size=26,
#         tickfont_size=24,
#     ),
#     legend=dict(
#         x=0,
#         y=1.0,
#         bgcolor='rgba(255, 255, 255, 0)',
#         bordercolor='rgba(255, 255, 255, 0)'
#     ),
#     barmode='group',
#     bargap=0.15, # gap between bars of adjacent location coordinates.
#     bargroupgap=0.1 # gap between bars of the same location coordinate.
# )
# fig.show()

###################################################################

def testplot(mod_directory, sen_directory, sen_shape_path, mod_shape_path):
    import plotly.graph_objects as go
    stations = ['Bad Berka', 'Dachwig', 'Erfurt-Weimar', 'Eschwege', 'Hof', 'Kleiner Inselberg', 'Kronach',
                'Bad Lobenstein', 'Martinroda', 'Meiningen', 'Neuhaus a.R.', 'Plauen', 'Schmücke', 'Schwarzburg',
                'Sontra', 'Waltershausen', 'Weimar-S.', 'Lichtentanne', 'Olbersleben', 'Krölpa-Rdorf']

    fig = go.Figure(data=[
        go.Bar(name='S3 Mean Temperature (°C)', x=stations, y=analyze_SENTINEL_temperature(sen_directory=sen_directory, sen_shape_path=sen_shape_path)),
        go.Bar(name='MODIS Mean Temperature (°C)', x=stations, y=analyze_MODIS_temperature(mod_directory=mod_directory, mod_shape_path=mod_shape_path))
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

def mean_diff(mod_directory, sen_directory, sen_shape_path, mod_shape_path):
    diff_list = []
    a = analyze_SENTINEL_temperature(sen_directory, sen_shape_path)
    b = analyze_MODIS_temperature(mod_directory, mod_shape_path)
    print(a)
    print(b)
    zip_object = zip(a, b)
    for list1_i, list2_i in zip_object:
        diff_list.append(list1_i - list2_i)
    print(diff_list)
