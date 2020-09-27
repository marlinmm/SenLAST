import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from functools import reduce
from SenLAST.analysis import *
from SenLAST.comparison import *


def datapairs():
    # Jonas Path
    # csv_path = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/"
    # Marlin Path
    csv_path = "C:/Users/marli/Downloads/"

    # Filename
    csv_file = "Datenpaare.csv"
    # Concatenation
    csv_data = csv_path + csv_file

    # Read csv data
    df = pd.read_csv(csv_data, delimiter=";")
    # Print head of csv data
    print(df)

    # Plot csv data
    fig = px.bar(df, y='Datenpaare', x='Monat', text='Datenpaare',
                 title='S3/MODIS-Datenpaare (Zeitraum: 07/2018-05/2020)')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
    fig.update_layout(
        title='S3/MODIS Datenpaare (07/2018 - 05/2020)',
        titlefont_size=30,
        xaxis=dict(
            title='Monat',
            titlefont_size=26,
            tickfont_size=24,
        ),
        yaxis=dict(
            title='Anzahl der Datenpaare',
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
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


# datapairs()


def count_all_occurences(satellite_directory):
    month_list = ["2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12", "2019-01", "2019-02", "2019-03",
                  "2019-04", "2019-05", "2019-06", "2019-07", "2019-08", "2019-09", "2019-10", "2019-11", "2019-12",
                  "2020-01", "2020-02", "2020-03", "2020-04", "2020-05"]
    sen_dates = extract_MODIS_date(satellite_directory)
    sat_dates2 = [elem[:7] for elem in sen_dates]
    occurence_list = []
    for element in month_list:
        print(element)
        occurences = sat_dates2.count(element)
        occurence_list.append(occurences)
    print(occurence_list)

    fig = go.Figure(data=[
        go.Bar(name='Anzahl der monatlichen MODIS Aufnahmen', x=month_list, y=occurence_list, text=occurence_list,
               textposition="outside"),
    ])
    # Change the bar mode
    fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
    fig.update_layout(
        title='Anzahl der monatlichen MODIS Aufnahmen',
        titlefont_size=28,
        xaxis=dict(
            title='Datum',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Anzahl der Aufnahmen',
            titlefont_size=20,
            tickfont_size=14,
        ),
        barmode='group',
        bargap=0.25,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


########################################################################################################################

def SenMod_DayNight(mod_directory, sen_directory, sen_shape_path, mod_shape_path, stat_metric, day_night_string):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen', 'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben',
                'Krölpa-Rdorf', 'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']
    y, counter = calculate_statics_SENTINEL(sen_directory=sen_directory, sen_shape_path=sen_shape_path,
                                            day_night_string=day_night_string, stat_metric=stat_metric)
    fig = go.Figure(data=[
        go.Bar(name="Sen-3 SLSTR " + stat_metric + " " + day_night_string + "time temperature (°C)", x=stations,
               y=y),
        go.Bar(name="Terra MODIS " + stat_metric + " " + day_night_string + "time temperature (°C)", x=stations,
               y=calculate_statics_MODIS(mod_directory=mod_directory, mod_shape_path=mod_shape_path,
                                         day_night_string=day_night_string, stat_metric=stat_metric))])
    # Change the bar mode
    fig.update_layout(
        title= stat_metric.capitalize() + " " + day_night_string + "time Temperature (n = " + str(counter) + " scenes)",
        titlefont_size=36,
        xaxis=dict(
            title='Stations',
            titlefont_size=32,
            tickfont_size=26,
        ),
        yaxis=dict(
            title=stat_metric.capitalize() + " " + day_night_string + "time Temperature",
            titlefont_size=32,
            tickfont_size=28,
        ),
        legend=dict(
            x=0.82,
            y=1.05,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            font=dict(
                size=16,
                color="black"
            ),
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


########################################################################################################################


def mean_diff(mod_directory, sen_directory, senmod_dir, mod_sen_dir,  sen_shape_path, mod_shape_path, day_night_string,
              stat_metric, DWD_temp_parameter, sen_DWD_dir, mod_DWD_dir, calculation):
    diff_list = []

    if calculation == "SenMod":
        SenMod_mean_list, counter = calculate_statics_SENTINEL(senmod_dir, sen_shape_path, day_night_string, stat_metric)
        ModSen_mean_list = calculate_statics_MODIS(mod_sen_dir, mod_shape_path, day_night_string, stat_metric)
    if calculation == "SemDWD":
        SenDWD_mean_list = calculate_statics_SENTINEL(sen_directory, sen_shape_path, day_night_string, stat_metric)
        DWD_Sen_list, Sen_mean_list = analyze_MODIS_DWD(sen_DWD_dir, mod_directory, mod_shape_path, DWD_temp_parameter,
                                                        day_night_string)
    if calculation == "ModDWD":
        ModDWD_mean_list = calculate_statics_MODIS(mod_directory, mod_shape_path, day_night_string,
                                                   stat_metric)
        DWD_Mod_list, Mod_mean_list = analyze_MODIS_DWD(mod_DWD_dir, mod_directory, mod_shape_path, DWD_temp_parameter,
                                                        day_night_string)

    print(len(DWD_Mod_list))
    # # b = DWD_5cm
    # # print("Sentinel = ")
    # # print(a)
    # # print("MODIS = ")
    # # print(b)
    # ### Multiple Means for every station and every scence --> order of scenes is fundamental !!! ###
    # # SENTINEL_1d = reduce(lambda x, y: x + y, a)
    # # MODIS_1d = reduce(lambda x, y: x + y, b)
    # # print(SENTINEL_1d)
    # # print(MODIS_1d)
    # zip_object = zip(a, b)
    # # zip_object = zip(SENTINEL_1d, MODIS_1d)
    # for list1_i, list2_i in zip_object:
    #     # diff_list.append(abs(list1_i - list2_i))
    #     diff_list.append(list1_i - list2_i)
    # print("Difference S3-MODIS = ")
    # print(diff_list)
    # print("mean difference = ")
    # print(np.mean(diff_list))
    # print("median difference = ")
    # print(np.median(diff_list))
    # print(np.std(diff_list))
    #
    # return diff_list


def barchart_mean_diff(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS,
                       stat_metric):  # , path_to_csv):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen', 'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben',
                'Krölpa-Rdorf', 'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']

    fig = go.Figure(data=[
        go.Bar(name='', x=stations,
               y=mean_diff(sen_directory=sen_directory, mod_directory=mod_directory,
                           sen_shape_path=sen_shape_path, mod_shape_path=mod_shape_path, daytime_S3=daytime_S3,
                           daytime_MODIS=daytime_MODIS, stat_metric=stat_metric)),
        # , path_to_csv=path_to_csv)),
    ])
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=20, uniformtext_mode='hide')
    fig.update_layout(
        title='Mittlere Temperaturdifferenz von MODIS zu DWD-Daten (2m) (MODIS-DWD)',
        titlefont_size=30,
        xaxis=dict(
            title='Stationen',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mittlere Temperaturdifferenz von MODIS zu DWD-Daten (2m) (°C)',
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

def SenMod_scatter(mod_directory, sen_directory, sen_shape_path, mod_shape_path, day_night_string):
    SENTINEL = extract_Sentinel_temp_list(sen_directory, sen_shape_path, day_night_string)
    MODIS = extract_MODIS_temp_list(mod_directory, mod_shape_path, day_night_string)
    ### Multiple Means for every station and every scence --> order of scenes is fundamental !!! ###
    SENTINEL_1d = reduce(lambda x, y: x + y, SENTINEL)
    MODIS_1d = reduce(lambda x, y: x + y, MODIS)

    # Regression
    reg = LinearRegression().fit(np.vstack(MODIS_1d), SENTINEL_1d)
    reg_fit = reg.predict(np.vstack(MODIS_1d))

    fig = go.Figure()
    fig.add_trace(go.Scatter(name='line of best fit', x=MODIS_1d, y=reg_fit, mode='lines'))
    fig.add_trace(go.Scatter(name='X vs Y', x=MODIS_1d, y=SENTINEL_1d, mode='markers'))
    fig.update_traces(marker=dict(size=10),
                      selector=dict(mode='markers'))
    fig.update_layout(
        title="Correlation of the Mean " + day_night_string + "time Temperature (MODIS/S3)",
        titlefont_size=32,
        xaxis=dict(
            title="Mean MODIS " + day_night_string + "time Temperature (°C)",
            titlefont_size=32,
            tickfont_size=26,
        ),
        yaxis=dict(
            title="Mean Sentinel " + day_night_string + "time Temperature (°C)",
            titlefont_size=32,
            tickfont_size=26,
        ))
    fig.show()


########################################################################################################################

def allstations_alldata(mod_directory, sen_directory, sen_shape_path, mod_shape_path, stat_metric, day_night_string):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']

    # 2020-01-16
    # TT_10 = [1.1, 1.7, 6.7, 3.5, -0.6, 6.5, 3.1, 2.2, 3.5, 1.4, 8.1, 6.7, 4.0, 5.2, 2.2, 3.6, -0.7, 4.2, 0.7, 4.7]
    # TM5_10 = [-1.1, -1.3, 4.7, 1.4, -2.6, 4.1, 0.9, -0.2, 2.2, -0.8, 6.0, 3.5, 1.9, 1.7, -0.5, 1.6, -2.9, 2.4, -2.5, 0.4]

    # 2020-03-27
    # TT_10 = [9.0, 10.3, 8.1, 4.6, 12.8, 7.1, 10.9, 6.3, 4.3, 8.3, 6.3, 9.7, 11.2, 9.1, 10.2, 12.0, 13.3, 14.3, 9.3, 13.2]
    # TM5_10 = [12.8, 15.7, 11.5, 10.4, 16.9, 11.9, 16.2, 8.5, 7.1, 12.8, 11.7, 13.0, 13.3, 15.1, 14.3, 15.7, 17.7, 17.1, 13.0, 16.1]

    # 2019-07-17
    TT_10 = [12.3, 14.6, 15.2, 11.4, 12.6, 12.9, 14.6, 12.2, 11.6, 14.1, 12.9, 13.3, 13.4, 15.0, 14.0, 14.4, 17.1, 14.1,
             11.5, 12.5]
    TM5_10 = [10.7, 11.7, 12.9, 9.0, 11.8, 11.8, 12.5, 10.1, 10.1, 12.1, 11.5, 10.7, 11.1, 13.6, 12.3, 12.0, 15.3, 12.7,
              8.3, 10.2]

    y, counter = calculate_statics_SENTINEL(sen_directory=sen_directory, sen_shape_path=sen_shape_path,
                               stat_metric=stat_metric, day_night_string=day_night_string)

    fig = go.Figure(data=[
        go.Bar(name='Mittlere S3 Temperatur (°C)', x=stations,
               y=y),
        go.Bar(name='Mittlere MODIS Temperatur (°C)', x=stations,
               y=calculate_statics_MODIS(mod_directory=mod_directory, mod_shape_path=mod_shape_path,
                                        stat_metric=stat_metric, day_night_string=day_night_string)),
        go.Bar(name='DWD 2m Absolute Temperatur (°C)', x=stations,
               y=TT_10),
        go.Bar(name='DWD 5cm Absolute Temperatur (°C)', x=stations,
               y=TM5_10)
    ])
    # Change the bar mode
    fig.update_layout(
        title='Temperatur (17.07.19, 21 Uhr) für jede Station',
        titlefont_size=28,
        xaxis=dict(
            title='Stationen',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Temperatur (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        legend=dict(
            x=0.87,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.35,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


def plot_MODIS_DWD(path_to_csv, mod_directory, mod_shape_path, DWD_temp_parameter):
    csv_list = extract_files_to_list(path_to_folder=path_to_csv, datatype=".csv")
    MOD_data_list = extract_MODIS_temp_list(mod_directory=mod_directory, mod_shape_path=mod_shape_path)

    print("######################## MODIS ########################")
    for i, file in enumerate(csv_list):
        # Read csv data
        df = pd.read_csv(file, delimiter=",")
        temp_2m = df[DWD_temp_parameter]

        tmp = temp_2m[temp_2m == -999]
        if len(tmp) > 0:
            for j, value in enumerate(tmp):
                temp_2m = temp_2m.drop([tmp.index[j]])
                MOD_data_list[i].pop(tmp.index[j])
        if DWD_temp_parameter == "TM5_10":
            DWD_variable = "DWD Temperatur 5cm (°C)"
        if DWD_temp_parameter == "TT_10":
            DWD_variable = "DWD Temperatur 2m (°C)"

        # Fit linear model
        # Mod_DWD_correlation_list = np.array(temp_2m).reshape(-1, 1)
        # model = LinearRegression()
        # model.fit(temp_2m, Mod_DWD_correlation_list)
        # model = LinearRegression().fit(temp_2m, Mod_DWD_correlation_list)
        # r_sq = model.score(temp_2m, Mod_DWD_correlation_list)
        #
        # print("")
        # print(station_names[i])
        # print('R2:', r_sq)
        # intercept = model.intercept_
        # print('Y-intercept:', model.intercept_)
        # coefficient = model.coef_
        # print('Coefficient:', model.coef_)

        reg = LinearRegression().fit(np.vstack(MOD_data_list[i]), temp_2m)
        reg_fit = reg.predict(np.vstack(MOD_data_list[i]))

        # Plot scatterplot for each station
        fig, ax = plt.subplots()
        ax.set_title('MODIS/DWD Temperatur Korrelation (' + station_names[i] + ")")
        ax.set_ylabel('MODIS Temperatur (°C)')
        ax.set_xlabel(DWD_variable)
        # abline_values = [coefficient * i + intercept for i in Mod_DWD_correlation_list]
        # plt.plot(reg_fit, temp_2m, ("#FFA500"))
        plt.plot(temp_2m, MOD_data_list[i], 'o')
        plt.show()


def plot_Sentinel_DWD(path_to_csv, sen_directory, sen_shape_path, DWD_temp_parameter):
    csv_list = extract_files_to_list(path_to_folder=path_to_csv, datatype=".csv")
    Sen_data_list = extract_Sentinel_temp_list(sen_directory=sen_directory, sen_shape_path=sen_shape_path)
    DWD_mean_list = []
    Sen_data_mean_list = []
    boxplot_result_list = []
    print("######################## SENTINEL ########################")
    for i, file in enumerate(csv_list):
        # Read csv data
        df = pd.read_csv(file, delimiter=",")
        temp_2m = df[DWD_temp_parameter]

        tmp = temp_2m[temp_2m == -999]
        if len(tmp) > 0:
            for j, value in enumerate(tmp):
                temp_2m = temp_2m.drop([tmp.index[j]])
                Sen_data_list[i].pop(tmp.index[j])
        if DWD_temp_parameter == "TM5_10":
            DWD_variable = "DWD temperatur 5cm (°C)"
        if DWD_temp_parameter == "TT_10":
            DWD_variable = "DWD temperatur 2m (°C)"

        # # for bar chart only
        Sen_data_mean_list.append(np.mean(Sen_data_list[i]))
        boxplot_result_list.append(Sen_data_list[i])
        DWD_mean_list.append(np.mean(temp_2m))

        # Fit linear model
        Sen_DWD_correlation_list = np.array(Sen_data_list[i]).reshape(-1, 1)
        model = LinearRegression()
        model.fit(Sen_DWD_correlation_list, temp_2m)
        model = LinearRegression().fit(Sen_DWD_correlation_list, temp_2m)
        r_sq = model.score(Sen_DWD_correlation_list, temp_2m)

        print("")
        print(station_names[i])
        print('R2:', r_sq)
        intercept = model.intercept_
        print('Y-intercept:', model.intercept_)
        coefficient = model.coef_
        print('Coefficient:', model.coef_)

        # Plot scatterplot for each station
        fig, ax = plt.subplots()
        ax.set_title('Sentinel-3/DWD Temperatur Korrelation (' + station_names[i] + ")")
        ax.set_xlabel('Sentinel-3 Temperatur (°C)')
        ax.set_ylabel(DWD_variable)
        abline_values = [coefficient * i + intercept for i in Sen_DWD_correlation_list]
        plt.plot(Sen_DWD_correlation_list, abline_values, ("#FFA500"))
        plt.plot(Sen_data_list[i], temp_2m, 'o')
        plt.show()

    #### for creating a boxplot #####
    # # Create a figure instance
    # fig = plt.figure(1, figsize=(9, 6))
    #
    # # Create an axes instance
    # ax = fig.add_subplot(111)
    #
    # # Create the boxplot
    # bp = ax.boxplot(boxplot_result_list)
    # ax.set_xticklabels(station_names, rotation='vertical')
    # plt.xlabel("Stationen")
    # plt.ylabel("Mittlere Temp. in °C")
    #
    # fig.savefig('fig1.png', bbox_inches='tight')


def SenDWD_barchart(sen_directory, sen_shape_path, path_to_csv, DWD_temp_parameter):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']
    DWD_2m, Sen = analyze_Sentinel_DWD(path_to_csv, sen_directory, sen_shape_path, DWD_temp_parameter="TT_10")
    DWD_5cm, Sen = analyze_Sentinel_DWD(path_to_csv, sen_directory, sen_shape_path, DWD_temp_parameter="TM5_10")
    print(Sen)
    print(DWD_2m)
    fig = go.Figure(data=[
        go.Bar(name='Mittlere S3 Temperature (°C)', x=stations, y=Sen),
        go.Bar(name='Mittlere DWD Stations-Temperatur 2m (°C)', x=stations, y=DWD_2m),
        go.Bar(name='Mittlere DWD Stations-Temperatur 5cm (°C)', x=stations, y=DWD_5cm)
    ])
    # Change the bar mode
    fig.update_layout(
        title='Mittlere S3/DWD Temperatur (n = 130 Szenen)',
        titlefont_size=32,
        xaxis=dict(
            title='Stationen',
            titlefont_size=32,
            tickfont_size=26,
        ),
        yaxis=dict(
            title='Mittlere Temperatur (°C)',
            titlefont_size=32,
            tickfont_size=26,
        ),
        legend=dict(
            x=0.82,
            y=1.12,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            font=dict(
                size=16,
                color="black"
            ),
        ),
        barmode='group',
        bargap=0.3,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


def ModDWD_barchart(mod_directory, mod_shape_path, path_to_csv):
    stations = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                'Meiningen',
                'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben', 'Krölpa-Rdorf',
                'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']
    DWD_2m, MOD = analyze_MODIS_DWD(path_to_csv, mod_directory, mod_shape_path, DWD_temp_parameter="TT_10")
    DWD_5cm, MOD = analyze_MODIS_DWD(path_to_csv, mod_directory, mod_shape_path, DWD_temp_parameter="TM5_10")
    print(MOD)
    print(DWD_2m)
    fig = go.Figure(data=[
        go.Bar(name='Mittlere MODIS Temperature (°C)', x=stations, y=MOD),
        go.Bar(name='Mittlere DWD Stations-Temperatur 2m (°C)', x=stations, y=DWD_2m),
        go.Bar(name='Mittlere DWD Stations-Temperatur 5cm (°C)', x=stations, y=DWD_5cm)
    ])
    # Change the bar mode
    fig.update_layout(
        title='Mittlere MODIS/DWD Temperatur (n = 262 Szenen)',
        titlefont_size=28,
        xaxis=dict(
            title='Stationen',
            titlefont_size=20,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Mittlere Temperatur (°C)',
            titlefont_size=20,
            tickfont_size=14,
        ),
        legend=dict(
            x=0.86,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.3,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    fig.show()


def SenMod_histogram(mod_directory, sen_directory, sen_shape_path, mod_shape_path, daytime_S3, daytime_MODIS):
    import seaborn as sns
    import pandas as pd
    SENTINEL = extract_Sentinel_temp_list(sen_directory, sen_shape_path, daytime_S3)
    MODIS = extract_MODIS_temp_list(mod_directory, mod_shape_path, daytime_MODIS)
    SENTINEL_1d = reduce(lambda x, y: x + y, SENTINEL)
    MODIS_1d = reduce(lambda x, y: x + y, MODIS)
    print(SENTINEL_1d)
    print(len(SENTINEL_1d))
    print(MODIS_1d)
    print(len(MODIS_1d))
    difference = []
    zip_object = zip(SENTINEL_1d, MODIS_1d)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i - list2_i)
    print(difference)
    df = pd.DataFrame(difference, columns=["SLSTR minus MODIS Difference"])
    print(df)
    # sns.displot(data=df, x=df["SLSTR minus MODIS Difference"], kde=True)

    g = sns.displot(
        data=df, x="SLSTR minus MODIS Difference", kde=True)
    g.set_axis_labels(daytime_MODIS + "time SLSTR minus MODIS Difference", "Number")
    g.set_titles("{Histogram of " + daytime_MODIS + "time Difference")
    plt.show()
