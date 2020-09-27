import os
import rasterio as rio
import rasterio.mask
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from SenLAST.base_information import extract_files_to_list, import_polygons

# List of station names
station_names = ['Bad Berka', 'Dachwig', 'Flughafen Erfurt', 'Kleiner Inselberg', 'Bad Lobenstein', 'Martinroda',
                 'Meiningen', 'Neuhaus a.R.', 'Schmücke', 'Schwarzburg', 'Waltershausen', 'Weimar-S.', 'Olbersleben',
                 'Krölpa-Rdorf', 'Eschwege', 'Hof', 'Kronach', 'Plauen', 'Sontra', 'Lichtentanne']


def calculate_statics_SENTINEL(sen_directory, sen_shape_path, day_night_string, stat_metric):
    """
    :param sen_directory:
    :param sen_shape_path:
    :param day_night_string:
    :param stat_metric: string
        Can be "mean", "median", "stdev", "values_mean" and "values_median"
    :return:
    """
    import_list = import_polygons(shape_path=sen_shape_path)
    sentinel_file_list = extract_files_to_list(path_to_folder=sen_directory, datatype=".tif")

    print("#################### SENTINEL RESULTS ####################")

    Sen_station_mean = []
    Sen_station_median = []
    Sen_station_stdev = []

    if day_night_string == "Day":
        day_night_string = "DAY"
    if day_night_string == "Night":
        day_night_string = "NIGHT"

    for i, polygons in enumerate(import_list):
        ## Initialize empty analysis lists
        Sen_final_mean = []
        Sen_final_median = []
        Sen_final_stdev = []
        Sen_final_variance = []
        Sen_final_percentile = []
        Sen_final_range = []
        file_counter = 0

        print("{}.{}".format(i + 1, station_names[i]))

        for j, tifs in enumerate(sentinel_file_list):
            if day_night_string in str(sentinel_file_list[j]) or day_night_string == "Day/Night":
                file_counter = file_counter + 1
                src1 = rio.open(sentinel_file_list[j])
                mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
                Sen_temperature_array = mask[0][0]
                if stat_metric == "mean":
                    ## Calculate mean ##
                    mean_Sen = np.nanmean(Sen_temperature_array)
                    # print("Mean =" + " " + str(mean_Sen))
                    Sen_final_mean.append(mean_Sen)

                if stat_metric == "median":
                    ## Calculate median ##
                    median_Sen = np.nanmedian(Sen_temperature_array)
                    # print("Median =" + " " + str(median_Sen))
                    Sen_final_median.append(median_Sen)

                if stat_metric == "stdev":
                    ## Calculate stdev ##
                    stdev_Sen = np.nanstd(Sen_temperature_array)
                    # print("Stdev =" + " " + str(stdev_Sen))
                    Sen_final_stdev.append(stdev_Sen)

                if stat_metric == "variance":
                    ## Calculate variance ##
                    var_Sen = np.nanvar(Sen_temperature_array)
                    # print("Variance =" + " " + str(var_Sen))
                    Sen_final_variance.append(var_Sen)

                if stat_metric == "percentile":
                    ## Calculate percentile ##
                    percentile_Sen = np.nanpercentile(Sen_temperature_array, 10)
                    # print("Percentile =" + " " + str(percentile_Sen))
                    Sen_final_percentile.append(percentile_Sen)

                if stat_metric == "range":
                    ## Calculate range ##
                    range_Sen = np.nanmax(Sen_temperature_array) - np.nanmin(Sen_temperature_array)
                    # print("Range =" + " " + str(range_Sen))
                    Sen_final_range.append(range_Sen)

        if stat_metric == "mean":
            Station_mean = np.nanmean(Sen_final_mean)
            print("Station " + str(i + 1) + " mean for all scenes =" + " " + str(Station_mean))
            Sen_station_mean.append(Station_mean)
        if stat_metric == "median":
            Station_median = np.nanmedian(Sen_final_median)
            print("Station " + str(i + 1) + " median for all scenes =" + " " + str(Station_median))
            Sen_station_median.append(Station_median)
        if stat_metric == "stdev":
            Station_stdev = np.nanmedian(Sen_final_stdev)
            print("Station " + str(i + 1) + " stdev for all scenes =" + " " + str(Station_stdev))
            Sen_station_stdev.append(Station_stdev)
    if stat_metric == "mean":
        return Sen_station_mean, file_counter
    if stat_metric == "median":
        return Sen_station_median, file_counter
    if stat_metric == "stdev":
        return Sen_station_stdev, file_counter


def calculate_statics_MODIS(mod_directory, mod_shape_path, day_night_string, stat_metric):
    """

    :param mod_directory:
    :param mod_shape_path:
    :param day_night_string:
    :param stat_metric: string
        Can be "mean", "median", "stdev", "values_mean" and "values_median"
    :return:
    """
    import_list = import_polygons(shape_path=mod_shape_path)
    modis_file_list = extract_files_to_list(path_to_folder=mod_directory, datatype=".tif")

    Mod_station_mean = []
    Mod_station_median = []
    Mod_station_stdev = []

    print("#################### MODIS RESULTS ####################")

    for i, polygons in enumerate(import_list):
        ## Initialize empty analysis lists
        Mod_final_mean = []
        Mod_final_median = []
        Mod_final_stdev = []
        Mod_final_variance = []
        Mod_final_percentile = []
        Mod_final_range = []

        print("{}.{}".format(i + 1, station_names[i]))

        for j, tifs in enumerate(modis_file_list):
            if day_night_string in str(modis_file_list[j]) or day_night_string == "Day/Night":
                src1 = rio.open(modis_file_list[j])
                mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
                Mod_temperature_array = mask[0][0]
                if stat_metric == "mean":
                    ## Calculate mean ##
                    mean_Mod = np.nanmean(Mod_temperature_array)
                    # print("Mean =" + " " + str(mean_Mod))
                    Mod_final_mean.append(mean_Mod)

                if stat_metric == "median":
                    ## Calculate median ##
                    median_Mod = np.nanmedian(Mod_temperature_array)
                    # print("Median =" + " " + str(median_Mod))
                    Mod_final_median.append(median_Mod)

                if stat_metric == "stdev":
                    ## Calculate stdev ##
                    stdev_Mod = np.nanstd(Mod_temperature_array)
                    # print("Stdev =" + " " + str(stdev_Mod))
                    Mod_final_stdev.append(stdev_Mod)

                if stat_metric == "variance":
                    ## Calculate variance ##
                    var_Mod = np.nanvar(Mod_temperature_array)
                    # print("Variance =" + " " + str(var_Mod))
                    Mod_final_variance.append(var_Mod)

                if stat_metric == "percentile":
                    ## Calculate percentile ##
                    percentile_Mod = np.nanpercentile(Mod_temperature_array, 10)
                    # print("Percentile =" + " " + str(percentile_Mod))
                    Mod_final_percentile.append(percentile_Mod)

                if stat_metric == "range":
                    ## Calculate range ##
                    range_Mod = np.nanmax(Mod_temperature_array) - np.nanmin(Mod_temperature_array)
                    # print("Range =" + " " + str(range_Mod))
                    Mod_final_range.append(range_Mod)

        if stat_metric == "mean":
            Station_mean = np.nanmean(Mod_final_mean)
            print("Station " + str(i + 1) + " mean for all scenes =" + " " + str(Station_mean))
            Mod_station_mean.append(Station_mean)
        if stat_metric == "median":
            Station_median = np.nanmedian(Mod_final_median)
            print("Station " + str(i + 1) + " median for all scenes =" + " " + str(Station_median))
            Mod_station_median.append(Station_median)
        if stat_metric == "stdev":
            Station_stdev = np.nanmedian(Mod_final_stdev)
            print("Station " + str(i + 1) + " stdev for all scenes =" + " " + str(Station_stdev))
            Mod_station_stdev.append(Station_stdev)
    if stat_metric == "mean":
        return Mod_station_mean
    if stat_metric == "median":
        return Mod_station_median
    if stat_metric == "stdev":
        return Mod_station_stdev


def extract_MODIS_temp_list(mod_directory, mod_shape_path, day_night_string):
    """

    :param day_night_string:
    :param mod_directory:
    :param mod_shape_path:
    :return:
    """
    import_list = import_polygons(shape_path=mod_shape_path)
    modis_file_list = extract_files_to_list(path_to_folder=mod_directory, datatype=".tif")

    Mod_station_time_series = []

    for i, polygons in enumerate(import_list):
        ## Initialize empty analysis lists
        Mod_final_mean = []

        for j, tifs in enumerate(modis_file_list):
            if day_night_string in str(modis_file_list[j]) or day_night_string == "Day/Night":
                src1 = rio.open(modis_file_list[j])
                mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
                Mod_temperature_array = mask[0][0]
                ## Calculate pixel mean ##
                mean_Mod = np.nanmean(Mod_temperature_array)
                Mod_final_mean.append(mean_Mod)
            # if day_night_string == "Day/Night":
            #     src1 = rio.open(modis_file_list[j])
            #     mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
            #     Mod_temperature_array = mask[0][0]
            #     ## Calculate pixel mean ##
            #     mean_Mod = np.nanmean(Mod_temperature_array)
            #     Mod_final_mean.append(mean_Mod)

        Mod_station_time_series.append(Mod_final_mean)
    return Mod_station_time_series


def extract_Sentinel_temp_list(sen_directory, sen_shape_path, day_night_string):
    """

    :param day_night_string:
    :param sen_directory:
    :param sen_shape_path:
    :return:
    """
    import_list = import_polygons(shape_path=sen_shape_path)
    sentinel_file_list = extract_files_to_list(path_to_folder=sen_directory, datatype=".tif")

    if day_night_string == "Day":
        day_night_string = "DAY"
    if day_night_string == "Night":
        day_night_string = "NIGHT"

    Sen_station_time_series = []

    for i, polygons in enumerate(import_list):
        ## Initialize empty analysis lists
        Sen_final_mean = []

        for j, tifs in enumerate(sentinel_file_list):
            if day_night_string in str(sentinel_file_list[j]) or day_night_string == "Day/Night":
                src1 = rio.open(sentinel_file_list[j])
                mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
                Sen_temperature_array = mask[0][0]
                ## Calculate pixel mean ##
                mean_Sen = np.nanmean(Sen_temperature_array)
                Sen_final_mean.append(mean_Sen)

            # if day_night_string == "Day/Night":
            #     src1 = rio.open(sentinel_file_list[j])
            #     mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
            #     Sen_temperature_array = mask[0][0]
            #     ## Calculate pixel mean ##
            #     mean_Sen = np.nanmean(Sen_temperature_array)
            #     Sen_final_mean.append(mean_Sen)

        Sen_station_time_series.append(Sen_final_mean)
    return Sen_station_time_series


def analyze_Sentinel_DWD(sen_DWD_dir, sen_directory, sen_shape_path, DWD_temp_parameter, day_night_string):
    """

    :param day_night_string:
    :param sen_DWD_dir:
    :param sen_directory:
    :param sen_shape_path:
    :param DWD_temp_parameter:
    :return:
    """
    csv_list = extract_files_to_list(path_to_folder=sen_DWD_dir, datatype=".csv")
    Sen_data_list = extract_Sentinel_temp_list(sen_directory=sen_directory, sen_shape_path=sen_shape_path,
                                               day_night_string=day_night_string)
    DWD_list = []
    Sen_data_mean_list = []
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

        Sen_data_mean_list.append(np.mean(Sen_data_list[i]))
        DWD_list.append(np.mean(temp_2m))
    return DWD_list, Sen_data_mean_list


def analyze_MODIS_DWD(mod_DWD_dir, mod_directory, mod_shape_path, DWD_temp_parameter, day_night_string):
    """

    :param mod_DWD_dir:
    :param day_night_string:
    :param mod_directory:
    :param mod_shape_path:
    :param DWD_temp_parameter:
    :return:
    """
    csv_list = extract_files_to_list(path_to_folder=mod_DWD_dir, datatype=".csv")

    Mod_data_list = extract_MODIS_temp_list(mod_directory=mod_directory, mod_shape_path=mod_shape_path,
                                            day_night_string=day_night_string)
    DWD_list = []
    Mod_data_mean_list = []
    print("######################## MODIS ########################")
    for i, file in enumerate(csv_list):
        # Read csv data
        df = pd.read_csv(file, delimiter=",")
        temp_2m = df[DWD_temp_parameter]
        tmp = temp_2m[temp_2m == -999]
        if len(tmp) > 0:
            for j, value in enumerate(tmp):
                temp_2m = temp_2m.drop([tmp.index[j]])
                Mod_data_list[i].pop(tmp.index[j])

        Mod_data_mean_list.append(np.mean(Mod_data_list[i]))
        DWD_list.append(np.mean(temp_2m))
    return DWD_list, Mod_data_mean_list
