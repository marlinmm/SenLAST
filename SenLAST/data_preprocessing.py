import os
import rasterio as rio
import rasterio.mask
import numpy as np
import shutil
from SenLAST.base_information import extract_files_to_list, import_polygons

def eliminate_MODIS_cloudy_data(mod_directory, shape_path):
    """
    eliminates the scenes which are not cloud_free
    :return:
    """
    # create new cloud_free directory, overwrite if already exits
    cloud_free = mod_directory + "/cloud_free"
    if os.path.exists(cloud_free):
        shutil.rmtree(cloud_free)
    os.mkdir(mod_directory + "/cloud_free")
    selected_tifs = extract_files_to_list(path_to_folder=mod_directory)

    # import polygons from shapefile
    import_list = import_polygons(shape_path=shape_path)

    # loop through all .tif files in folder
    for i, tifs in enumerate(selected_tifs):
        src1 = rio.open(selected_tifs[i])
        bool_list = []
        flag = 0   #set boolean flag to 0

        # loop through all weatherstations for each .tif file
        for j, polygons in enumerate(import_list):
            out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][j]], all_touched=1, crop=True,
                                                       nodata=np.nan)

            # extract nanmean temperature at all stations for each .tif file to eliminate error values
            mean_temp = np.nanmean(out_image1[0])

            # create boolean values for error values and store in list (-40° is lowest remotely realistic temperature)
            if mean_temp < -40 or np.isnan(mean_temp) == True:
                bool_list.append(False)
            else:
                bool_list.append(True)

        # check the list for flags of error values and only save tif files without any error values at station locations
        for boolean in bool_list:
            if boolean == False:
                flag = 1
                break
        if flag == 0:
            shutil.copy(selected_tifs[i], cloud_free)



def eliminate_nanoverlap(sen_directory, shape_path):
    """
    eliminates the scenes which would'nt match with all weather stations
    :return:
    """
    import_list = import_polygons(shape_path=shape_path)
    file_list = extract_files_to_list(path_to_folder=sen_directory)
    tifs_selected = sen_directory + "/selected"
    if os.path.exists(tifs_selected):
        shutil.rmtree(tifs_selected)
    os.mkdir(sen_directory + "/selected")

    for i, files in enumerate(file_list):
        src1 = rio.open(file_list[i])
        try:
            for j, polygons in enumerate(import_list):
                rio.mask.mask(src1, [import_list[0][j]], all_touched=0, crop=True, nodata=np.nan)
            shutil.copy(file_list[i], tifs_selected)
        except ValueError:
            pass


def eliminate_SENTINEL_cloudy_data(sen_directory, shape_path):
    """
    eliminates the scenes which are not cloud_free
    :return:
    """
    # use this function to delete data which is not overlapping with ROI
    eliminate_nanoverlap(sen_directory=sen_directory, shape_path=shape_path)

    # create new cloud_free directory, overwrite if already exits
    cloud_free = sen_directory + "/selected/cloud_free"
    if os.path.exists(cloud_free):
        shutil.rmtree(cloud_free)
    os.mkdir(sen_directory + "/selected/cloud_free")
    selected_tifs = extract_files_to_list(path_to_folder=sen_directory + "/selected")

    # import polygons from shapefile
    import_list = import_polygons(shape_path=shape_path)

    # loop through all .tif files in folder
    for i, tifs in enumerate(selected_tifs):
        src1 = rio.open(selected_tifs[i])
        bool_list = []
        flag = 0   #set boolean flag to 0

        # loop through all weatherstations for each .tif file
        for j, polygons in enumerate(import_list):
            out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][j]], all_touched=1, crop=True,
                                                       nodata=np.nan)

            # extract minimal temperature at all stations for each .tif file to eliminate error values
            min_temp = np.min(out_image1[0])

            # create boolean values for error values and store in list (-40° is lowest remotely realistic temperature)
            if min_temp < -40:
                bool_list.append(False)
            else:
                bool_list.append(True)

        # check the list for flags of error values and only save tif files without any error values at station locations
        for boolean in bool_list:
            if boolean == False:
                flag = 1
                break
        if flag == 0:
            shutil.copy(selected_tifs[i], cloud_free)
