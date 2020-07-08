import os
import fiona
import rasterio as rio
import rasterio.mask
import numpy as np


def extract_files_to_list(path_to_folder, datatype):
    """
    finds all .tif-files in the corresponding directory
    :return:
    """
    new_list = []

    for filename in os.listdir(path_to_folder):
        if filename.endswith(datatype):
            new_list.append(os.path.join(path_to_folder, filename))
        else:
            continue
    return new_list


def import_polygons(shape_path):
    """
    imports the 3x3km polygons of the DWD weather stations
    :return:
    """
    shape_list = []
    active_shapefile = fiona.open(shape_path, "r")
    for i in range(0,len(list(active_shapefile))):
        shapes = [feature["geometry"] for feature in active_shapefile]
        shape_list.append(shapes)
    return shape_list


def extract_time_value_MODIS(mod_time_directory, shape_path):
    # create new cloud_free directory, overwrite if already exits
    selected_tifs = extract_files_to_list(path_to_folder=mod_time_directory, datatype=".tif")

    # import polygons from shapefile
    import_list = import_polygons(shape_path=shape_path)

    # loop through all .tif files in folder
    all_time_list = []
    for i, tifs in enumerate(selected_tifs):
        src1 = rio.open(selected_tifs[i])
        # loop through all weatherstations for each .tif file
        for j in range(0,1):
            out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][j]], all_touched=1, crop=True,
                                                       nodata=np.nan)
            temp = np.nanmean(out_image1[0])
            str_temp = str(temp)
            result = str_temp.find(".")
            sol_minute = int(int(str_temp[result+1:result+3]) * 60 / 100)
            sol_hour = str_temp[result-2:result]
            normal_hour = int(sol_hour)
            normal_minute = int(sol_minute) - 46
            if normal_minute < 0:
                normal_hour = normal_hour - 1
                normal_minute = 60 + normal_minute
                if normal_hour < 10:
                    normal_hour = "0" + str(normal_hour)
            if normal_minute < 10:
                normal_minute = "0" + str(normal_minute)
            final_normal_time = "___" + str(normal_hour) + "_" + str(normal_minute)
        all_time_list.append(final_normal_time)
    return all_time_list


def rename_files(mod_directory, mod_time_directory,  shape_path):
    new_mod_time_directory = mod_time_directory
    new_mod_directory = mod_directory
    time_list = extract_time_value_MODIS(mod_time_directory=new_mod_time_directory, shape_path=shape_path)
    selected_tifs = extract_files_to_list(path_to_folder=new_mod_directory, datatype=".tif")
    for i, tifs in enumerate(selected_tifs):
        #Marlin Index:
        name = tifs[0:95]
        # Jonas Index:
        #name = tifs[0:hier dein Index]
        print(name)
        os.rename(tifs, name + time_list[i] + ".tif")