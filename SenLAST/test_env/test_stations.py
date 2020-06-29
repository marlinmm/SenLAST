from datetime import datetime
import os
import rasterio as rio
import rasterio.mask
import numpy as np
#from SenLAST.extract_MODIS import import_polygons
import fiona
import shutil


start_time = datetime.now()

### ----- TIFF Data ----- ###
## Jonas Folder:
# directory = "F:/411/LST/GeoTIFF/Thuringia/scaled"
## Marlin Folder:
directory = "F:/GEO411_data/MODIS_Daten/MODIS_download"

### ----- Shapefile Data ----- ###
## Shapefile Marlin:
shapefolder = "F:/GEO411_data/Daten_Sandra/new/"
shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"
## Shapefile Jonas:
#shapefolder = "C:/Users/jz199/Documents/Studium/Master/2. Semester/Vorlesungsmitschriften/GEO411 - Landschaftsmanagement und Fernerkundung/Auszug_Daten_SandraBauer_MA/Auszug_Daten_SandraBauer_MA/"
#shapefile = "Stationen_Thüringen_Umland_3x3box_reprojected.shp"

shape_path = shapefolder + shapefile


def extract_files_to_list(path_to_folder):
    """
    finds all .tif-files in the corresponding directory
    :return:
    """
    new_list = []

    for filename in os.listdir(path_to_folder):
        if filename.endswith(".tif"):
            new_list.append(os.path.join(path_to_folder, filename))
        else:
            continue
    return new_list

### this function needs to be generalized ###
def import_polygons(shape_path):
    """
    imports the 3x3km polygons of the DWD weather stations
    :return:
    """
    shape_list = []
    acitve_shapefile = fiona.open(shape_path, "r")
    for i in range(0,len(list(acitve_shapefile))-1):
        shapes = [feature["geometry"] for feature in acitve_shapefile]
        shape_list.append(shapes)
    return shape_list


def find_best_stations():
    """
    eliminates the scenes which are not cloud_free
    :return:
    """
    # create new cloud_free directory, overwrite if already exits
    selected_tifs = extract_files_to_list(path_to_folder=directory)

    # import polygons from shapefile
    import_list = import_polygons(shape_path=shape_path)
    station_list = []
    # loop through all .tif files in folder
    for i, tifs in enumerate(selected_tifs):
        src1 = rio.open(selected_tifs[i])
        bool_list = []
        flag = 0   #set boolean flag to 0

        # loop through all weatherstations for each .tif file
        single_station_list = []
        for j, polygons in enumerate(import_list):
            out_image1, out_transform1 = rio.mask.mask(src1, [import_list[0][j]], all_touched=1, crop=True,
                                                       nodata=np.nan)

            # extract nanmean temperature at all stations for each .tif file to eliminate error values
            mean_temp = np.nanmean(out_image1[0])

            single_station_list.append(mean_temp)

            # create boolean values for error values and store in list (-40° is lowest remotely realistic temperature)
            if mean_temp < -40 or np.isnan(mean_temp) == True:
                bool_list.append(False)
            else:
                bool_list.append(True)

        station_list.append(single_station_list)

    print(station_list)
    print(len(station_list))
find_best_stations()