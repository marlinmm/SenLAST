import os
import rasterio as rio
import rasterio.mask
import numpy as np
import shutil
from SenLAST.base_information import extract_files_to_list, import_polygons


def analyze_SENTINEL_temperature(sen_directory, sen_shape_path):
    """
    returns the temperature value for each pixel of each station for each SENTINEL scene
    prints an array for the scenes according to the stations
    :return:
    returns three arrays (1st array displayed for each station is the temperature array)
    returns one temperature array for each station if a[0][0]
    """
    import_list = import_polygons(shape_path=sen_shape_path)
    sentinel_file_list = extract_files_to_list(path_to_folder=sen_directory, datatype= ".tif")

    print(import_list)
    print(sentinel_file_list)

    print("#################### SENTINEL RESULTS ####################")

    Sen_station_mean = []

    for i, polygons in enumerate(import_list):
        scenes = i + 1

        ## Initialize empty analysis lists
        Sen_final_mean = []
        Sen_final_median = []
        Sen_final_stdev = []
        Sen_final_variance = []
        Sen_final_percentile = []
        Sen_final_range = []

        print(scenes, ". weather station")

        for j, tifs in enumerate(sentinel_file_list):
            if "DAY" in str(sentinel_file_list[j]):
            ### DAY/NIGHT STATEMENT ### if "day" in xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:
                stations = j + 1
                # print(stations, ". scene")
                src1 = rio.open(sentinel_file_list[j])
                mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
                Sen_temperature_array = mask[0][0]
                # print(Sen_temperature_array)

                ## Calculate mean ##
                mean_Sen = np.nanmean(Sen_temperature_array)
                # print("Mean =" + " " + str(mean_Sen))
                Sen_final_mean.append(mean_Sen)
                Station_mean = np.nanmean(Sen_final_mean)

                ## Calculate median ##
                median_Sen = np.nanmedian(Sen_temperature_array)
                # print("Median =" + " " + str(median_Sen))
                Sen_final_median.append(median_Sen)

                ## Calculate stdev ##
                stdev_Sen = np.nanstd(Sen_temperature_array)
                # print("Stdev =" + " " + str(stdev_Sen))
                Sen_final_stdev.append(stdev_Sen)

                ## Calculate variance ##
                var_Sen = np.nanvar(Sen_temperature_array)
                # print("Variance =" + " " + str(var_Sen))
                Sen_final_variance.append(var_Sen)

                ## Calculate percentile ##
                percentile_Sen = np.nanpercentile(Sen_temperature_array, 10)
                # print("Percentile =" + " " + str(percentile_Sen))
                Sen_final_percentile.append(percentile_Sen)

                ## Calculate range ##
                range_Sen = np.nanmax(Sen_temperature_array) - np.nanmin(Sen_temperature_array)
                # print("Range =" + " " + str(range_Sen))
                Sen_final_range.append(range_Sen)



            # print("Station " + str(i+1) + " mean for all scenes =" + " " + str(Station_mean))
                Sen_station_mean.append(Station_mean)
            else:
                pass
        return Sen_station_mean


def analyze_MODIS_temperature(mod_directory, mod_shape_path):
    """
    returns the temperature value for each pixel of each station for each MODIS scene
    :return:
    returns one temperature array for each station
    """
    import_list = import_polygons(shape_path=mod_shape_path)
    modis_file_list = extract_files_to_list(path_to_folder=mod_directory, datatype=".tif")

    Mod_station_mean = []

    print("#################### MODIS RESULTS ####################")

    for i, polygons in enumerate(import_list):
        scenes = i+1

        ## Initialize empty analysis lists
        Mod_final_mean = []
        Mod_final_median = []
        Mod_final_stdev = []
        Mod_final_variance = []
        Mod_final_percentile = []
        Mod_final_range = []

        print(scenes, ". weather station")

        for j, tifs in enumerate(modis_file_list):
            ### DAY/NIGHT STATEMENT ### if "day" in xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:
            stations = j+1
            # print(stations, ". scene")
            src1 = rio.open(modis_file_list[j])
            mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
            Mod_temperature_array = mask[0][0]
            # print(Mod_temperature_array)

            ## Mittelwert berechnen ##
            mean_Mod = np.nanmean(Mod_temperature_array)
            # print("Mean =" + " " + str(mean_Mod))
            Mod_final_mean.append(mean_Mod)
            Station_mean = np.nanmean(Mod_final_mean)

            ## Median berechnen ##
            median_Mod = np.nanmedian(Mod_temperature_array)
            # print("Median =" + " " + str(median_Mod))
            Mod_final_median.append(median_Mod)

            ## Calculate stdev ##
            stdev_Mod = np.nanstd(Mod_temperature_array)
            # print("Stdev =" + " " + str(stdev_Mod))
            Mod_final_stdev.append(stdev_Mod)

            ## Calculate variance ##
            var_Mod = np.nanvar(Mod_temperature_array)
            # print("Variance =" + " " + str(var_Mod))
            Mod_final_variance.append(var_Mod)

            ## Calculate percentile ##
            percentile_Mod = np.nanpercentile(Mod_temperature_array, 10)
            # print("Percentile =" + " " + str(percentile_Mod))
            Mod_final_percentile.append(percentile_Mod)

            ## Calculate range ##
            range_Mod = np.nanmax(Mod_temperature_array) - np.nanmin(Mod_temperature_array)
            # print("Range =" + " " + str(range_Mod))
            Mod_final_range.append(range_Mod)

        print("Station " + str(i+1) + " mean for all scenes =" + " " + str(Station_mean))
        Mod_station_mean.append(Station_mean)
    return Mod_station_mean


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
