import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from functools import reduce
from SenLAST.analysis import *


def datapairs():
    # Jonas Path
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
    fig = px.bar(df, y='Datenpaare', x='Monat', text='Datenpaare', title='S3/MODIS-Datenpaare (Zeitraum: 07/2018-05/2020)')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
    fig.update_layout(
        title='S3/MODIS data pairs (07/2018-05/2020)',
        titlefont_size=30,
        xaxis=dict(
            title='Month',
            titlefont_size=26,
            tickfont_size=24,
        ),
        yaxis=dict(
            title='Number of data pairs',
            titlefont_size=26,
            tickfont_size=24,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    fig.show()

########################################################################################################################

def SenMod_DayNight(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda', 'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']

    fig = go.Figure(data=[
        go.Bar(name='S3 Mean Night Temperature (°C)', x=stations, y=analyze_SENTINEL_temperature(sen_directory=sen_directory,
                                                                                           sen_shape_path=sen_shape_path,
                                                                                           daytime_S3=daytime_S3)),
        go.Bar(name='MODIS Mean Night Temperature (°C)', x=stations, y=analyze_MODIS_temperature(mod_directory=mod_directory,
                                                                                           mod_shape_path=mod_shape_path,
                                                                                           daytime_MODIS=daytime_MODIS))
    ])
    # Change the bar mode
    fig.update_layout(
        title='Mean night temperature (n_S3 = 64 scenes; n_MODIS = 57 scenes)',
        titlefont_size=28,
        xaxis=dict(
            title='Stations',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mean night temperature (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        legend=dict(
            x=1.0,
            y=1.1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()

########################################################################################################################

def mean_diff(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    diff_list = []
    a = analyze_SENTINEL_temperature(sen_directory, sen_shape_path, daytime_S3)
    b = analyze_MODIS_temperature(mod_directory, mod_shape_path, daytime_MODIS)
    print("Sentinel = ")
    print(a)
    print("MODIS = ")
    print(b)
    ### Multiple Means for every station and every scence --> order of scenes is fundamental !!! ###
    SENTINEL_1d = reduce(lambda x, y: x + y, a)
    MODIS_1d = reduce(lambda x, y: x + y, b)
    print(SENTINEL_1d)
    print(MODIS_1d)
    # zip_object = zip(a, b)
    zip_object = zip(SENTINEL_1d, MODIS_1d)
    for list1_i, list2_i in zip_object:
        diff_list.append(abs(list1_i - list2_i))
    print("Difference S3-MODIS = ")
    print(diff_list)
    print("mean difference = ")
    print(np.mean(diff_list))
    # print("median difference = ")
    # print(np.median(diff_list))

    return diff_list


def barchart_mean_diff(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']


    fig = go.Figure(data=[
        go.Bar(name='', x=stations,
               y=mean_diff(sen_directory=sen_directory, mod_directory=mod_directory,
                                              sen_shape_path=sen_shape_path, mod_shape_path=mod_shape_path,
                                              daytime_S3=daytime_S3, daytime_MODIS=daytime_MODIS)),
    ])
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
    fig.update_layout(
        title='Mean night temperature difference (°C) for every investigated station (S3-MODIS)',
        titlefont_size=30,
        xaxis=dict(
            title='Stations',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mean night temperature difference (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


########################################################################################################################

def SenMod_scatter(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    SENTINEL = analyze_SENTINEL_temperature(sen_directory, sen_shape_path, daytime_S3)
    MODIS = analyze_MODIS_temperature(mod_directory, mod_shape_path, daytime_MODIS)
    print(SENTINEL)
    print(MODIS)
    ### Multiple Means for every station and every scence --> order of scenes is fundamental !!! ###
    SENTINEL_1d = reduce(lambda x,y : x+y, SENTINEL)
    MODIS_1d = reduce(lambda x,y : x+y, MODIS)
    print(SENTINEL_1d)
    print(MODIS_1d)

    fig = go.Figure(data=go.Scatter(
        x=MODIS,
        y=SENTINEL,
        mode='markers',
        marker=dict(
            color='rgba(187, 67, 141, 1)',
            size=10,
            line_width=1
        ),
    ))
    fig.update_layout(
        title='MODIS/S3-Mean day temperature correlation',
        titlefont_size=28,
        xaxis=dict(
            title='Mean MODIS day temperature (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mean SENTINEL day temperature (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ))

    fig.show()

########################################################################################################################

def allstations_alldata(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda', 'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']

    # 2018-09-30
    ground_temp = [14.8]
    air_temp = [16.7]

    fig = go.Figure(data=[
        go.Bar(name='S3 Mean Night Temperature (°C)', x=stations, y=analyze_SENTINEL_temperature(sen_directory=sen_directory,
                                                                                           sen_shape_path=sen_shape_path,
                                                                                           daytime_S3=daytime_S3)),
        go.Bar(name='MODIS Mean Night Temperature (°C)', x=stations, y=analyze_MODIS_temperature(mod_directory=mod_directory,
                                                                                           mod_shape_path=mod_shape_path,
                                                                                           daytime_MODIS=daytime_MODIS))
    ])
    # Change the bar mode
    fig.update_layout(
        title='Mean night temperature (n_S3 = 64 scenes; n_MODIS = 57 scenes)',
        titlefont_size=28,
        xaxis=dict(
            title='Stations',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mean night temperature (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        legend=dict(
            x=1.0,
            y=1.1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()