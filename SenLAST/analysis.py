import os
import rasterio as rio
import rasterio.mask
import numpy as np
import shutil
from SenLAST.base_information import extract_files_to_list, import_polygons


def analyze_MODIS_temperature(mod_directory, shape_path):
    """
    returns the temperature value for each pixel of each station for each MODIS scene
    :return:
    returns one temperature array for each station
    """
    import_list = import_polygons(shape_path=shape_path)
    sentinel_file_list = extract_files_to_list(path_to_folder=mod_directory)
    final_mean = []
    print("#################### SENTINEL RESULTS ####################")

    for i, files in enumerate(import_list):
        scenes = i+1
        print(scenes, ". weather station")
        for j, polygons in enumerate(sentinel_file_list):
            stations = j+1
            print(stations, ". scene")
            src1 = rio.open(sentinel_file_list[j])
            mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
            Sen_temperature_array = mask[0][0]
            mean_Sen = np.nanmean(Sen_temperature_array)
            print(Sen_temperature_array)
            print(mean_Sen)
            final_mean.append(mean_Sen)
        print(np.nanmean(final_mean))


def analyze_SENTINEL_temperature(sen_directory, shape_path):
    """
    returns the temperature value for each pixel of each station for each SENTINEL scene
    prints an array for the scenes according to the stations
    :return:
    returns three arrays (1st array displayed for each station is the temperature array)
    returns one temperature array for each station if a[0][0]
    """
    import_list = import_polygons(shape_path=shape_path)
    sentinel_file_list = extract_files_to_list(path_to_folder=sen_directory)
    final_mean = []
    print("#################### SENTINEL RESULTS ####################")

    for i, files in enumerate(import_list):
        scenes = i+1
        print(scenes, ". weather station")
        for j, polygons in enumerate(sentinel_file_list):
            stations = j+1
            print(stations, ". scene")
            src1 = rio.open(sentinel_file_list[j])
            mask = rio.mask.mask(src1, [import_list[0][i]], all_touched=True, crop=True, nodata=np.nan)
            Sen_temperature_array = mask[0][0]
            mean_Sen = np.nanmean(Sen_temperature_array)
            print(Sen_temperature_array)
            print(mean_Sen)
            final_mean.append(mean_Sen)
        print(np.nanmean(final_mean))
